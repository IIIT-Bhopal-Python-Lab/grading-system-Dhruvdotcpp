#Write your code here in python
def grading():

    marks = input("Enter your marks here: ") # Ask the user to enter marks or type EXIT to quit
    
    if(marks=="EXIT"): # Check if the user wants to exit the program
        print("Exiting the program.")
        return
    
    try: # if I give any input then try should execute but if some error occurs then except should run
        marks = int(marks)
    
        if marks >= 90:
            print("A")
        elif marks >= 75:
            print("B")
        elif marks >= 60:
            print("C")
        elif marks >= 40:
            print("D")
        elif marks >= 0:
            print("F")
        else:
            print("Invalid Input")
        
    except ValueError: # when input is other than digits
        print("Invalid Input")

grading()
# End of Program