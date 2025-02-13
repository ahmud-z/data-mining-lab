def main():
    myList = []
    sz = int(input("Enter no of inputs you want provide: "))

    for i in range(sz):
        num = input(f"Enter number{i+1}: ")
        num = int(num)
        myList.append(num)

    print(f"Output List: {myList}")

main()
