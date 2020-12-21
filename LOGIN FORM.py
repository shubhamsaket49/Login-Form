#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:



from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Login Form")
root.geometry("400x200")
L0=Label(root,text="Login Form",fg="Black",font=('Arabic', 18, 'bold')) 
L0.pack(side=TOP)
L1=Label(root,text="Email or Phone",font=('Sans Serif', 10, 'bold'))
L1.pack(side=TOP)       # side is used for position of text
E1=Entry(root,fg="red",bd=5)  # bd means border size
E1.pack(side=TOP)
L2=Label(root,text="Password",font=('Sans Serif', 10, 'bold')) 
L2.pack(side=TOP)       # side is used for position of text
E2=Entry(root,fg="red",bd=5)  # bd means border size
E2.pack(side=TOP)
L3=Label(root,text="Forget Password",font=('Sans Serif', 10, 'bold'))
L3.pack(side=TOP)
def msg():
    messagebox.showinfo("Message Window","Login Successfully")
b1=Button(root,text="LOGIN", bg="blue",fg="white",bd=5,command=msg)
b1.pack(side=TOP)
L4=Label(root,text="Not a member? Signup now")
L4.pack(side=TOP)
msg()
root.mainloop()


# In[1]:





# In[ ]:




