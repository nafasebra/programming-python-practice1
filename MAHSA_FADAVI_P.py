# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I_VP7dYyzR9NPygI4TAoAOUB7OpOSsUl

MAHSA FADAVI
"""

from tkinter import *
from tkinter import messagebox
import sys

m1=["tehran","esfahan","shiraz","yazd","kerman"]
m2=["iran","Dubai","Istanbul","Iraq","Korea"]

l1=[]
x=len(l1)
l2=[]
x2=len(l2)

lf1=[]
x=len(lf1)
lf2=[]
x2=len(lf2)

name=(input("لطفا نام خود را وارد كنيد:"))
fname=(input("لطفا نام خانوادگي خود را وارد كنيد:"))

tarikh=int(input(":لطفا روز پرواز خود را انتخاب كنيد (روز را بين 1 تا 30 انتخاب كنيد)"))
if tarikh>30:
    while tarikh>30:
        messagebox.showerror("Error", "همچين روزي براي پرواز وجود ندارد لطفا اطلاعات خود را دوباره و با دقت وارد كنيد.")
        tarikh=int(input(":لطفا روز پرواز خود را انتخاب كنيد (روز را بين 1 تا 30 انتخاب كنيد)"))

sat=int(input(":لطفا ساعت حركت را وارد كنيد (ساعت بين 1 تا 24 باشد)"))
if sat>24:
    while sat>24:
        messagebox.showerror("Error", "همچين ساعتي براي پرواز وجود ندارد")
        sat=int(input(":لطفا ساعت حركت را وارد كنيد (ساعت بين 1 تا 24 باشد)"))

print("""-----------------
d:Domestic flight
f=Foreign flight
-----------------""")

p=(input("لطفا نوع پرواز خود را انتخاب كنيد (d/f)"))

if p=="d":
    print("""------
0=تهران
1=اصفهان
2=شيراز
3=يزد
4=كرمان
------""")
    mabda=int(input("(0/1/2/3/4) لطفا مبدا خود را انتخاب كنيد:"))
    if mabda>4:
        while mabda>4:
            mabda=int(input("(0/1/2/3/4) لطفا مبدا خود را انتخاب كنيد:"))



    print("""---------------
0=تهران
1=اصفهان
2=شيراز
3=يزد
4=كرمان
---------------""")
    maghsad=int(input("(0/1/2/3/4) لطفا مقصد خود را انتخاب كنيد:"))
    if maghsad>4:
        while maghsad>4:
            maghsad=int(input("(0/1/2/3/4) لطفا مقصد خود را انتخاب كنيد:"))



    print("""-----------------
1=First class
2=Economy class
-----------------""")

    num1=int(input("لطفا نوع صندلي خود را انتخاب كنيد (1/2)"))

    if num1==1:
        if len(l1)<20:
            l1.append(1)
            print("-------------------------")
            print("نام:",name)
            print("نام خانوادگي:",fname)
            print("-------------------------")
            print("""
مشخصات پرواز شما
نوع پرواز: Domestic flight
نوع صندلي: First class
شماره صندلي:""",len(l1))
            print("مبدا:",m1[mabda])
            print("مقصد:",m1[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")

        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش First class پر شده است لطفا از بخش Economy class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد Economy class هستين(N/Y)؟"))

            if num2=="y":
                l2.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("-------------------------")
                print("""
مشخصات پرواز شما
نوع پرواز: Domestic flight
نوع صندلي: Economy class
شماره صدلي:""",len(l2))
                print("مبدا:",m1[mabda])
                print("مقصد:",m1[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")

            else:
                print("متاسفانه تمام صندلي هاي پرواز شما پر شده است")
                sys.exit(0)

    elif num1==2:
        if len(l2)<20:
            l2.append(1)
            print("-------------------------")
            print("نام:",name)
            print("نام خانوادگي:",fname)
            print("-------------------------")
            print("""
مشخصات پرواز شما
نوع پرواز: Domestic flight
نوع صندلي: Economy class
:شماره صدلي""",len(l2))
            print("مبدا:",m1[mabda])
            print("مقصد:",m1[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")

        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش Economy class پر شده است لطفا از بخش First class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد First class هستين(N/Y)؟"))

            if num2=="y":
                l1.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("-------------------------")
                print("""
مشخصات پرواز شما
نوع پرواز: Domestic flight
نوع صندلي: First class
:شماره صدلي""",len(l2))
                print("مبدا:",m1[mabda])
                print("مقصد:",m1[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")

            else:
                print("متاسفانه تمام صندلي هاي پرواز شما پر شده است")
                sys.exit(0)

    else:
        while num1>2:
            messagebox.showerror("Error", "شما عددي جز عدد 1 و 2 انتخاب كرده ايد. همچين پروازي وجود ندارد.")
            maghsad=int(input("لطفا نوع صندلي خود را انتخاب كنيد (1/2)"))

elif p=="f":
    print("""------
0=iran
1=Dubai
2=Istanbul
3=Iraq
4=Korea
------""")
    mabda=int(input("(0/1/2/3/4) لطفا مبدا خود را انتخاب كنيد:"))
    if mabda>4:
        while mabda>4:
            mabda=int(input("(0/1/2/3/4) لطفا مبدا خود را انتخاب كنيد:"))



    print("""---------------
0=iran
1=Dubai
2=Istanbul
3=Iraq
4=Korea
---------------""")
    maghsad=int(input("(0/1/2/3/4) لطفا مقصد خود را انتخاب كنيد:"))
    if maghsad>4:
        while maghsad>4:
            maghsad=int(input("(0/1/2/3/4) لطفا مقصد خود را انتخاب كنيد:"))


    print("""-----------------
1=First class
2=Economy class
-----------------""")

    num1=int(input("لطفا نوع صندلي خود را انتخاب كنيد (1/2)"))

    if num1==1:
        if len(lf1)<20:
            lf1.append(1)
            print("-------------------------")
            print("نام:",name)
            print("نام خانوادگي:",fname)
            print("-------------------------")
            print("""
مشخصات پرواز شما
نوع پرواز: Foreign flight
نوع صندلي: First class
:شماره صدلي""",len(lf1))
            print("مبدا:",m2[mabda])
            print("مقصد:",m2[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")

        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش Economy class پر شده است لطفا از بخش First class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد First class هستين(N/Y)؟"))

            if num2=="y":
                lf2.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("-------------------------")
                print("""
مشخصات پرواز شما
نوع پرواز: Foreign flight
نوع صندلي: Economy class
:شماره صدلي""",len(lf2))
                print("مبدا:",m2[mabda])
                print("مقصد:",m2[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")

            else:
                print("پرواز مورد نظر شما يافت نشد")
                sys.exit(0)

    elif num1==2:
        if len(lf2)<20:
            lf2.append(1)
            print("-------------------------")
            print("نام:",name)
            print("نام خانوادگي:",fname)
            print("-------------------------")
            print("""
مشخصات پرواز شما
نوع پرواز: Foreign flight
نوع صندلي: Economy class
:شماره صدلي""",len(lf2))
            print("مبدا:",m2[mabda])
            print("مقصد:",m2[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")

        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش First class پر شده است لطفا از بخش Economy class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد Economy class هستين(N/Y)؟"))

            if num2=="y":
                lf1.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("-------------------------")
                print("""
مشخصات پرواز شما
نوع پرواز: Foreign flight
نوع صندلي: First class
:شماره صدلي""",len(lf1))
                print("مبدا:",m2[mabda])
                print("مقصد:",m2[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")

            else:
                print("پرواز مورد نظر شما يافت نشد")
                sys.exit(0)

    else:
        messagebox.showerror("Error", "شما عددي جز عدد 1 و 2 انتخاب كرده ايد. همچين پروازي وجود ندارد.")
        sys.exit(0)

else:
    messagebox.showerror("Error", "همچين پروازي در ليست وجود ندارد")
    sys.exit(0)




# In[ ]: