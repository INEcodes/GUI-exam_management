
import mysql.connector as sqlcon
from tkinter import *
import numpy as np


x=0

if x==0:  


  if x==0:
   
        con=sqlcon.connect(host='localhost',user='root',password='1234', database='project',charset='utf8')
        mycur=con.cursor() 
        x=input('Enter the password:')
        str2 = "Select PASSWORD from T_ID where password = '"+str(x)+"'" 
        mycur.execute(str2)
        data=mycur.fetchall()
        for g in data:
            y=g
            print('Password is correct')
         
     

   
    
 
   if  :
       print('Access Granted')

      
       root = Tk()
 

       def getvals():
                rol = rollnoentry.get()
                en = englishentry.get()
                ma = mathsentry.get()
                ph = physicsentry.get() 
                ch = chemistryentry.get()
                ip = ipentry.get()
                total = en+ma+ph+ch+ip 
                percentage = total*1/5
                percentile= np.quantile(total)
    
                conn=sc.connect(host='localhost',user='root',password='1234',database='project',charset='utf8')
                cur=conn.cursor()
                savedata="insert into marks1(rol,english, maths, physics, chemistry, ip, total, percentage, percentile) values(%i, %i, %i, %i, %i, %i, %i, %i)"      
                val = (rol, en, ma, ph, ch, ip, total, percentage, percentile)
                cur.execute(savedata,val)
                conn.commit()
                print('Record Saved Successfuly') 
                conn.close()
                
                
                root.geometry("400x400")
                root.minsize(300,300)
                root.maxsize(330,330)

                root.title("IP PROJECT")

                Label(root, text="Exam Registration Portal", font="BreeSerif 10 bold", pady=10).grid(row=0, column=3)

                #Text for our form
                english = Label(root, text="English", fg="red")
                maths = Label(root, text="Maths", fg="red")
                physics = Label(root, text="Physics", fg="red")
                chemistry = Label(root, text="chemistry", fg="red")
                ip = Label(root, text="IP", fg="red")
                


                #Pack text for our form
                english.grid(row=1, column=2)
                maths.grid(row=2, column=2)
                physics.grid(row=3, column=2)
                chemistry.grid(row=4, column=2)
                ip.grid(row=5,column=2) 
           


                # Tkinter variable for storing entries
                englishvalue = StringVar()
                mathsvalue = StringVar()
                physicsvalue = StringVar()
                chemistryvalue = StringVar()
                ipvalue = StringVar()
                


                #Entries for our form
                englishentry = Entry(root, textvariable=englishvalue)
                mathsentry = Entry(root, textvariable=mathsvalue)
                physicsentry = Entry(root, textvariable=physicsvalue)
                chemistryentry = Entry(root, textvariable=chemistryvalue)
                ipentry = Entry(root, textvariable=ipvalue)
                

                # Packing the Entries
                englishentry.grid(row=1, column=3)
                mathsentry.grid(row=2, column=3)
                physicsentry.grid(row=3, column=3)
                chemistryentry.grid(row=4, column=3)
                ipentry.grid(row=5, column=3)
                

                #Button & packing it and assigning it a command
                Button(text="Submit the marks", command=getvals).grid(row=7, column=3, pady=5) 
                
                root.mainloop()
    
   
    
   
 
   
 
    
 
   else :
        print('Access not granted')
       

