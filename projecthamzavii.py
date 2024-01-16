#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
if tarikh>31:
    while tarikh>31:
        messagebox.showerror("Error", "همچين روزي براي پرواز وجود ندارد لطفا اطلاعات خود را دوباره و با دقت وارد كنيد.")
        tarikh=int(input(":لطفا روز پرواز خود را انتخاب كنيد (روز را بين 1 تا 30 انتخاب كنيد)"))
        
sat=int(input(":لطفا ساعت حركت را وارد كنيد (ساعت بين 1 تا 24 باشد)"))
if sat>24:
    while sat>24:
        messagebox.showerror("Error", "همچين ساعتي براي پرواز وجود ندارد")
        sat=int(input(":لطفا ساعت حركت را وارد كنيد (ساعت بين 1 تا 24 باشد)"))
        
bargasht=input("آيا بليط رفت و برگشت ميخواهيد؟(y/n)")
if bargasht=="y":
    tarikh2=int(input("لطفا روز برگشت را انتخاب کنيد(روز را بين 1 تا 30 انتخاب کنيد:"))
    if tarikh2>31:
        while tarikh2>31:
            messagebox.showerror("Error", "همچين روزي براي پرواز وجود ندارد لطفا اطلاعات خود را دوباره و با دقت وارد كنيد.")
            tarikh2=int(input(":لطفا روز پرواز خود را انتخاب كنيد (روز را بين 1 تا 30 انتخاب كنيد)"))
        
    sat2=int(input(":لطفا ساعت حركت را وارد كنيد (ساعت بين 1 تا 24 باشد)"))
    if sat2>24:
        while sat2>24:
            messagebox.showerror("Error", "همچين ساعتي براي پرواز وجود ندارد")
            sat2=int(input(":لطفا ساعت حركت را وارد كنيد (ساعت بين 1 تا 24 باشد)"))
        
elif bargasht!="y" and bargasht!="n":
    messagebox.showerror("Error", "همچين پروازي در ليست وجود ندارد")
    sys.exit(0)

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
0=آبادان
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
            print("------------مشخصات پرواز-------------")
            print("""
نوع پرواز: Domestic flight
نوع صندلي: First class
شماره صندلي:""",len(l1))
            print("مبدا:",m1[mabda])
            print("مقصد:",m1[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")
            if bargasht=="y":
                print("-----------بليط برگشت--------------")
                print("ساعت برگشت:",sat2)
                print(tarikh2,"/1402/10 تاريخ برگشت")
                print("مقصد:",m1[mabda])
                print("مبدا:",m1[maghsad])
            
        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش First class پر شده است لطفا از بخش Economy class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد Economy class هستين(N/Y)؟"))
        
            if num2=="y":
                l2.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("------------مشخصات پرواز-------------")
                print("""
نوع پرواز: Domestic flight
نوع صندلي: Economy class
شماره صدلي:""",len(l2))
                print("مبدا:",m1[mabda])
                print("مقصد:",m1[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")
                if bargasht=="y":
                    print("-----------بليط برگشت--------------")
                    print("ساعت برگشت:",sat2)
                    print(tarikh2,"/1402/10 تاريخ برگشت")
                    print("مقصد:",m1[mabda])
                    print("مبدا:",m1[maghsad])
            
            else:
                print("متاسفانه تمام صندلي هاي پرواز شما پر شده است")
                sys.exit(0)
            
    elif num1==2:
        if len(l2)<20:
            l2.append(1)
            print("-------------------------")
            print("نام:",name)
            print("نام خانوادگي:",fname)
            print("------------مشخصات پرواز-------------")
            print("""
نوع پرواز: Domestic flight
نوع صندلي: Economy class
:شماره صدلي""",len(l2))
            print("مبدا:",m1[mabda])
            print("مقصد:",m1[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")
            if bargasht=="y":
                print("-----------بليط برگشت--------------")
                print("ساعت برگشت:",sat2)
                print(tarikh2,"/1402/10 تاريخ برگشت")
                print("مقصد:",m1[mabda])
                print("مبدا:",m1[maghsad])
            
        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش Economy class پر شده است لطفا از بخش First class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد First class هستين(N/Y)؟"))
        
            if num2=="y":
                l1.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("------------مشخصات پرواز-------------")
                print("""
نوع پرواز: Domestic flight
نوع صندلي: First class
:شماره صدلي""",len(l2))
                print("مبدا:",m1[mabda])
                print("مقصد:",m1[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")
                if bargasht=="y":
                    print("-----------بليط برگشت--------------")
                    print("ساعت برگشت:",sat2)
                    print(tarikh2,"/1402/10 تاريخ برگشت")
                    print("مقصد:",m1[mabda])
                    print("مبدا:",m1[maghsad])
            
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
            print("------------مشخصات پرواز-------------")
            print("""
نوع پرواز: Foreign flight
نوع صندلي: First class
:شماره صدلي""",len(lf1))
            print("مبدا:",m2[mabda])
            print("مقصد:",m2[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")
            if bargasht=="y":
                print("-----------بليط برگشت--------------")
                print("ساعت برگشت:",sat2)
                print(tarikh2,"/1402/10 تاريخ برگشت")
                print("مقصد:",m2[mabda])
                print("مبدا:",m2[maghsad])
        
        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش Economy class پر شده است لطفا از بخش First class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد First class هستين(N/Y)؟"))
        
            if num2=="y":
                lf2.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("------------مشخصات پرواز-------------")
                print("""
نوع پرواز: Foreign flight
نوع صندلي: Economy class
:شماره صدلي""",len(lf2))
                print("مبدا:",m2[mabda])
                print("مقصد:",m2[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")
                if bargasht=="y":
                    print("-----------بليط برگشت--------------")
                    print("ساعت برگشت:",sat2)
                    print(tarikh2,"/1402/10 تاريخ برگشت")
                    print("مقصد:",m2[mabda])
                    print("مبدا:",m2[maghsad])
            
            else:
                print("پرواز مورد نظر شما يافت نشد")
                sys.exit(0)
            
    elif num1==2:
        if len(lf2)<20:
            lf2.append(1)
            print("-------------------------")
            print("نام:",name)
            print("نام خانوادگي:",fname)
            print("------------مشخصات پرواز-------------")
            print("""
نوع پرواز: Foreign flight
نوع صندلي: Economy class
:شماره صدلي""",len(lf2))
            print("مبدا:",m2[mabda])
            print("مقصد:",m2[maghsad])
            print("ساعت پرواز:",sat)
            print(tarikh,"/1402/10 تاريخ پرواز")
            if bargasht=="y":
                print("-----------بليط برگشت--------------")
                print("ساعت برگشت:",sat2)
                print(tarikh2,"/1402/10 تاريخ برگشت")
                print("مقصد:",m2[mabda])
                print("مبدا:",m2[maghsad])
        
        else:
            messagebox.showwarning("Warning","تعداد صندلي هاي بخش First class پر شده است لطفا از بخش Economy class استفاده كنيد")
            num2=(input("آيا شما مايل به خريد Economy class هستين(N/Y)؟"))
        
            if num2=="y":
                lf1.append(1)
                print("-------------------------")
                print("نام:",name)
                print("نام خانوادگي:",fname)
                print("-----------مشخصات پرواز--------------") 
                print("""
نوع پرواز: Foreign flight
نوع صندلي: First class
:شماره صدلي""",len(lf1))
                print("مبدا:",m2[mabda])
                print("مقصد:",m2[maghsad])
                print("ساعت پرواز:",sat)
                print(tarikh,"/1402/10 تاريخ پرواز")
                if bargasht=="y":
                    print("-----------بليط برگشت--------------")
                    print("ساعت برگشت:",sat2)
                    print(tarikh2,"/1402/10 تاريخ برگشت")
                    print("مقصد:",m2[mabda])
                    print("مبدا:",m2[maghsad])
            
            else:
                print("پرواز مورد نظر شما يافت نشد")
                sys.exit(0)
            
    else:
        messagebox.showerror("Error", "شما عددي جز عدد 1 و 2 انتخاب كرده ايد. همچين پروازي وجود ندارد.")
        sys.exit(0)
    
else:
    messagebox.showerror("Error", "همچين پروازي در ليست وجود ندارد")
    sys.exit(0)
    
    

