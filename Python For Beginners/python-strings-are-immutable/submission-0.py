def remove_fourth_character(word: str) -> str:
    x = word[0:3]
    y = word[4:]
    z = x+y
    return z


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
