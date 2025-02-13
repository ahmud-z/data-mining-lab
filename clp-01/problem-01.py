def solve(n, m):
    value1 = n * n + (2 * n * m) + (m * m)
    value2 = (n + m) * (n + m)

    print(f"value-1: ", value1)
    print(f"value-2: ", value2)

    if value1 == value2:
        print("Values are equal")
    else:
        print("Values are not equal")


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    solve(num1, num2)

main()