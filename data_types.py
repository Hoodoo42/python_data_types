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


client = {'username': 'user1', 'age': 24, 'friends':['Anna', 'Beth', 'Carly', 'Diana']}

print(client['username'], client['age'])

for friend in client['friends']:
    print(friend)


clients = [{'username': 'user2', 'age': 26, 'friends':['Terry', 'Bob', 'Carl', 'Dan']}, {'username': 'user3', 'age': 22, 'friends':['Tracy', 'Bev', 'Cara', 'Don']}, {'username': 'user4', 'age': 32, 'friends':['Trey', 'Ben', 'Carla', 'Donna']}]

for client in clients:
    print(client['username'], client['age'], client['friends'])