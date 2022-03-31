## Omar Obeissy
## Integration Project Sprint 2

## This program will help students be successful through:
## time management tools
## GPA calculator.
## Later sprints may include projected graduation term tracker

print("Hi Professor Osheroff and fellow COP1500 students!", end ='')
# Use the end function to have the next print statement come on the same line
#as the previous print statement.
print(" My integration project is an academic tracker and success program!")
print("Project due date:"+"3","25","2022", sep = "/")
# Use the sep command to change the comma from a space to a backslash.
print("Don't forget: " + "Hard work is key! "*5)
# Here I used + to concatanate two strings and * to repeat the string
#"Hard work is key! " five times.
# The following part will output the total study hours per week for each student.
print("The GPA calculator is meant for a range of 1 to 5 classes!")
numClasses = int(input("How many classes are you in this semester? "))
credHours = input("How many credit hours are you enrolled in this semester? ", )
intCreditHours = int(credHours)
studyHours = intCreditHours*(2**2)
#The multiplication operator (*) is used to multiply two numbers.
# The exponential operator (**) takes the first number and
#raises it to the power of the second number.
print("You should spend the following amount of hours outside of class working on schoolwork each week:", studyHours)


#The following part will calculate a students total GPA based on
#projected grades for the current semester.

prevGPA = input("Enter your current GPA coming into this semester: ", )
prevCH = input("Enter your total credit hours completed coming into this semester: ", )
numPrevCH = int(prevCH)
numPrevGPA = float(prevGPA)
print("For the following inputs please enter your grade as a capital letter by itself. Do not put a + or -.")

counter = 1
grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
grade5 = 0
goodInput = not(True)
## Boolean operator not actually sets goodInput to False ##

## For loop for calculating GPA this semester ##
for x in range (numClasses):
    grade = input("Enter your projected grade for a class: ", )
    if grade in ('A', 'B', 'C', 'D', 'F'):
        if grade == 'A':
            grade = 4.0
        elif grade == 'B':
            grade = 3.0
        elif grade == 'C':
            grade = 2.0
        elif grade == 'D':
            grade = 1.0
        elif grade == 'F':
            grade = 0
    else:
        while(goodInput != True):
            ## != means not equal to ##
            ## this while loop makes users put in valid input ##
            print("Invalid input. Please enter a capital letter grade.")
            grade = input("Enter your projected grade for a class: ", )
            if grade in ('A', 'B', 'C', 'D', 'F'):
                if grade == 'A':
                    grade = 4.0
                elif grade == 'B':
                    grade = 3.0
                elif grade == 'C':
                    grade = 2.0
                elif grade == 'D':
                    grade = 1.0
                elif grade == 'F':
                    grade = 0
                goodInput = True

    if counter == 1 and grade1 ==0:
        grade1 = grade
    ##Grade 1 will only save the value of grade if counter=1 and grade1=0 ##
    ## This is only on loop 1 ##   
    elif counter == 2 or grade2==0:
        grade2 = grade
    ## Grade 2 will save the value of grade the first time through the loop##
    ## Since grade=0. But it will resave the second time through the ##
    ## loop since counter = 2. This will leave us with the correct ##
    ## value for grade2. ##
    elif counter == 3:
        grade3 = grade
    elif counter == 4:
        grade4 = grade
    elif counter == 5:
        grade5 = grade
    counter += 1
 ## Shortcut operator +=1 saves counter as (counter = counter+1) ##           
    
##GPA Calculator
#The addition operator (+) is used to add to numeric values.
#The division operator (/) is used to divide two values.


gpaThisSemester = (grade1 + grade2 + grade3 + grade4 + grade5)/(numClasses)
print("Your projected GPA this semester is: ", round(gpaThisSemester, 2))


##A conservative gpa can be optained using
##the floor division operator (//).
##It will round down to the nearest integer. 

floorGpaThisSmtr = (grade1 + grade2 + grade3 + grade4 + grade5)//(numClasses)
print("A conservative projected GPA for this semester is: ", floorGpaThisSmtr)



##Projected GPA Calculator
pctCredHoursThisSemester = intCreditHours / (intCreditHours + numPrevCH)
pctCredHoursPrevSemesters = numPrevCH / (intCreditHours + numPrevCH)
projectedGPA = (gpaThisSemester * pctCredHoursThisSemester) + (numPrevGPA * pctCredHoursPrevSemesters)
print("Your projected total GPA after this semester is: ", round(projectedGPA, 2))

##The following function will display the modulus operator.##
def mod(num1,num2):
    modulo = (num1 % num2)
    return modulo

def main():
    userInput1 = int(input("Enter a number larger than 1: "))
    userInput2 = int(input("Enter a larger number: "))
    while userInput1 > userInput2:
        ## Relational operator > will test if userInput1 ##
        ## Is greater than userInput2. The while loop will
        ## only run in the case that userInput1 is greater.##
        print("Invalid entries. Please try again.")
        userInput1 = int(input("Enter a number larger than 1: "))
        userInput2 = int(input("Enter a larger number: "))
        

    modulus = mod(userInput2, userInput1)
    print(userInput2, "modulus", userInput1,"=", modulus)
main()


    
