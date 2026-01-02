Python

print("====ATM SIMULATION SYSTEM====")

pin = 1234
balance = 5000

enetered_pin = int(input("Enter your PIN:"))

if enetered_pin!=pin:
    print("Incorrect PIN")
else:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Choose an opttion:"))

        if choice == 1:
            print("Current Balance: Rupees",balance)
            
        elif choice == 2:
            amount = int(input("Enter amount to deposit: Rupees"))
            balance += amount
            print("Deposited successfully")

        elif choice == 3:
            amount = int(input("Enter amount to wihtdraw: Rupees"))
            if amount>balance:
             print("Insufficient balance")
        else:
            balance -=amount
            print("Please collect your cash")

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid option")

