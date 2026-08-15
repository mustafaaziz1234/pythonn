number= int(input('please enter a number:'))

power= len(str(number))
total = 0

for digit in str(number):
    total = total + int(digit) **power

if total == number:
    print(number, "is a armstrong number")
else:
    print(number, "is not a armstrong number")


        