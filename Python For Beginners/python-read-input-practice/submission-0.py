def add_two_numbers() -> int:
    line = input()
    string_list = line.split(",")
    
    sum = 0
    for s in string_list:
        sum += int(s)
    return sum 



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
