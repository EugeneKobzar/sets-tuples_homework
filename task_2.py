n = int(input("Enter the range (1 to n): "))
multiples_of_3 = [i for i in range(1, 1 + n) if i % 3 == 0]
multiples_of_5 = [i for i in range(1, 1 + n) if i % 5 == 0]
set_3 = set(multiples_of_3)
set_5 = set(multiples_of_5)
common = set_3 & set_5
print("Multiples_of_3:", multiples_of_3)
print("Multiples_of_5:", multiples_of_5)
print("Common numbers:", sorted(common))