balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Balance =", balance)

elif choice == 2:
    amount = int(input("Enter amount: "))
    balance += amount
    print("New balance =", balance)

elif choice == 3:
    amount = int(input("Enter amount: "))
    if amount <= balance:
        balance -= amount
        print("Withdraw successful")
        print("Remaining balance =", balance)
    else:
        print("Insufficient balance")

else:
    print("Invalid option")