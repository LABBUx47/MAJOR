"""
Simple Bank Account Simulator
-------------------------------------------------------------
Menu-driven program that lets a user deposit, withdraw, and check
their balance. Every transaction is validated with if/elif/else
logic (e.g. blocking overdrafts and invalid amounts), a running
transaction history is kept in a list of dictionaries, and the
balance is saved to a file so it persists between runs.
"""

BALANCE_FILE = "balance.txt"


def load_balance():
    """Read the saved balance from file; default to 0.0 if none exists."""
    try:
        with open(BALANCE_FILE, "r") as f:
            return float(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0.0


def save_balance(balance):
    """Persist the current balance to file."""
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))


def deposit(balance, history):
    try:
        amount = float(input("Enter amount to deposit: Rs. "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return balance

    if amount <= 0:
        print("Deposit amount must be positive.")
    else:
        balance += amount
        history.append({"type": "Deposit", "amount": amount, "balance_after": balance})
        print(f"Deposited Rs.{amount:.2f}. New balance: Rs.{balance:.2f}")
    return balance


def withdraw(balance, history):
    try:
        amount = float(input("Enter amount to withdraw: Rs. "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return balance

    if amount <= 0:
        print("Withdrawal amount must be positive.")
    elif amount > balance:
        print("Insufficient funds! Transaction denied (overdraft prevented).")
    else:
        balance -= amount
        history.append({"type": "Withdraw", "amount": amount, "balance_after": balance})
        print(f"Withdrew Rs.{amount:.2f}. New balance: Rs.{balance:.2f}")
    return balance


def check_balance(balance):
    print(f"Current balance: Rs.{balance:.2f}")


def show_history(history):
    if not history:
        print("No transactions yet.")
        return
    print("\n--- Transaction History ---")
    for i, txn in enumerate(history, start=1):
        print(f"{i}. {txn['type']:<8} Rs.{txn['amount']:.2f}  (Balance after: Rs.{txn['balance_after']:.2f})")


def main():
    balance = load_balance()
    history = []  # list of dicts — one entry per transaction this session

    print("=== Simple Bank Account Simulator ===")
    print(f"Loaded balance: Rs.{balance:.2f}")

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            balance = deposit(balance, history)
        elif choice == "2":
            balance = withdraw(balance, history)
        elif choice == "3":
            check_balance(balance)
        elif choice == "4":
            show_history(history)
        elif choice == "5":
            save_balance(balance)
            print("Balance saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()