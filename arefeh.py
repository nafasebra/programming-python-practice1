f=""
for r in range(0,len(str)):
    if str[r].islower()==True:
        f+=str[r].upper()
    else:
        f+=str[r].lower()
return f
str=input("مقدار را وارد کنيد:")
str=charChange(str)
print("پاسخ نهايي:",str)
