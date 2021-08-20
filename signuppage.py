from tkinter import *
import os
from PIL import ImageTk,Image

#Main screen
root = Tk()
root.title('Movie Ticketing System')
root.geometry("637x688")
root.resizable(0,0)
root.geometry("638x689")
root.resizable(0,0)
pic=Image.open('CREATE ACC.png')
ren=ImageTk.PhotoImage(pic)
img=Label(root,image=ren)
img.place(x=0,y=0)

def goto_homepage():
    root.destroy()
    os.system('python home.py')

submit_img=Image.open("submit.png")
submit_img=ImageTk.PhotoImage(submit_img)







std_id=Entry(root,bd=8,width=21,relief=FLAT, font=('arial',14,'bold'), bg='#385273', fg='turquoise3')
std_id.place(x=260,y=210)

last=Entry(root,bd=8,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#385273', fg='white')
last.place(x=260,y=260)

email=Entry(root,bd=8,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
email.place(x=260,y=310)


phone=Entry(root,bd=8,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
phone.place(x=260,y=360)


password=Entry(root,bd=8,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
password.place(x=260,y=407)


c_password=Entry(root,bd=8,width=21,relief= FLAT, font=('arial',14,'bold'), bg='#00437c', fg='white')
c_password.place(x=260,y=458)

sub_btn=Button(root,image=submit_img,borderwidth=0,command=goto_homepage,width=287,height=53,highlightthickness=3)
sub_btn.place(x=200,y=510)


root.mainloop()