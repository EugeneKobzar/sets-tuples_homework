text_1 = input("Enter first string: ").lower()
text_2 = input("Enter second string: ").lower()
set_1 = set(char for char in text_1 if char.isalpha())
set_2 = set(char for char in text_2 if char.isalpha())
common = set_1 & set_2
if common:
    print("Common letters are", common)
else:
    print("There is no common letter in both strings")