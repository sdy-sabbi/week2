# Divya's ATM Simulation program

import time

correct_pin = "2025"
balance_amount = 100000
phone_number = "8888800000"   # Default registered phone number

# ---------------- Welcome Screen ----------------
print("\n" + "=" * 50)
print("               WELCOME TO DIVYA'S ATM")
print("=" * 50)

# ---------------- PIN Verification ----------------
pin = input("\nEnter your 4-digit PIN             : ")

if pin != correct_pin:
    print("\n[ERROR] Incorrect PIN. Access denied.")
    time.sleep(3)
    exit()

print("\nPIN verified successfully.")
time.sleep(3)
print("-" * 50)

# ---------------- ATM Menu ----------------
while True:
    print("\n" + "-" * 50)
    print("                   MAIN MENU")
    print("-" * 50)
    print("1. Balance Enquiry")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change ATM PIN")
    print("5. Change Phone Number")
    print("6. Exit")
    print("-" * 50)

    user_input = int(input("Select an option (1-6)            : "))

    # ----- Balance Enquiry ------
    if user_input == 1:
        print("\n" + "-" * 50)
        print("BALANCE ENQUIRY")
        print("-" * 50)
        print(f"Available Balance : {balance_amount}")
        print("-" * 50)
        time.sleep(3)

    # ------ Deposit Money ------
    elif user_input == 2:
        print("\n" + "-" * 50)
        print("DEPOSIT MONEY")
        print("-" * 50)
        deposit_amount = float(input("Enter deposit amount            : ₹ "))

        if deposit_amount > 0:
            balance_amount = balance_amount + deposit_amount
            print("\nDeposit Successful!")
            print(f"Updated Balance   : {balance_amount}")
        else:
            print("\n[ERROR] Invalid deposit amount.")
        time.sleep(3)

    # ------ Withdraw Money ------
    elif user_input == 3:
        print("\n" + "-" * 50)
        print("WITHDRAW MONEY")
        print("-" * 50)
        withdraw_amount = float(input("Enter withdrawal amount         : ₹ "))

        if withdraw_amount > balance_amount:
            print("\n[ERROR] Insufficient balance.")
        elif withdraw_amount > 0:
            balance_amount = balance_amount - withdraw_amount
            print("\nPlease collect your cash.")
            print(f"Remaining Balance : {balance_amount}")
        else:
            print("\n[ERROR] Invalid withdrawal amount.")
        time.sleep(3)

    # ------ Change ATM PIN ------
    elif user_input == 4:
        print("\n" + "-" * 50)
        print("CHANGE ATM PIN")
        print("-" * 50)

        old_pin = input("Enter current PIN                : ")

        if old_pin != correct_pin:
            print("\n[ERROR] Incorrect current PIN.")
        else:
            new_pin = input("Enter new 4-digit PIN            : ")
            confirm_pin = input("Confirm new PIN                 : ")

            if not (new_pin.isdigit() and len(new_pin) == 4):
                print("\n[ERROR] PIN must be exactly 4 digits.")
            elif new_pin != confirm_pin:
                print("\n[ERROR] PIN confirmation failed.")
            else:
                correct_pin = new_pin
                print("\nATM PIN changed successfully.")
        time.sleep(3)

    # ------ Change Phone Number ------
    elif user_input == 5:
        print("\n" + "-" * 50)
        print("CHANGE PHONE NUMBER")
        print("-" * 50)

        new_phone = input("Enter new 10-digit phone number   : ")

        if not (new_phone.isdigit() and len(new_phone) == 10):
            print("\n[ERROR] Phone number must be 10 digits.")
        else:
            phone_number = new_phone
            print("\nPhone number updated successfully.")
            print(f"Registered Number : {phone_number}")
        time.sleep(3)

    # ------ Exit ------
    elif user_input == 6:
        print("\n" + "=" * 50)
        print("Thank you for using Divya's ATM")
        print("Have a Good day!")
        print("=" * 50)
        time.sleep(3)
        break

    else:
        print("\n[ERROR] Invalid option. Please choose 1-6.")
        time.sleep(3)