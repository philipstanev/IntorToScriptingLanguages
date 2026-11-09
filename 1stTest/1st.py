def main():
    N = int(input("Enter number: "))
    if N < 0:
        print("Invalid input")
        return
    divisible = 0
    avr = 0
    for _ in range(N):
        num = int(input("Enter number: "))
        if num%3 == 0:
            divisible += 1
        
        if num > 0:
            avr += num
    
    print(f"{divisible} numbers are divisible by 3")
    if avr != 0:
        print(f"The average is: {avr/N}")
    else:
        print("There are no positive numbers")

if __name__ == '__main__':
    main()