st=input("enter string:")

for i in range(0, len(st)):
  if(st[i].islower()):
    st=st.replace(st[i],st[i].upper())
  elif(st[i].isupper()):
    st=st.replace(st[i],st[i].lower())
  else:
    pass
print("string: ",st)
