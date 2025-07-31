def grading():
    # infinite loop to keep asking for input
    while True:
        # Ask the user to enter marks or type EXIT to quit
        marks = input()

        try:
            # Check if the user wants to exit the program
            if marks.upper() == "EXIT":
                return  # Exit the loop

            # Check if the input is not a number
            if not marks.isdigit():
                print("Invalid input. Please enter a number.")
                continue  # Skip to the next loop iteration

            # Convert the input string to an integer
            marks = int(marks)

            # Check if the marks are in valid range
            if marks < 0 or marks > 100:
                print("Invalid input. Marks should be between 0 and 100.")
                continue

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
        except ValueError:
            print("Invalid Input")

grading()
