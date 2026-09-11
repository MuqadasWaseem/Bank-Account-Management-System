class BankAccount():
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount

    def get_account_number(self):
        return self.__account_number

    def check_balance(self):
        return self.__balance

    def display_account(self):
        print(f"\nAccount Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: Rs{self.__balance:.2f}")


def find_account(accounts, account_number):
    for acc in accounts:
        if acc.get_account_number() == account_number:
            return acc
    return None


accounts = []

while True:
    print("\nBank Account Management System")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        opening_balance = float(input("Enter opening balance (0 or greater): "))

        if opening_balance < 0:
            print("Opening balance cannot be negative.")
            continue

        account = BankAccount(account_number, account_holder, opening_balance)
        accounts.append(account)

        print("Account created successfully.")

    elif choice == 2:
        account_number = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))

        account = find_account(accounts, account_number)

        if account:
            try:
                account.deposit(amount)
                print("Money deposited successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Account not found.")

        print("\nProgram is still running...")

    elif choice == 3:
        account_number = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))

        account = find_account(accounts, account_number)

        if account:
            try:
                account.withdraw(amount)
                print("Money withdrawn successfully.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Account not found.")

        print("\nProgram is still running...")

    elif choice == 4:
        account_number = input("Enter account number: ")

        account = find_account(accounts, account_number)

        if account:
            balance = account.check_balance()
            print(f"Current balance: Rs{balance:.2f}")
        else:
            print("Account not found.")

        print("\nProgram is still running...")

    elif choice == 5:
        account_number = input("Enter account number: ")

        account = find_account(accounts, account_number)

        if account:
            account.display_account()
        else:
            print("Account not found.")

        print("\nProgram is still running...")

    elif choice == 6:
        print("Thank you for using the Bank Account Management System. Goodbye!")
        break