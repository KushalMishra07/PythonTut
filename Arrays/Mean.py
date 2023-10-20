
def mean(nums):
    if not nums:
        raise ValueError("List is empty")
    return sum(nums) / len(nums)


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(mean(nums))
#Will be completed tomorrow