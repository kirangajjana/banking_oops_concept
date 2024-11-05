# Banking Simulation Program

This is a simple **Banking Simulation** application developed using Object-Oriented Programming (OOP) concepts in Python. The application allows users to deposit, withdraw, and take out loans, simulating a basic banking experience. 

## Features

- **Deposit Money**: Add funds to the account.
- **Withdraw Money**: Withdraw funds from the account, with checks on balance availability.
- **Loan Services**: Take a loan of up to ₹5,00,000 (amounts higher than this require additional approval).
- **Exit the Program**: Exit the banking simulation gracefully.

## Class Structure

- **Static Variables**:
  - `bank`: The name of the bank, "Kiran Gajjana Bank".
  - `branch`: The branch location, "Hyderabad".

- **Constructor**:
  - Initializes the user's name and account balance.

- **Instance Methods**:
  - `deposit`: Allows the user to deposit an amount into their account.
  - `withdraw`: Allows the user to withdraw an amount from their account.
  - `loanservice`: Adds a loan amount to the user's account balance.

## Code Overview

The `banking` class includes methods to manage deposit, withdrawal, and loan operations, giving users the flexibility to interact with the account in various ways.

## Getting Started

### Prerequisites

- **Python 3.x**
- **sys module** (comes with Python standard library)

