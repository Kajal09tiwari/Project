import os
import pickle

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Balance: ${self.balance}")

    def close_account(self):
        return f"Account {self.username} closed."

class BankingSystem:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        if os.path.exists("users.pkl"):
            with open("users.pkl", "rb") as file:
                self.users = pickle.load(file)

    def save_users(self):
        with open("users.pkl", "wb") as file:
            pickle.dump(self.users, file)

    def register(self, username, password):
        if username in self.users:
            print("Username already exists!")
        else:
            self.users[username] = User(username, password)
            self.save_users()
            print(f"User {username} registered successfully!")

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            print(f"Welcome back, {username}!")
            return user
        else:
            print("Invalid username or password.")
            return None

def main():
    banking_system = BankingSystem()

    while True:
        print("\nBanking System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            banking_system.register(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            user = banking_system.login(username, password)

            if user:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Close Account")
                    print("5. Logout")
                    action = input("Choose an action: ")

                    if action == "1":
                        amount = float(input("Enter amount to deposit: $"))
                        user.deposit(amount)
                    elif action == "2":
                        amount = float(input("Enter amount to withdraw: $"))
                        user.withdraw(amount)
                    elif action == "3":
                        user.check_balance()
                    elif action == "4":
                        print(user.close_account())
                        del banking_system.users[user.username]
                        banking_system.save_users()
                        break
                    elif action == "5":
                        print(f"Logged out successfully.")
                        break
                    else:
                        print("Invalid option.")
        elif choice == "3":
            print("Exiting system...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()




