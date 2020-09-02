for i in range(0, 110, 10):
    print(i, end=" ")

for j in range(21, -1, -1):
    print(j, end=" ")

i = 0
while i < 10:
    print('*', end='')
    i += 1

x = int(input("Number of star:"))
for i in range(x):
    print("* " * (i + 1))