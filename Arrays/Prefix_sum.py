#Asking user to insert elements in List

def prefix_sum(list,le,pre_sum):
     pre_sum[0] = list[0]
     for i in range(1,n):
         pre_sum[i] = pre_sum[i-1] + list[i]






if __name__ == '__main__':

    inputlist = []
    n = int(input("Enter the Number of elements: "))
    i = 0
    for i in range(0,n):
        ele = int(input("Enter the Element"))
        inputlist.append(ele)


print("Lnimit reached")
print(inputlist)
le = len(inputlist)
pre_sum = [0 for i in range(le)]
prefix_sum(inputlist, le, pre_sum)
print("Prefix Sum of the given inputlist:")
for i in range(le):
    print(pre_sum[i]," ",end="")








