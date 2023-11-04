m=""
for a in range(0,len(str)):
    if str[a].islower()==True:
        m+=str[a].upper()
    else:
        m+=str[a].lower()
return m
str=input("رشته را وارد کنيد:")
str=charChange(str)
print("پاسخ:",str)
