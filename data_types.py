one = 'first test'
two = 'second'



if(one.endswith('test') or two.endswith('test')):
    print('Found Test')
else:
    print('No Test')    


list_of_numbers = [11, 22, 36, 49, 5, 1, 16, 10]

for number in list_of_numbers:
    if(number > 10):
        print('Large', number)
    elif(number <= 10):
        print('Not large', number)
