word = input()
vowels = "aeiou"
cons_count = 0
for char in word:
    if char in "bcdfghjklmnpqrstvwxz":
        cons_count += 1
    глас_count = len(word) - cons_count
print(глас_count,cons_count)

