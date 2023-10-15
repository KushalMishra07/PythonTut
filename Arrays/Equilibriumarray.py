
#DSA Day 1
def equilibrium(arr):
    lsum = 0
    rsum = 0
    n = len(arr)

    # Check for indexes one by one
    # until an equilibrium index is found
    # adding sum one by one 
    for i in range(n):
        lsum = 0
        rsum = 0

        # get left sum
        for j in range(i):
            lsum += arr[j]

        # get right sum
        for j in range(i + 1, n):
            rsum += arr[j]

        # if lsum and rsum are same,
        # then we are done
        if lsum == rsum:
            return i

    # return -1 if no equilibrium index is found
    return -1

#range

def checkrange(val):
    for i in range(val):
        print(i)

# Driver code
if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]

    # Function call
    print(equilibrium(arr))
