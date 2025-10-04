# comp163-assignment-5
1. Why you chose each loop type for each challenge

Challenge 1: Collatz Sequence
- I used a while loop because the number of steps to reach 1 is undefined The loop continues until the condition current_number != 1 is false.

Challenge 2: Prime Number Checker
- I used a for loop because we know the exact range of numbers to test for divisibility (from 2 to num-1). A for loop was perfect for iterating over the known range.

Challenge 3: Multiplication Table
- I used nested loops because we need a 2D multiplication table. The outer loop iterates through rows and the inner loop iterates through columns to calculate and print each product.

2. How Your Solutions Work

Challenge 1: Collatz Sequence
- The program asks the user for a starting number.
- It repeatedly updates the number: divide by 2 if even, multiply by 3 and add 1 if odd.
- Each step is counted until the sequence reaches 1.
- The sequence and step count are printed.

Challenge 2: Prime Number Checker
- The program asks the user for a number greater than 1.
- It checks each number from 2 up to the input number minus 1 to see if it divides evenly.
- If a divisor is found, the number is not prime. Otherwise, it is prime.
- The program prints whether the number is prime and shows which divisor caused it to fail if not.

Challenge 3: Multiplication Table
- The program prints a header row for numbers 1–10.
- For each row number, it prints the row number, then iterates through all column numbers to calculate and print the product (table).
- f-strings were used to keep columns aligned, and each row printed on a new line using print() and \n.

3. Any AI Assistance Used

- AI was used to clarify concepts and suggest beginner-friendly formatting.
- The actual code logic and solutions were written and understood by me, not copied from AI.
