import pickle


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def create_account(self):
        self.name = input("Enter your name: ")
        self.balance = int(input("Enter your balance: "))
        print("Account created for {}".format(self.name))
    
    def deposit(self, amount):
        self.balance += amount
        print("You have deposited {}".format(amount))
        print("Your new balance is {}".format(self.balance))
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("You have withdrawn {}".format(amount))
            print("Your new balance is {}".format(self.balance))
        else:
            print("You have insufficient balance")
    
    def show_balance(self):
        print("Your balance is {}".format(self.balance))
    
    def save_account(self):
        with open("account.pkl", "wb") as file:
            pickle.dump(self, file)
            print("Account saved")
    
    @classmethod
    def load_account(cls):
        with open("account.pkl", "rb") as file:
            account = pickle.load(file)
            return account
    
    @staticmethod
    def show_menu():
        print("1. Create an account")
        print("2. Load an account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Show balance")
        print("6. Save account")
        print("7. Exit")

    def run(self):
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.create_account()
            elif choice == 2:
                self.load_account()
            elif choice == 3:
                amount = int(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == 4:
                amount = int(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == 5:
                self.show_balance()
            elif choice == 6:
                self.save_account()
            elif choice == 7:
                break
            else:
                print("Invalid choice")


def main():
    print("Welcome to the banking system")
    name = input("Enter your name: ")
    balance = int(input("Enter your balance: "))
    account = Bank(name, balance)
    account.run()


if __name__ == "__main__":
    main()
