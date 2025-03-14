# Patric Natindim
# March 13 2025

# Problem 4: A counter that starts at 0 and runs until it reaches 50
# If the value of the counter is divisible by 10, appends the value to the list called tens

counter = 0        
tens = []          

while counter <= 50:
    if counter % 10 == 0:     
        tens.append(counter)  
    counter += 1              

print("List:", tens)
