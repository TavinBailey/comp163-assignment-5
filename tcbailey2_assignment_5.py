# ==============================
# Challenge 1: Collatz Sequence (WHILE loop)
# ==============================

# Read starting number from user input
current_number = int(input())

# Initialize step counter
step_count = 0

# Print the heading and starting sequence line
print("=== Challenge 1: Collatz Conjecture ===")
print("Enter starting number: Sequence:", end=" ")

# Continue loop until the current number becomes 1
while current_number != 1:
    print(current_number, end=" ")  # print the current number in the sequence
    if current_number % 2 == 0:  # check if the number is even
        current_number = current_number // 2  # divide even number by 2
    else:  # if the number is odd
        current_number = current_number * 3 + 1  # multiply by 3 and add 1
    step_count += 1  # increase the step counter by 1

# Print the last number (1) of the sequence
print(current_number)

# Print the total number of steps taken
print("Steps:", step_count)

# ==============================
# Challenge 2: Prime Number Checker (FOR loop)
# ==============================

print("\n=== Challenge 2: Prime Number Checker ===")

# Read number to check for primality
num = int(input())

# Print the range of divisors being tested
print(f"Enter a number: Testing divisors from 2 to {num - 1}...")

# Assume number is prime until proven otherwise
is_prime = True

# Loop through all possible divisors from 2 up to (num-1)
for divisor in range(2, num):
    if num % divisor == 0:  # if divisible evenly
        print(f"{num}, is not prime (divisible by {divisor})")  # print result
        is_prime = False  # mark as not prime
        break  # exit loop since we found a divisor

# If no divisors found, the number is prime
if is_prime:
    print(f"{num} is prime!")