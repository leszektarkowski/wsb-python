def average(numbers):
    """Calculate average of list"""
    # remember to use correct variables
    # s = sum(nums)
    s = sum(numbers)
    return s/len(numbers)

if __name__ == "__main__":
    l = [1,2,3,4,5]
    if average(l) == 3.0:
        print("Correct")
    else:
        print("Wrong")