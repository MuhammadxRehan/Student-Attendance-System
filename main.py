# Write a Python program to create an attendance management system.


FileName = 'Students.txt'  # This is student file  


def attendance(): # main dunction 
    try:
        name = input('Enter student name: ') # input name from user
        roll_no = input('Enter student Roll no:') # input roll no from user

        found = False  # conditional flag

        with open(FileName , 'r') as file: # open file with read mode
           
            for line in file: # check every line of file 
                if roll_no in line and name in line: # if roll no and name match 
                    found = True  # flag becomes True
                    break
        if found:
            print(f'Roll no {roll_no}.{name} is present!') # when flag True run this         
        else:
            print(f'Roll no {roll_no}.{name} is absent!') # else this line 

    except FileNotFoundError: # error hanndling .
        print('Student is NOT admitted in School yet!') 



#  main menu
while True:
    print('\n---- main menu ----\n')
    print('1. Student Attendace.')
    print('2. Exit')
    choice = input('Enter your choice: ') # input choice from user
    # checks conditions from user input
    if choice == '1':
        attendance()
    elif choice == '2':
        print('Exited..')
        break
    else:
        print('Invalid choice...\nTry again!')












