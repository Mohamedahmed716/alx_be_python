length = int(input("Enter the size of the pattern:"))
i = 0
while length > i :
    for j in range(length):
        print("*" * length,end="")
        print()
        i += 1
