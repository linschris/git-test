def two_sum(arr, target):
    sum_dict = {} # Returns index of number
    for index, num in enumerate(arr):
        curr_complement = target - num
        if curr_complement in sum_dict:
            complement_index = sum_dict[curr_complement]
            return [complement_index, index]
        sum_dict[num] = index
    return [-1, -1] # Not found

def three_sum(arr, target):
    arr.sort()
    ans = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i + 1
        right = len(arr) - 1
        curr_target = target - arr[i]
        while left < right:
            if arr[left] == arr[left + 1]:
                left += 1
            elif arr[right] == arr[right - 1]:
                right -= 1
            curr_sum = arr[left] + arr[right]

            if curr_sum < curr_target:
                left += 1
            elif curr_sum > curr_target:
                right -= 1
            else:
                ans += [arr[i], arr[left], arr[right]]
                left += 1
    return ans

def main():
    print(two_sum([3,5,9,0,-1,-5], 4)) # Returns [1, 4]
    print(two_sum([], 0)) # Returns [-1,-1]

if __name__ == "__main__":
    main()