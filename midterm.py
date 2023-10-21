1
try:
    name = input("Enter your name, please: ")
    salary = int(input("Enter your desired salary, please: "))
    tax_level = salary * 0.2
    print(name,", your desired salary is: ",tax_level)
except ValueError:
    print(name,"Wrong")

2
addition = lambda x, y: x + y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y
exponentiation = lambda x, y: x ** y
print("Please chose the task you want to perform: 1. Addition 2. Multiplication 3. Division 4. Exponentiation:")
number = int(input("Enter your number: "))
if number in [1, 2, 3, 4]:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
if number == 1:
        result = addition(number1, number2)
elif number == 2:
        result = multiplication(number1, number2)
elif number == 3:
        if number2 == 0:
            result = "Cannot divide to zero"
        else:
            result = division(number1, number2)
else:
        result = exponentiation(number1, number2)
print(f"Result: {result}")


#3
try:
    N = int(input("Enter a positive integer (N): "))
    if N <= 0:
        print("Please enter a positive integer.")
    else:
        a, b = 0, 1
        count = 0
        while count < N:
            print(a, end=' ')
        a, b = b, a + b
        count += 1
    print()
except ValueError:
    print("Write correct integer!")

#4
special = set()
not_special = []
item_list = {}
while True:
    print("Please choose the task you want to perform: 1. Enter items 2. Exit")
    user_choice = input("Enter your choice: ")
    if user_choice == '1':
        number = input("Please enter items: ")
        items = [item.strip() for item in number.split(',')]
        for item in items:
            if item in item_list:
                item_list[item] += 1
            else:
                item_list[item] = 1
        print("Items are saved")
    elif user_choice == '2':
        break
    else:
        print("Goodbye: ")

for item, count in item_list.items():
    if count == 1:
        special.add(item)
    else:
        not_special.append((item, count))

print("Special items:", special)
print("Not special items:", tuple(not_special))