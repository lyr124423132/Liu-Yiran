names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

first_initials = [name[0] for name in names]
print(first_initials)

full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

a_names = [name for name in names if name.startswith('A')]
print(a_names)

lowercase_full_names =[]
for i in lowercase_full_names:
    lowercase_full_names.append(name.lower())
print(lowercase_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']

numbers = []
for i in almost_numbers:
    numbers.append(int(i))
print(numbers)

numbers2 =  [ number for number in numbers if (number > 9)]
print(numbers2)