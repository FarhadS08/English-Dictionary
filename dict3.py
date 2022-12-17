from tkinter import *
import json

data = json.load(open('/home/toxic008/Desktop/Python/Dictionary/data.json'))

def translate():
    if word.get() in data:
        list1.delete(0, END)
        list1.insert(END,data[word.get()])
    else:
        pass
      

window = Tk()

window.wm_title('Dictionary')

label2 = Label(window, text = 'Put Word Here')
label2.grid(row=1, column=0)

word = StringVar()
e1= Entry(window, textvariable=word)
e1.grid(row=2, column=0)

b1 = Button(window, text='Show', command=translate)
b1.grid(row=3, column=0)


list1 = Listbox(window, height=6, width=35)
list1.grid(row=4, column=0)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2)



list1.configure(xscrollcommand=sb1.set)
sb1.configure(command=list1.xview)



window.mainloop()