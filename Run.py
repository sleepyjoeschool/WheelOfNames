# IMPORT
import tkinter as tk
import random
import time

# DECLARE Array
# You may remove or append any names when there is a change in student status. The datatype should be STRING (e.g. "Name").
StudentNames = ["Andy", "Amy", "Ethan", "Bob", "David", "Smith", "Kim", "Zellin"] # New samples
#The program will not selected student already being picked. This array will be empty if all student names are picked (number of item = NumberOfStudent) or the function "EmptyStudentNamesBeingPicked" being actived.
StudentNamesAlreadyPicked = []
# It is not necessary to change the number of students in class as the program will automatically obtain the number of items inside it.
NumberOfStudent = len(StudentNames)
# Class detail text display
# Add any details below
ClassDetailTextDisplay = ("GCSE CS Class B, Grade 9. Currently there are" +str(NumberOfStudent) + " " + "names in the list.")
# Open source text display
OpenSourceDisplay = ("Open source via GPL License at: https://github.com/sleepyjoeschool/WheelOfNames")
# Variable for Random
RandomTempVariable = 0
# Variable for Student Name
StudentNamePicked = "Empty"
# Varibale for picked output
SelectedPromotOutput = "Empty2"
# Variable to check if name in the list
IsTheNameInTheList = True
# Variable to check the length of list 2
LengthOfStudentNamesAlreadyPicked = 0

# Global Variable
Display_Name_Status = None

# DECLEAR "RandomStudentNameGen" function
def RandomStudentNameGen():
    global StudentNamesAlreadyPicked
    global Display_Name_Status
    # Remove the content while click
    if Display_Name_Status:
        Display_Name_Status.destroy()
        
    # Generate name
    while True:
        RandomTempVariable = random.randint(0, NumberOfStudent-1) # From 1 to NumberOfStudent
        StudentNamePicked = StudentNames[RandomTempVariable]
        IsTheNameInTheList = StudentNamePicked in StudentNamesAlreadyPicked # Check if name were in the list
        #print (IsTheNameInTheList, StudentNamePicked)
        if IsTheNameInTheList == False:
            time.sleep(0.3)
            StudentNamesAlreadyPicked.append(StudentNamePicked) # Append to the last
            print("Name: " + StudentNamePicked + " " + "was being selected.")
            print ("[INFO] All selected names are:", StudentNamesAlreadyPicked)
            SelectedPromotOutput = ("We have a winner! Name:" + StudentNamePicked + " ")  # Promot content
            Display_Name_Status = tk.Label(TkinterWindow, text=SelectedPromotOutput, font=("Arial", 15))
            Display_Name_Status.pack(pady=10)
            if len(StudentNamesAlreadyPicked) == NumberOfStudent:
                print ("[INFO] All existing names are being picked once! The array is now being reset...")
                StudentNamesAlreadyPicked = []
            break # Exit the loop when the condition is met

        # Display name
# DECLEAR Remove Display Name button function
def RemoveDisplayedName():
    global Display_Name_Status
    if Display_Name_Status:
        Display_Name_Status.destroy()
        Display_Name_Status = None

#DECLEAR EmptyStudentNamesBeingPicked function
def EmptyStudentNamesBeingPicked():
    print ("[INFO]The reset button is clicked manually. The array is now being reset...")
    StudentNamesAlreadyPicked = []

# Setup main Window
TkinterWindow = tk.Tk()
# Set Title name
TkinterWindow.title("Wheel of Names")

# Obtain Display Screen Size
ScreenWidthCalc = TkinterWindow.winfo_screenwidth()
ScreenHeightCalc = TkinterWindow.winfo_screenheight()

# Calculate and set Window
ScreenWidthCalc = int(ScreenWidthCalc / 3)
ScreenHeightCalc = int(ScreenHeightCalc / 3)
TkinterWindow.geometry(f"{ScreenWidthCalc}x{ScreenHeightCalc}+{int((ScreenWidthCalc - ScreenWidthCalc) / 2)}+{int((ScreenHeightCalc - ScreenHeightCalc) / 2)}")


# Title
big_label = tk.Label(TkinterWindow, text="Wheel of Names", font=("Arial", 30))
big_label.pack(pady=20)

# Other detail
small_text2_label = tk.Label(TkinterWindow, text=ClassDetailTextDisplay, font=("Arial", 10))
small_text2_label.pack(pady=10)

# Open source
OpenSourceDisplay_text3_label = tk.Label(TkinterWindow, text=OpenSourceDisplay, font=("Arial", 10))
OpenSourceDisplay_text3_label.pack(pady=10)
# Spin button
button = tk.Button(TkinterWindow, text="Spin!", command=RandomStudentNameGen)
button.pack(pady=20)

# Empty list button
clear_button = tk.Button(TkinterWindow, text="Reset list", command=EmptyStudentNamesBeingPicked)
clear_button.pack(pady=10)

# End
TkinterWindow.mainloop()
