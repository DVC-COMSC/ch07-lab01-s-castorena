
# ******************************
# Make your Code
# ******************************
#sarah Castorena
# SID 2028049
count =0
numbers = []
while count < 5:
    num = int(input('Enter a number'))
    numbers.append(num)
    count = count +1

sum = sum(numbers) - min(numbers) - max(numbers)   

print(sum)