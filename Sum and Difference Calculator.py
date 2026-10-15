#Global variables
sum = 0
difference = 0

first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))

def calculate_sum():
    #local variable
    global sum
    sum = first + second

def calculate_difference():
    #local variable
    global difference
    difference = first - second

calculate_sum()
calculate_difference()

print(f"Sum: {sum}")
print(f"Difference: {difference}")

