# P3. Greater Than 10 , Print numbers from 5 to 15
for i in range(5, 16):
    if i > 10:
        print(i, "is BIG")
    else:
        print(i, "is small")
# %%
# Print numbers between 1 and 50 that are divisible by 5
for i in range(1, 51):
    if i % 5 == 0:
        print(i, "is divisible by 5")

# %%
# P4. Fixed Repetition with Condition, Run loop 5 times
for i in range(1, 6):
    if i % 2 == 0:
        print("Hello")
    else:
        print("Hi")

# %%
# P5. Count Evens - Count how many even numbers exist between 1 and 20  , mistake I did
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1
    print(f"The even numbers between 1 to 20 are:", count)
# %%
#P5 Count Evens - Count how many even numbers exist between 1 and 20
count = 0
for i in range(1, 21):
    if i % 2 == 0:
        count += 1

print(f"The even numbers between 1 to 20 are:", count)
# %%
# P6. Count Odds - Count how many odd numbers exist between 10 and 30
count = 0
for i in range(10, 31):
    if i % 2 != 0:
        count += 1

print(f"The even numbers between 1 to 20 are:", count)
# %%
# P7. Count Divisible by 3 - Count numbers divisible by 3 between 1 and 50
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1

print(f"The count of numbers divsible by 3 between 1 to 50 are:", count)

# %%
# P8. Sum of Evens - Find sum of all even numbers between 1 and 20
total = 0
for i in range(1, 21):
    if i % 2 == 0:
        total += i
print(f"The sum of even numbers between 1 to 20 are:", total)
# %%
# P9. Positive, Negative or Zero
num = int(input("Enter a number:"))
if num > 0:
    print(f"The number is Positive")
elif num < 0:
    print(f"The number is Negative")
else:
    print(f"The number is Zero")
# %%
# P10. Number Classification
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"The number is Even")
else:
    print(f"The number is Odd")
# %%
# P11. Multiples Checker
num = int(input("Enter a number:"))
for i in range(1, 21):
    if i % num == 0:
        print(f"Multiple")
    else:
        print(i)

# %%
count = 0
for i in range(10, 31):
    if i % 2 != 0:
        count = count + 1
        print(f"The even numbers between 1 to 20 are:", count)
# %%
count = 0
for i in range(10, 31):
    if i % 2 != 0:
        count = count + 1
print(f"The even numbers between 1 to 20 are:", count)
# %%
# P20. Simple Password Logic - Ask user for number.If number is 4 digits → "Strong" , Else → "Weak"
num = int(input("Set up a password:"))
if num == 4:
    print(f"Your password is strong")
else:
    print(f"Your password is week")
# %%
# P20. Simple Password Logic - Ask user for number.If number is 4 digits → "Strong" , Else → "Weak"
num = input("Set up a password:")
count = 0
for i in num:
    count = count + 1
if count > 4:
    print("strong")
else:
    print("weak")

# %%
# P15. Factor Finder - Print all factors of a number.
n = 6
print(f"The factors of 12 are:")
for i in range(1, 13):
    if n % i == 0:
        print(i)

# %%
# P16. First Non-Multiple - Print numbers from 1 to 20 , Skip numbers divisible by 4 ,Print rest

for num in range(1, 21):
    if num % 4 != 0:
        print(num)
# %%
# P17. Count Digits - Take a number, Print how many digits it has
# (hint: loop over range of number length logic)
num = input("Enter number:")
count = 0
for i in num:
    count += 1

print("It has", count, "digits")
# %%
# p19.Print all prime numbers between 1 and 50
for num in range(2, 51):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num)