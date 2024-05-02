#A WITU Sacco platform that will help students save their money

class Sacco:
    def __init__(self): #  initializing the balance to zero when a new Sacco object is created
        self.balance = 0

    def deposit(self, amount): # checking if the user has deposited amount not less than 1000
        if amount < 1000:
            print("Minimum deposit amount is 1000.")
        else:
            self.balance += amount
            print(f"Deposited {amount:,} successfully.")  # Using commas for thousands separator

    def withdraw(self, amount):
        if amount < 500:
            print("Minimum withdrawal amount is 500.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"You have Withdrawn {amount:,} successfully.")  # Using commas for thousands separator

    def display_balance(self):
        print(f"Your account balance is: {self.balance:,}")  # Using commas for thousands separator

def main():
    sacco = Sacco()
    print("Welcome to WITU Sacco!")

    while True: # displaying a menu of options for the user to choose from
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Account Balance")
        print("4. Quit")

        choice = int(input("Enter your choice: ")) # this will prompt the user to enter the number their choice

        if choice == 1:
            amount = int(input("Enter amount to deposit: ").replace(',', ''))  # Allowing commas in input
            sacco.deposit(amount)
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: ").replace(',', ''))  # Allowing commas in input
            sacco.withdraw(amount)
        elif choice == 3:
            sacco.display_balance()
        elif choice == 4:
            print("Thank you for using WITU Sacco. !")
            break
        else:
            print("Invalid choice. Please select a correct number from the menu.")

if __name__ == "__main__":
    main()
