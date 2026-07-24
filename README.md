# Bank Account Simulator

A simple Python bank account simulator that lets users deposit money, withdraw funds, check the current balance, view transaction history, and exit.

## Features

- Deposit money
- Withdraw money
- Check current balance
- View transaction history
- Simple file-backed storage using `account_data.txt`

## Files

- `account_simulator.py` - main Python script for running the bank account simulator
- `account_data.txt` - transaction log file used to store deposits and withdrawals

## Usage

1. Open a terminal in the project folder.
2. Run the simulator:

```bash
python account_simulator.py
```

3. Choose an operation by entering:
   - `1` for deposit
   - `2` for withdraw
   - `3` for balance inquiry
   - `4` for history
   - `5` to exit

4. For deposits and withdrawals, enter the amount when prompted.

## Notes

- The script stores each transaction in `account_data.txt` in the format `deposit:<amount>` or `withdraw:<amount>`.
- If `account_data.txt` does not exist yet, balance inquiry and history operations will start from zero.
- This project is intended as a basic learning exercise for Python file I/O and conditional logic.
