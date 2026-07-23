    # ...existing code...
    HISTORY = "some history text"  # define this first if needed
    
    with open("account_data.txt", "a", encoding="utf-8") as file:
        file.write(f"transaction history: {HISTORY}\n")