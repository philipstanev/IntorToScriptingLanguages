def getArr():
    arr = []
    while True:
        num = int(input("Enter number: "))
        if num == 0:
            break
        else:
            arr.append(num)
    
    return arr

def findMin(arr :list[int]):
    min = arr[0]
    for a in arr:
        if a < min:
            min = a

    return min

def findSteps(arr: list[int]):
    prev = arr[0]
    steps = 0
    for a in arr[1:]:
        if a > prev:
            steps += 1
        
        prev = a

    return steps

def partNegative(arr: list[int]):
    count = 0
    total = len(arr)
    for a in arr:
        if a<0:
            count += 1
    
    return round(count/total, 2)

def main():
    nums = getArr()
    if nums == []:
        print("No numbers")
        return
    
    print(f"Min: {findMin(nums)}")
    print(f"Increasing: {findSteps(nums)}")
    print(f"Negative: {int(partNegative(nums)*100)}%")

if __name__ == '__main__':
    main()