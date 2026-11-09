def isPrime(num :int):
    for i in range(2, num//2):
        if num%i == 0:
            return False

    return True

def findFirstTwins(num :int):
    twins = []
    for i in range(2, num):
        if isPrime(i) and isPrime(i+2) and i<=num:
            twins.append(i)
    
    return twins

def main():
    n = 0
    while n < 5:
        n = int(input("Enter number: "))
    
    twins = findFirstTwins(n)
    for twin in twins:
        print(f"{twin} {twin+2}")

    print(f"Twin count: {len(twins)}")
    print(f"Largest twins: {max(twins)} {max(twins) + 2}")


if __name__ == "__main__":
    main()