# Initialize the sum to 0
total_sum = 0

print("Enter 5 numbers:")

# Loop to take 5 inputs
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    total_sum += num

# Calculate average
average = total_sum / 5

# Display the result
print(f"The average of the 5 numbers is: {average}")
