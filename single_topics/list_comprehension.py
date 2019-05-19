nums = [i for i in range(10)]
# n*n for each n in nums
print([n * n for n in nums])

# n in nums if n is even
print([n for n in nums if n % 2 == 0])

# (letter, num) pair for each letter in 'abcd' and each number in '0123'
print([(letter, num) for letter in 'abcd' for num in '0123'])

# Dictionary comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine']

for a, b in zip(names, heros):
    print(a, b)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'Peter'}
print(my_dict)
