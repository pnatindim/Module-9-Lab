# Patric Natindim
# March 15 2025

# Problem 3: Appends user inputted numbers to a list and adds them together
# Continues asking for a number until the sum of the list of numbers is greater than 100

numbers = []        
total_sum = 0        

while total_sum <= 100:
    num = float(input("Number: "))   
    numbers.append(num)                      
    total_sum = sum(numbers)                 
    print(f"List: {numbers}")     
    print(f"Sum: {total_sum}")       

print("The sum is greater than 100.")
print(f"Final list: {numbers}")
