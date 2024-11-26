# Initialize the sum to 0
total_sum = 0

print("Enter 10 numbers:")

# Loop to take 10 inputs
for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    total_sum += num

# Display the result
print(f"The total sum of the 10 numbers is: {total_sum}")
