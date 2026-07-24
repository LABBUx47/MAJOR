# Bank Account Simulator

A simple Python command-line account simulator that records deposits and withdrawals in `account_data.txt` and calculates the current balance from that file.

## What it does

- `1` — deposit an amount and save it as `deposit:<amount>`
- `2` — withdraw an amount and save it as `withdraw:<amount>`
- `3` — calculate and display the current balance from recorded transactions
- `4` — show the raw transaction history stored in `account_data.txt`
- `5` — exit the program

## Interface

This simulator uses a simple command-line interface with a numbered menu.

- The program prints a menu and asks the user to choose an operation by entering `1`, `2`, `3`, `4`, or `5`.
- For deposit and withdrawal, it then asks for a numeric amount.
- Feedback is printed immediately after each action, such as the deposited or withdrawn amount, current balance, or transaction history.

## Real-life UI usage

In a real bank simulator, this backend logic could be connected to a user interface in several ways:

- A desktop GUI could display buttons for Deposit, Withdraw, Balance, History, and Exit instead of typed menu choices.
- A web app could use forms and pages so users click actions and enter amounts in text fields.
- A mobile app could present the same operations as touch buttons and show the balance and history on the screen.

The core backend behavior would remain the same:

- Record each transaction in a persistent store.
- Recalculate balance from transaction records.
- Show transaction history when requested.

This project is a prototype of that backend logic; the UI layer could be added later on top of the current file-based transaction store.

## Files

- `account_simulator.py` — the main script that handles user input and file-based account data storage
- `account_data.txt` — the plain-text transaction log created by the script when deposits or withdrawals are made

## How it works

- Deposits and withdrawals are appended to `account_data.txt`.
- Balance inquiry reads each line in the file and applies deposits as positive values and withdrawals as negative values.
- History prints every saved transaction line-by-line.
- If `account_data.txt` is missing, the script treats balance as `0` and history as empty.

## Prototype backend behavior

This project is a prototype of how a very simple bank simulator backend can work:

- The file `account_data.txt` acts like a transaction store, similar to a database table for transaction records.
- Each transaction is saved as a text entry, showing the operation type and amount.
- The current balance is not stored separately; it is recalculated from the transaction log each time the user requests balance inquiry.
- This is similar to ledger-based accounting, where the balance is derived by applying each transaction in order.
- The script demonstrates the core backend concepts: recording events, reading stored records, and computing derived state from those records.

## Run the simulator

1. Open a terminal in this project folder.
2. Run:

```bash
python account_simulator.py
```

3. Enter one of the operation numbers when prompted:
   - `1` for deposit
   - `2` for withdraw
   - `3` for balance inquiry
   - `4` for history
   - `5` to exit

4. For deposit or withdraw, enter the numeric amount when asked.

## Notes

- The program uses simple file I/O with UTF-8 encoding.
- Invalid menu choices show an error message and do not change the transaction file.
- The transaction file format is `deposit:<amount>` or `withdraw:<amount>`, one entry per line.
- This is a basic learning exercise for Python conditionals, input handling, and file operations.
