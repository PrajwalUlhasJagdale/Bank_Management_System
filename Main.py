import pandas as pd
import numpy as np
import streamlit as st
from Bank import BankAccount  # make sure class name is BankAccount

# Load CSV data
df = pd.read_csv("E:/Sumago/Bank_app/Customer-Records.csv")

# 🔒 Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'account' not in st.session_state:
    st.session_state.account = None

# 🏦 App Title
st.title("🏦 Bank Account Management System")

# 🔐 Login Section (only shown if not logged in)
if not st.session_state.get("logged_in", False):
    st.subheader("🔐 Login")

    customer_id_str = st.text_input("Customer ID")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if customer_id_str.strip() == "" or password.strip() == "":
            st.warning("⚠️ Both fields are required.")
        else:
            try:
                customer_id = int(customer_id_str)
                account = BankAccount(customer_id, password, df)

                if account.user is not None:
                    st.session_state.logged_in = True
                    st.session_state.account = account
                    st.success("✅ Login successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid Customer ID or Password.")
            except ValueError:
                st.error("❌ Customer ID must be a valid number.")


# 🧑‍💼 Dashboard (only shown if logged in)
else:
    account = st.session_state.account
    st.subheader(f"👋 Welcome, {account.user['Surname']}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🔍 Check Balance"):
            st.subheader("Checking Balance...")
            st.success(f"Current Balance: ₹{account.get_balance():.2f}")
          

    with col2:
        st.subheader("💰 Credit Amount to your Account")
        credit_amt = st.number_input("Credit Amount", min_value=1.0, key="credit_amt")
        if st.button("➕ Credit"):
            st.subheader("Crediting Amount...")
            account.credit(credit_amt)
            st.success(f"Credited ₹{credit_amt} successfully.")
            st.info(f"Current Balance: ₹{account.get_balance():.2f}")

    with col3:
        st.subheader("💳 Debit Amount from your Account")
        debit_amt = st.number_input("Debit Amount", min_value=1.0, key="debit_amt")
        if st.button("➖ Debit"):
            st.subheader("Debiting Amount...")
            if account.debit(debit_amt):
                st.success(f"Debited ₹{debit_amt} successfully.")
                st.info(f"Current Balance: ₹{account.get_balance():.2f}")
            else:
                st.error("Minimum ₹500 must remain after debit.")

    with col4:
       st.subheader("💸 Send Money to Someone")
       recipient_id_str = st.text_input("Recipient ID", key="recipient_id")

       valid_input = False  # Flag to track input validity
       recipient_id = None

       if recipient_id_str.strip() != '':
          try:
            recipient_id = int(recipient_id_str)
            valid_input = True
          except ValueError:
            st.error("❌ Please enter a valid numeric Recipient ID.")
       else:
        st.warning("⚠️ Please enter the Recipient ID.")

       if valid_input:
        send_amt = st.number_input("Send Amount", min_value=1.0, key="send_amt")
        
        recipient = account.dt.loc[account.dt['CustomerId'] == recipient_id]
        
        if not recipient.empty:
            if st.button("💸 Send"):
                st.subheader("Sending the Money...")
                if account.send_money(recipient_id, send_amt):
                    st.success(f"₹{send_amt} sent to ID {recipient_id}")
                    st.balloons()
                    recipient = account.dt.loc[account.dt['CustomerId'] == recipient_id]
                    st.info(f"Recipient '{recipient['Surname'].values[0]}' Balance: ₹{recipient['Balance'].values[0]:.2f}")
                    st.info(f"Your Balance: ₹{account.get_balance():.2f}")
                else:
                    st.error("❌ Failed: Insufficient balance.")
        else:
            st.error("❌ Recipient not found. Please check the ID.")
 

    # 🚪 Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.account = None
        st.success("Logged out successfully.")
        st.rerun()
