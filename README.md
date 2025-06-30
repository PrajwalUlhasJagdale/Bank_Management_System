
# 🏦 Bank Account Management System

A fully functional **banking web application** built with **Python**, **Streamlit**, **pandas**, and **NumPy**, applying **Object-Oriented Programming (OOP)** principles. This application allows users to **log in**, **view balance**, **credit/debit funds**, and **send money**, with all changes saved back to a persistent CSV file.

---

## 🚀 Features

- 🔐 **Secure Login**: Authenticate using `CustomerId` and `Password`
- 💰 **Check Balance**: View current account balance after login
- ➕ **Credit Money**: Add funds to your account
- ➖ **Debit Money**: Withdraw funds, ensuring minimum ₹500 balance remains
- 💸 **Send Money**: Transfer money to another customer using their ID
- 📁 **Persistent Data**: All changes are written to the CSV file in real time
- 🧼 **Session Handling**: State management using Streamlit `session_state`
- 🎈 **Interactive UI**: Built using Streamlit's beautiful UI components

---

## 🧠 Technologies Used

- **Python 3.x**
- **Streamlit** - UI framework
- **Pandas** - Data handling and filtering
- **NumPy** - Numeric operations (optional)
- **CSV** - Persistent data storage
- **OOP** - Clean code architecture

---

## 🏗️ Project Structure

```
Bank_app/
│
├── Main.py                          # Streamlit user interface logic
├── Bank.py                          # BankAccount class with all core operations
├── Customer-Records.csv             # Customer data file (live database)
├── Bank_Application_Dataset_filtering.ipynb  # Optional testing notebook
├── requirements.txt                 # List of Python package dependencies
└── README.md                        # Project documentation
```

---

## 🧠 How It Works (Core Logic)

- `BankAccount` class in `Bank.py` handles:
  - **Authentication** via `.validate()` method
  - **Balance checking** via `.get_balance()`
  - **Money updates** via `.credit()`, `.debit()` and `.send_money()`
- `Main.py` handles UI using Streamlit:
  - Shows login form if not logged in
  - After login, displays 4-column dashboard: Check, Credit, Debit, Send
  - Uses `st.session_state` to persist login status
  - Updates saved to CSV via `pandas.to_csv()`

---

## 📦 Dependencies

See `requirements.txt`:

```
streamlit
pandas
numpy
```

## 📌 Notes

- Minimum ₹500 balance required after debit or transfer
- CSV file updates automatically after each transaction
- The project is suitable for learning OOP, Streamlit, and file-based storage

---

## 🙋‍♂️ Author

**Prajwal Jagdale**  



