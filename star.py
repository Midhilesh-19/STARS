n = int(input("enter ur number: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# reverse
n = int(input("enter ur number: "))
for i in range(1, n + 1):
    print(" "*(n-i) + "*"*i)


# triangle stars
n = int(input("enter ur number: "))
for i in range(1, n + 1):
    print(" "*(n-i)+"* "*i)


# box type
n = int(input("enter ur number: "))
for i in range(n):
    print("* "*n)


# diamond
n = int(input("enter ur number: "))
for i in range(1, n + 1):
    print(" "*(n-i)+"* "*i)
for i in range(n, 0, -1):
    print(" "*(n-i)+"* "*i)

# down
n = int(input("enter ur number: "))

for i in range(n, 0, -1):
    print(" "*(n-i)+"* "*i)
