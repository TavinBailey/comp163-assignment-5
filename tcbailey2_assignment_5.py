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