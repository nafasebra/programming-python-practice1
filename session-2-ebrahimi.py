number = int(input('Enter the number: '))

if(number % 7 == 0):
  print('Saturday...')
elif(number % 6 == 0):
  print('Sunday...')
elif(number % 5 == 0):
  print('Monday...')
elif(number % 4 == 0):
  print('Tuesday...')
elif(number % 3 == 0):
  print('Wendesday...')
elif(number % 2 == 0):
  print('Thursday...')
else:
  print('Friday...')