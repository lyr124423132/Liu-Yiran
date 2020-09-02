out_file = open("name.txt","w")
name = input("What is your name?")
print(name, file=out_file)
out_file.close()


out_file = open("name.txt","r")
name = out_file.readline()
print("Your name is {}".format(name))
out_file.close()


out_file = open("number.txt","r")
n1 = int(out_file.readline())
n2 = int(out_file.readline())
print(n1+n2)
out_file.close()


out_file = open("number.txt","r")
total = 0
for i in out_file:
    numbers = int(i)
    total +=numbers
print(total)
out_file.close()

