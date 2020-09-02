FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    input_file = open(FILENAME)
    output = ""
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])# Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        output += "{} is taught by {} and has {} students\n".format(parts[0], parts[1], parts[2])
    input_file.close()
    return output


main()