# number patterns
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print('')
# %%
# number patterns
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print('')

# %%
# half-pyramid pattern of numbers , In each row, every next number is incremented by 1.
rows = 25
for i in range(1, rows + 1, 5):
    for j in range(1, i + 1, 3):
        print(j, end=" ")
    print('')
# %%
# inverted number pattern
count = 0
for i in range(5, 0, -1):
    count = count + 1
    for j in range(i, 0, -1):
        print(i, end="")
    print('')
# %%
#inveterd number pattern
count = 0
for i in range(5, 0, -1):
    count = count + 1
    for j in range(1, i + 1):
        print(i, end="")
    print('')
# %%
# inverted number pattern
count = 0
for i in range(5, 0, -1):
    count = count + 1
    for j in range(1, i + 1):
        print(count, end="")
    print('')

#%%
import time

base_amount = 100000

pin = "1234"

phone_num = ""

entered_pin = input("Enter your PIN: ")

if entered_pin == "" or entered_pin != pin:

    print("Invalid PIN. Exiting.")

    exit()

else:

    print("\n")

    print("*" * 50)

    print("\t\t\tPIN Entered is Valid.")

    print("*" * 50)

    while True:

        print("\n")

        print("=" * 70)

        print("\tPlease select the option you want to proceed with")

        print("\t1. Display Balance", " " * 15, "2. Withdraw Amount")

        print("\t3. Deposit Amount ", " " * 15, "4. Exit")

        print("\t5. Change Contact Number", " " * 9, "6. Display Contact Number")

        print("=" * 70)

        inp = input("Enter your choice: ")

        if inp == "1":

            print(f"Your current balance is: ${base_amount}")

            time.sleep(3)

        elif inp == "2":

            withdraw_amount = int(input("Enter amount to withdraw: $"))

            if withdraw_amount < 0:
                print("Invalid amount entered.")

                time.sleep(3)

                continue

            if withdraw_amount > base_amount:

                print("Insufficient balance.")

                time.sleep(3)

            else:

                base_amount -= withdraw_amount

                print(f"Please collect your cash. New balance is: ${base_amount}")

                time.sleep(3)

        elif inp == "3":

            deposit_amount = float(input("Enter amount to deposit: $"))

            if deposit_amount < 0:
                print("Invalid amount entered.")

                time.sleep(3)

                continue

            base_amount += deposit_amount

            print(f"Amount deposited successfully. New balance is: ${base_amount}")

            time.sleep(3)

        elif inp == "4":

            print("Thank you for using our ATM service. Goodbye!")

            break

        elif inp == "5":

            new_phone_num = input("Enter your new contact number: ")

            if len(new_phone_num) != 10 or not new_phone_num.isdigit():

                print("Invalid contact number. Please enter a 10-digit number.")

                time.sleep(3)

            else:

                phone_num = new_phone_num

                print("Contact number updated successfully.")

                time.sleep(3)

        elif inp == "6":

            if phone_num == "":

                print("No contact number found. Please set your contact number first.")

            else:

                print(f"Your contact number is: {phone_num}")

            time.sleep(3)

        else:

            print("Invalid choice. Please try again.")