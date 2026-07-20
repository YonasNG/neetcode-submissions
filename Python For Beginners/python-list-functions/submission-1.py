from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    count = 0
    for x in nums:
        count += x
    return count

def get_min(nums: List[int]) -> int:
    find_min = nums[0]
    for x in nums:
        if x < find_min:
            find_min = x
    return find_min

def get_max(nums: List[int]) -> int:
    cur_max = nums[0]
    for n in nums:
        if n > cur_max:
            cur_max = n
    return cur_max   

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
