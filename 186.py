from tkinter import *
from simplecrypt import encrypt,decrypt
from firebase import firebase

firebase=firebase.FirebaseApplication("",None)

login_window=Tk()
login_window.config(bg="purple")
login_window.geometry("400x400")

user_name=""
your_code=""
your_friends_code=""
message_text=""
message_entry=""

def sendData():
    global user_name
    global message_entry
    global your_code
    
    message=user_name+":"+message_entry.get()
    cipher_code=encrypt('AIM',message)
    hex_string=cipher_code.hex()
    put_date=firebase.put("/",your_code,hex_string)
    

user_name_lbl=Label(login_window,text="Username : ",font="arial 13",bg="purple",fg="white")
user_name_lbl.place(relx=0.3,rely=0.3,anchor=CENTER)

user_name_input=Entry(login_window)
user_name_input.place(relx=0.6,rely=0.3,anchor=CENTER)

your_code_lbl=Label(login_window,text="your code : ",font="arial 13",bg="purple",fg="white")
your_code_lbl.place(relx=0.3,rely=0.4,anchor=CENTER)

your_code_input=Entry(login_window)
your_code_input.place(relx=0.6,rely=0.4,anchor=CENTER)

your_friends_code_lbl=Label(login_window,text="your friends code : ",font="arial 13",bg="purple",fg="white")
your_friends_code_lbl.place(relx=0.3,rely=0.5,anchor=CENTER)

your_friends_code_input=Entry(login_window)
your_friends_code_input.place(relx=0.6,rely=0.5,anchor=CENTER)

def enterRoom():
    global user_name
    global your_code
    global your_friends_code
    global message_text
    global message_entry
    your_code=your_code_input.get()
    your_friends_code=your_friends_code_input.get()
    user_name=user_name_input.get()
    login_window.destroy()
    
    message_window=Tk()
    message_window.config(bg="purple")
    message_window.geometry("600x400")
    
    msg_text=Text(message_window,height=20,width=72)
    msg_text.place(relx=0.5,rely=0.35,anchor=CENTER)
    
    msg_lbl=Label(message_window,text="MESSAGE",font="arial 13",bg="purple",fg="white")
    msg_lbl.place(relx=0.3,rely=0.8,anchor=CENTER)
    
    msg_input=Entry(message_window)
    msg_lbl.place(relx=0.6,rely=0.8,anchor=CENTER)
    
    send_btn=Button(message_window,text="send",command=sendData)
    send_btn.place(relx=0.5,rely=0.9,anchor=CENTER)
    

start_btn=Button(login_window,text="start",command=enterRoom,bg="green",fg="white",relief=FLAT,padx=10)
start_btn.place(relx=0.5,rely=0.65,anchor=(CENTER)

