for i in range(1, 21, 2):
    print(i, end=' ')
print('\n')
for x in range(0, 101, 10):
    print(x, end=' ')
print('\n')
for y in range(20, 0, -1):
    print(y, end=' ')
print('\n')
number_of_star = int(input("Enter the number of stars: "))
print('*' * number_of_star)

for x in range(0, number_of_star + 1):
    star = x * '*'
    print(star)
