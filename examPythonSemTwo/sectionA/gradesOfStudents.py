# a program using  functions and conditions to display the grades that the students
# The grades are:
#90%-100% is Grade A
#80%-89% is Grade B
#70%-79% is Grade C
#60%-69% is Grade D
#50%-59% is Grade E
#<50 Fail

def calculateGrades(): # creating a function 
    print('Calculating student Grade')
    mark = int(input('Enter Your socred Marks\t')) # this will prompt the user to input marks scored

#creating the grade system for the marks
    if mark>=90 and mark<=100:
        print('Your Grade is A')

    elif mark>=80 and mark<=89:
        print('Your Grade is B')

    elif mark>=70 and mark<=79:
        print('Your Grade is C')

    elif mark>=60 and mark<=69:
        print('Your Grade is D')

    elif mark>=50 and mark<=59:
        print('Your Grade is E')

    else:
        print('You have Failed')


#calling the function
calculateGrades()