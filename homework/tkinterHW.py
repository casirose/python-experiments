from tkinter import *
import requests

def changeUrl():
    txtName= ent.get()
    r=requests.get('https://tinyurl.com/api-create.php?url='+txtName)
    a=r.text
    txt.insert(0.0, a)
    # print(r.text)

root= Tk()
root.geometry('400x400')

l1=Label (root,text="Enter the URL:")
ent = Entry (root)

l1.grid(row=0)
ent.grid(row = 0, column = 1)

btn = Button(root,text="convert", bg = 'purple', fg = 'white', command=changeUrl) 
btn.grid(row=1, columnspan=2)

txt = Text(root, width = 55, height = 55, wrap =WORD)
txt.grid(row=2,columnspan=2,sticky = W)


root.mainloop()
