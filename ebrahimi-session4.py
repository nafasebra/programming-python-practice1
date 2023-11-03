string = input('Enter a string: ')

for i in range(0, len(string)):
  if(string[i].islower()):
    string = string.replace(string[i], string[i].upper())
  elif(string[i].isupper()):
    string = string.replace(string[i], string[i].lower())
  else:
    pass

print("Converted string: ", string)