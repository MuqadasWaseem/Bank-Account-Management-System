# Bank Account Management System

A beginner-friendly Python project built using **Object-Oriented Programming (OOP)** concepts. This project simulates a simple bank account management system where users can create accounts, deposit money, withdraw money, check balances, and view account details.

## Features

* Create a new bank account
* Store account number, account holder name, and balance
* Deposit money
* Withdraw money
* Check account balance
* Display account details
* Search for an account using account number
* Validate deposit and withdrawal amounts
* Prevent withdrawals greater than the available balance
* Menu-driven console interface

## OOP Concepts Used

### Class and Object

A `BankAccount` class is created to represent a bank account. Objects of this class represent individual accounts.

### Encapsulation

Private attributes are used to protect account information:

```python
self.__account_number
self.__account_holder
self.__balance
```

### Methods

The `BankAccount` class contains methods for different banking operations:

* `deposit()`
* `withdraw()`
* `get_account_number()`
* `check_balance()`
* `display_account()`

### Exception Handling

`try-except` and `ValueError` are used to handle invalid transactions, including:

* Zero or negative deposit amounts
* Zero or negative withdrawal amounts
* Withdrawals greater than the available balance

### Lists

A Python list is used to store multiple bank account objects:

```python
accounts = []
```

### Loops and Conditional Statements

A `while` loop keeps the program running until the user chooses the Exit option. `if-elif-else` statements handle the user's menu choices.

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* Encapsulation
* Exception Handling
* Lists
* Loops
* Conditional Statements
* User Input

## Project Structure

```text
Bank-Account-Management-System/
│
├── Bank_Acount_Management_System.py
├── README.md
│
└── screenshot/
    └── output.png
```

## Program Menu

```text
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Display Account Details
6. Exit
```

## What I Learned

Through this project, I practiced applying Python OOP concepts to a real-life style application. I learned how to create classes and objects, use encapsulation, create methods, work with lists of objects, handle errors using exceptions, and build a menu-driven console application.

## Future Improvements

Possible future improvements include:

* Account deletion
* Account login/PIN
* Permanent data storage using files or a database
* Transaction history
* Money transfer between accounts
* Graphical User Interface (GUI)

## Project Files

**Python File:** `Bank_Acount_Management_System.py`

**Output Screenshot:** `screenshot/output.png`

