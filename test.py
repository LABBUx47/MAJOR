# import os

# ACCOUNT_FILE = "balance.txt"

# def load_balance():
#     """Reads the balance from the file, or starts at 0.0 if no file exists."""
#     if os.path.exists(ACCOUNT_FILE):
#         with open(ACCOUNT_FILE, "r") as file:
#             try:
#                 # Read the file and convert the string back to a float
#                 return float(file.read().strip())
#             except ValueError:
#                 # If the file is empty or corrupted, default to 0
#                 return 0.0
#     return 0.0

# def save_balance(balance):
#     """Overwrites the file with the new balance."""
#     with open(ACCOUNT_FILE, "w") as file:
#         file.write(str(balance))

# def run_bank():
#     print("Welcome to the Terminal Bank!")
#     # Initialize state from the file
#     balance = load_balance()
    
#     # Main application loop
#     while True:
#         print("\n--- Main Menu ---")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
        
#         choice = input("Select an option (1-4): ").strip()
        
#         # Menu Router & Validation Logic
#         if choice == '1':
#             print(f"💰 Current Balance: ${balance:.2f}")
            
#         elif choice == '2':
#             try:
#                 amount = float(input("Enter amount to deposit: $"))
#                 if amount <= 0:
#                     print("⚠️ Error: Deposit amount must be greater than zero.")
#                 else:
#                     balance += amount
#                     save_balance(balance)
#                     print(f"✅ Success! Deposited ${amount:.2f}.")
#             except ValueError:
#                 print("⚠️ Error: Please enter a valid number.")
                
#         elif choice == '3':
#             try:
#                 amount = float(input("Enter amount to withdraw: $"))
                
#                 # Transaction validation using if/elif
#                 if amount <= 0:
#                     print("⚠️ Error: Withdrawal amount must be greater than zero.")
#                 elif amount > balance:
#                     print(f"🛑 Declined: Insufficient funds. Your balance is only ${balance:.2f}.")
#                 else:
#                     balance -= amount
#                     save_balance(balance)
#                     print(f"✅ Success! Withdrew ${amount:.2f}.")
#             except ValueError:
#                 print("⚠️ Error: Please enter a valid number.")
                
#         elif choice == '4':
#             print("Thank you for banking with us. Goodbye!")
#             break  # Exits the while loop, ending the program
            
#         else:
#             print("⚠️ Invalid choice. Please select 1, 2, 3, or 4.")

# # Run the program
# if __name__ == "__main__":
#     run_bank()


# Read balance from file
try:
    file = open("balance.txt", "r")
    balance = float(file.read())
    file.close()
except:
    balance = 0

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount: "))
        balance += amount
        print("Money Deposited Successfully!")

    elif choice == 2:
        amount = float(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Money Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        file = open("balance.txt", "w")
        file.write(str(balance))
        file.close()
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")





#         print("========💸💸BANK ACCOUNT SIMULATOR💸💸=======")

# while True:
#     OPERATION = input("choose operation: \n 1. DEPOSIT \n 2. WITHDRAW \n 3. BALANCE INQUIRY\n").strip()

#     if OPERATION == "1":
#         print("Deposit selected")
#         try:
#             DEPOSIT = int(input("enter amount: "))
#             print(f"Amount of deposit: {DEPOSIT}")
#         except ValueError:
#             print("Please enter a valid number")
#         break

#     elif OPERATION == "2":
#         print("Withdraw selected")
#         try:
#             WITHDRAW = int(input("Amount you withdraw: "))
#             print(f"withdraw amount: {WITHDRAW}")
#         except ValueError:
#             print("Please enter a valid number")
#         break

#     elif OPERATION == "3":
#         print("BALANCE INQUIRY selected")
#         break

#     else:
#         print("Invalid option. Please choose 1, 2 or 3.")

