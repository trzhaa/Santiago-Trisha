class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        """Initialize the bank account with an account number, owner, and balance (default is 0)."""
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"₱{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw money from the account if sufficient balance exists."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance for this withdrawal.")
        else:
            self.balance -= amount
            print(f"₱{amount} withdrawn successfully.")
    
    def display_balance(self):
        """Display the current account balance."""
        print(f"Account balance: ₱{self.balance}")
        
# Create an account
account = BankAccount(account_number="08432218", owner="Trisha")

# Perform transactions
account.deposit(50000)     # Deposit ₱500
account.withdraw(11000)    # Withdraw ₱200
account.withdraw(41000)    # Try to withdraw more than available
account.display_balance()  # Display the current balance
