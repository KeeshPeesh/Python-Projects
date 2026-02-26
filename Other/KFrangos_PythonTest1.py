balance = 0
transactions = 0

while True:
    print("Select an option by entering a number: ")
    print("1 - Deposit ")
    print("2 - Withdraw ")
    print("3 - Check Balance")
    print("4 - Exit")
    print("Total transactions: ", transactions)
    
    try:
        option = int(input())
    except ValueError:
        print("Invalid input, try again")
    
    if option == 1:
        def deposit(balance, amount):
            return balance + amount
        
        try:
            amount = float(input("Enter the amount to deposit: "))
        except ValueError:
            print("Invalid input, try again")
            continue

        if amount < 0:
            print("No negative deposits, try again")
            continue
        
        balance = deposit(balance, amount)
        transactions += 1
        
    if option == 2:
        def withdraw(balance, amount):
            return balance - amount
        
        try:
            amount = float(input("Enter the amount to withdraw: "))
        except ValueError:
            print("Invalid input, try again")
            continue
        
        balance = withdraw(balance, amount)
        transactions += 1
        
        if amount > balance:
            print("You're broke")
            
    if option == 3:
        print("You have $",balance, "in your account.")
        
    if option == 4:
        break