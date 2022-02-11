def two_sum(arr, target):
    sum_dict = {} # Returns index of number
    for index, num in enumerate(arr):
        curr_complement = target - num
        if curr_complement in sum_dict:
            complement_index = sum_dict[curr_complement]
            return [complement_index, index]
        sum_dict[num] = index
    return [-1, -1] # Not found

def two_sum_two_pointers(arr, target):
    left, right = 0, len(arr) - 1
    arr.sort() # Requires sorting
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return [arr[left], arr[right]] # Returns two numbers instead
    return [None, None]

def main():
    print(two_sum([3,5,9,0,-1,-5], 4)) # Returns [1, 4]
    print(two_sum([], 0)) # Returns [-1,-1]

if __name__ == "__main__":
    main()