
def sorttwoarrays(arr1,n,arr2,n2):
    merged = sorted(arr1+arr2)
    finallength = len(merged)

    if finallength%2 ==1:
        print(float(merged[finallength//2]))

    middle1 = merged[finallength // 2 - 1]
    middle2 = merged[finallength // 2]
    print((float(middle1) + float(middle2)) / 2.0)




if __name__ == '__main__':

    arr1 = []
    arr2 = []
    n = int(input("Enter the Number of elements for List 1: "))
    i = 0
    for i in range(0,n):
        ele = int(input("Enter the Element"))
        arr1.append(ele)

    n2 = int(input("Enter the Number of elements for List 2: "))
    i = 0
    for i in range(0,n2):
        elem = int(input("Enter the Element"))
        arr2.append(elem)

    if not arr1 and not arr2:
        raise ValueError("Both input arrays are empty.")


    print("First list is:", arr1)
    print("Second list is:", arr2)
    sorttwoarrays(arr1,n,arr2,n2)


