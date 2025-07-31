# infinite loop to keep asking for input
# while True:
# Ask the user to enter marks or type EXIT to quit
marks = input()

# Check if the user wants to exit the program
if marks.upper() == "EXIT":
    print("Exiting the program.")
    exit()  # Exit the loop

# Check if the input is not a number
if not marks.isdigit():
    print("Invalid input. Please enter a number.")
    exit()  # Skip to the next loop iteration

# Convert the input string to an integer
marks = int(marks)

# Check if the marks are in valid range
if marks < 0 or marks > 100:
    print("Invalid input. Marks should be between 0 and 100.")
    exit()

# Check the grade based on the marks
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")
