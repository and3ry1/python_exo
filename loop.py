print(*range(5))
print([0, 1, 2, 3, 4])
print(list(range(5)))

for i in [1, 2, 3]:
    print(i)


cars = ['BMW', 'Mercedes', 'Audi']
for car in cars:
    print(car)
    
numberA = input('Saisis un nombre entre 1 et 18: ')

while not numberA.isnumeric() or int(numberA) < 1 or int(numberA) > 18: 
    numberA = input('Saisis un nombre entre 1 et 18: ')



for i in range (int(numberA)):
    if i % 2 == 1:
        continue
    if i == 6:
        break
    print(i)


