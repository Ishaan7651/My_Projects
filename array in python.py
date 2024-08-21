

r = int(input("How many rows do you want?"))
c = int(input("How many columns do you want?"))
arr[i][j]=[]

for i in range(r):
    print("Enter the values of the row")
    for j in range(c):
        arr[i][j]=int(input(""))

for i in range(r):
    print("Enter the values of the row")
    for j in range(c):
        print(arr[i][j],"\t")

("\n")  