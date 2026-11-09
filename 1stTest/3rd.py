def divisorSum(num :int):
    sum = 0
    for i in range(1, num):
        if num%i == 0:
            sum += i

    return sum

def calcRange(a :int, b :int):
    count = 0
    noDiv = True
    for i in range(a, b+1):
        print(divisorSum(i))

        if i == divisorSum(i):
            print(i, end=" ")
            noDiv = False
        elif i > divisorSum(i):
            count += 1
    
    if noDiv:
        print("Няма")

    print("")
    print(f"Изобилни: {count}")

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if a > b:
        a, b = b, a
    
    calcRange(a, b)

if __name__ == "__main__":
    main()