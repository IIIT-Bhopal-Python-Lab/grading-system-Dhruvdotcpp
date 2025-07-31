# Python program to convert marks into grades

def get_grade():
    # Prompt the user to enter marks or type EXIT to quit
    marks = input("Please enter your marks (or type 'EXIT' to quit): ")
    
    # Check if the user wants to exit
    if marks.upper() == "EXIT":
        print("Program terminated.")
        return
    
    try:
        # Attempt to convert the input to an integer
        marks = int(marks)
        
        # Determine grade based on the marks entered
        if 0 <= marks < 40:
            print("Grade: F")
        elif 40 <= marks <= 59:
            print("Grade: D")
        elif 60 <= marks <= 74:
            print("Grade: C")
        elif 75 <= marks <= 89:
            print("Grade: B")
        elif 90 <= marks <= 100:
            print("Grade: A")
        else:
            print("Invalid marks! Please enter a number between 0 and 100.")
    
    except ValueError:
        # Handle non-numeric input
        print("Invalid input! Please enter a valid number between 0 and 100.")

get_grade()

# End of program
