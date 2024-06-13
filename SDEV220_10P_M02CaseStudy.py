# Tracie Lindquist
# SDEV220_10P_M02_Case Study
# Prompt users to enter a student's Last Name name or enter ZZZ to quit
# Prompt users to enter a student's first name
# Prompt users to enter a GPA as a float
# Use a loop to chedk if the student's GPA is greater than 3.5 
# If yes, print a message that the student has qualified for the Dean's list 
# If no, check to see if the student's GPA is greater than 3.25
# If yes, print a message that the student has qualified for the Honor Roll
# If no, break the loop
# Test with at least 5 students 

prompt1 = "Enter the student's last name or enter ZZZ to quit: "
prompt2 = "Enter the student's first name: "
prompt3 = "Enter the student's GPA as X.XX: "

last_name = str(input(prompt1)).lstrip().rstrip().upper() 

while last_name != "ZZZ":
    first_name = str(input(prompt2)).lstrip().rstrip().upper()
    GPA = float(input(prompt3))
    if GPA >= 3.50:
        print (f'{first_name } {last_name} has qualified for the Dean\'s list')
        #break
    elif 3.25 <= GPA <= 3.49:
        print (f'{first_name } {last_name} has qualified for the Honor Roll')
        #break
    else:
        print (f'{first_name } {last_name} GPA: {GPA}')
        print ("End")
        break
    last_name = str(input(prompt1)).lstrip().rstrip().upper()         
    #first_name = str(input(prompt2)).lstrip().rstrip().upper()
    #GPA = float(input(prompt3))
    #last_name = str(input(prompt1)).lstrip().rstrip().upper()
  


