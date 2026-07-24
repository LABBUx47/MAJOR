# Simple Bank Account Simulator
# Users can deposit, withdraw, check their balance , history and Exit.

print("========💸💸BANK ACCOUNT SIMULATOR💸💸=======")
#starting aur ending ki extra spaces ko hatata hai  not b/w the text .strip()
OPERATION = input("choose operation: \n 1. DEPOSIT \n 2. WITHDRAW \n 3. BALANCE INQUIRY\n 4. HISTORY\n 5. EXIT ").strip()

#if aur elif are the conditional statement
if OPERATION == "1":
    print("Deposit selected")
    DEPOSIT = int(input("enter amount: "))

#Here we start file with apend
    with open("account_data.txt", "a", encoding="utf-8") as file:#encoding="utf-8": Translator Dictionary which define the type of the text
        file.write(f"deposit:{DEPOSIT}\n")

    print(f"Amount of deposit: {DEPOSIT}")

elif OPERATION == "2":
    print("Withdraw selected")
    WITHDRAW = int(input("Amount you withdraw: "))

    with open("account_data.txt", "a", encoding="utf-8") as file:
        file.write(f"withdraw:{WITHDRAW}\n")

    print(f"withdraw amount: {WITHDRAW}")

elif OPERATION == "3":
    print("BALANCE INQUIRY selected")
    balance = 0 # defining intial balence zero

    try:# keyword that handle Errors (crashes) 
        with open("account_data.txt", "r", encoding="utf-8") as file:
            for line in file:#This reads the file line by line.
                line = line.strip()#Removes extra spaces or blank spaces from the line.
                if not line:#if line is empty,skip it
                    continue

                operation, amount = line.split(":", 1)# spliting line and convert text ammount into int
                amount = int(amount)

                if operation == "deposit":
                    balance += amount
                elif operation == "withdraw":
                    balance -= amount
    except (FileNotFoundError, ValueError):#Exception Handling
        balance = 0

    print(f"Current balance: {balance}")

elif OPERATION == "4":
    print("HISTORY:")

    try:#erroe crashes
        with open("account_data.txt", "r", encoding="utf-8") as file:
            history_lines = file.readlines()

        if history_lines:
            print("Transaction history:")
            for line in history_lines:
                print(line.strip())
        else:
            print("No transaction history yet.")
    except FileNotFoundError:
        print("No transaction history yet.")


elif OPERATION == "5":
    print("EXIT")

else:
    print("Invalid option. Please choose 1, 2 , 3 , 4 or 5")

