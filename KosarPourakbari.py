r=""
for h in range(0,len(str)):
    if str[h].islower()==True:
        r+=str[h].upper()
    else:
        r+=str[h].lower()
return r
str=input("Enter a string:")
str=charChange(str)
print("Result is",str)
