from tkinter import *

root = Tk()
root.title("Simple Chatbot")

def send():
    send = "You -> "+e.get()
    txt.insert(END, "\n"+send)
    user = e.get().lower()
    if(user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi!")
    elif(user == "hi" or user == "hii" or user == "hiiii" ):
        txt.insert(END, "\n" + "Bot -> Hello")
    elif(user == "how are you?"):
        txt.insert(END, "\n" + "Bot -> Fine!  You?")
    elif(user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! How can I help you?")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't get you...")
    e.delete(0, END)

txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root,width=88)
e.grid(row=1, column=0)
send = Button(root, 
                text="Send", 
                font=("Bookman Old Style", 15), 
                foreground="white", 
                background="#007bff",  # a bright blue color
                highlightbackground="#007bff", 
                cursor="hand2", 
                borderwidth=0.5, 
                relief="raised", 
                bd=2.5, 
                highlightcolor="green", 
                command=send).grid(row=1, column=1, padx=5, pady=15)
root.mainloop()