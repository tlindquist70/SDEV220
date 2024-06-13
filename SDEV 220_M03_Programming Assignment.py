# # SDEV 220_M03_Programming Assignment
# # Loops and Conditionals
# # Tracie Lindquist

# # 7.4
# # Create a list called strings with the following elements: mozzarella, cinderella, salmonella

# things = ['mozzarella', 'cinderella', 'salmonella']

# #7.5 capitalize the element that refers to a person and then print the list
# things[1] = things[1].capitalize()
# print (f'{things}')

# #7.6 Make the cheesy elements all upppercase and then print the list
# things[0] = things[0].capitalize()
# things[2] = things[2].capitalize()
# print(f'{things}')

# #7.7 Remove the disease element from the list, collect your Nobel Prize, and print the list
# print(f'Congratulations on your Nobel Prize for eliminating {things[2]}!')
# things.pop(2)
# print(f'{things}')

# #9.1 Create a function called good() that returns the following list ['Harry', 'Ron', 'Hermione']

# def good(): 
#     return['Harry','Ron','Hermione']

# good()

#9.2 Define a generator function called get_odds() that returns odd numbers from a range 10
#Use a for loop to find and print the third value returned

def get_odds(): 
    odds = []
    for num in range(10):
        if num % 2 ==1:
            odds.append(num)
    print(f'The third odd number is {odds[2]}')
get_odds()

# the hard way

def get_odds():
    for number in range(1, 10, 2):
        yield number
    
count = 1
for number in get_odds():
    if count == 3:
        print (f'The third number is {number}.')
        break
    count += 1

