"""
Name: Liu Yiran
Date started: 11/8/2020
GitHub URL:https://github.com/JCUS-CP1404/assignment-1-travel-tracker-lyr124423132.git
"""
# Import CSV file and append them to a list. Frame work of main function done.

import csv

place_list = []

with open('places.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
        place_list.append(line)

place_list.sort(
    key=lambda l: (l[1], l[0])
)


def main():

    print('{} places loaded from places.csv'.format(len(place_list)))
    Menu()

# 递归法改的菜单
def Menu():
    choice = input(  # Get input and change to lower case
            '\nMenu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n>>> ').lower()
    if choice == 'l':  # Selection
        place_list.sort(key=lambda l: (l[1], l[0]))
        List_Places()
        Menu()
    elif choice == 'a':
        Add_new_places()
        Menu()
    elif choice == 'm':
        Markplacevisited()
        Menu()
    elif choice=="q":
        with open('places.csv', 'w', newline='\n') as f:  # Write to csv and quit
            writer = csv.writer(f)
            for i in place_list:
                writer.writerow(i)
        print('{} places saved to places.csv\nHave a nice day :)'.format(len(place_list)))
    else:
         print('Invalid Menu Choice!')
         Menu()


# List all places.
def List_Places():
    visited = 0
    unvisited = 0
    for i in range(len(place_list)):

        if(place_list[i][-1] == 'u'):
            unvisited += 1
            print('  {}. * {} - {}  ({})'.format(i, place_list[i][0], place_list[i][1], place_list[i][2]))
        else:
            visited += 1
            print('  {}.   {} - {}  ({})'.format(i, place_list[i][0], place_list[i][1], place_list[i][2]))

    print('{} places visited, You still want to visit {} places'.format(visited, unvisited))


# 运用递归法添加地点
def Add_new_places():
    name = noblankinput("Name:")
    country = noblankinput('Country: ')
    priority = numinput('Priority: ','Invalid input; enter a valid number')
    print('{} by {} ({}) added to place list'.format(name, country, priority))
    place = [name, country, priority, 'u']
    place_list.append(place)

#数字输入递归
def numinput(title,errorwords):
     try:
         num=int(input(title))
         if num>0:
             return num
         else:
             print("数字必须大于0")
             numinput(title,errorwords)
     except:  # Exception
            print(errorwords)
            return numinput(title,errorwords)

#拒绝空输入
def noblankinput(title):
    name = input(title)
    if(name == ''):
        print('Input cannot be blank')
        return inputname()
    else:
        return name

# Function for marking a place as visited
def  Markplacevisited():
    visited = 0
    # See whether a place is visited or unvisited
    for i in place_list:
        if i[-1] == 'l':
            visited += 1
        else:
            visited -= 1
    if (visited == len(place_list)):
        print('No more places to visited!')
        return
    else:

        invalid = True
        while invalid:
            number = input('Enter the number of place to mark as visited\n>>>')
            invalid = MarkplacevisitedHandler(number)

        if (place_list[int(number)][3] == 'l'):
            print('You have already learned {}'.format(place_list[int(number)][0]))

        elif (place_list[int(number)][3] == 'u'):
            print('{} by {} learned '.format(place_list[int(number)][0], place_list[int(number)][1]))
            place_list[int(number)][3] = 'l'


# Function for handling correct output for marking a place as visited
def  MarkplacevisitedHandler(number):
    try:
        number = int(number)
    except:
        print('Invalid input; enter a valid number')
        return True
    if number < 0:
        print('Number must be >= 0')
        return True
    elif number >= len(place_list):
        print('Invalid place number')
        return True
    else:
        return False


main()  # Activate main function