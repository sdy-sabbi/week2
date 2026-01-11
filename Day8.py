#Practicing programs for if-else, elif.
# %%
#checking the age with if, elif and else blocks
age = int(input("What is your age? "))

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 55:
    print("Adult")
else:
    print("Senior Citizen")
# %%
#checking the larget number with if - else
a = 70
b = 100

if a > b:
    print("a is greater")
else:
    print("b is greater")
# %%
#Checking the availability of the user for session (morning/afternoon/evening batches)
time = int(input("Please enter your available time: "))

if time < 12:
    print("Morning batch")
elif time <= 4:
    print("Afternoon batch")
else:
    print("Evening batch")
# %%
#Checking the availability of the user for session (morning/afternoon/evening batches) in 24hours format
time = int(input("Please enter your available time(in 24 hours format): "))
if time < 12:
    print("Morning batch")
elif time <= 16:
    print("Afternoon batch")
else:
    print("Evening batch")