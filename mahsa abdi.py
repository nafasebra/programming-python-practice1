h=""
for s in range(0,len(str)):
    if str[s].islower()==True:
        h+=str[s].upper()
    else:
        h+=str[s].lower()
return h
str=input("عدد مورد نظر را وارد کنيد:")
str=charChange(str)
print("نتيجه:",str)
