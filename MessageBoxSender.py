
def Message(title,msg,type="error"):
    from tkinter import messagebox
    if type == "error":
        messagebox.showerror(title, msg)
    elif type == "warning":
        messagebox.showwarning(title, msg)
    elif type == "info":
        messagebox.showinfo(title,msg)
    else:
        messagebox.showerror("MessageBoxSender error", 'Value error at "Message" function: Invalid value for "type"\n\nUsable values are:\n"error"\n"info"\n"warning"')
Message(input("Input the message title\n"),input("Input the message title\n"),input("Input the message type\n"))
