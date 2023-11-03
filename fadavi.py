d=""
for e in range(0,len(str)):
    if str[e].islower()==True:
        d+=str[e].upper()
    else:
        d+=str[e].lower()
return d
str=input("مقدار را واردکنيد:")
str=charChange(str)
print("نتيجه:",str)
