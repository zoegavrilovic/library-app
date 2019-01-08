"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend

def get_selected_row(event):  #event holds info about the type of event
    try:
        global selected_tuple  #so that I don't have to use the whole function call but just this var in delete func
        index = list1.curselection()[0]  #to get the index of selected row in lsitbox
        selected_tuple = list1.get(index)  #from the listbox get the tuple with index x
        e1.delete(0,END)  #delete evrtything from the entry
        e1.insert(END, selected_tuple[1])  #when row selected, fill entries
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:  #use this more often!!!!
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(),isbn_text.get()):
    #because xyz_text is a StringVar and not String
        list1.insert(END,row)

def add_command():  #bug!!
    backend.insert(title_text.get(), author_text.get(), year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(),isbn_text.get())) #putting those in a tuple
    #so I don't get each variable in new line
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    #because we are updating what is enetered!! not selected. Selected is by the id, because
    #in backend.py is update blabla WHERE ID is...
    view_command()

window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 2)

l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)

l4 = Label(window, text = "ISBN")
l4.grid(row = 1, column = 2)

title_text = StringVar()
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)  #takes event type and function to bind with event

b1 = Button(window, text = "View all", width = 14, command = view_command)  #no brackets because
#I don't want python to execute view_command when it reads the script but when I press b1
b1.grid(row = 2, column = 3)

b2 = Button(window, text = "Search entry", width = 14, command = search_command)  #wrapper functions,
#good because I can't put brackets here and send parameters, so I need a new function
b2.grid(row = 3, column = 3)

b3 = Button(window, text = "Add entry", width = 14, command = add_command)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = "Update selected", width = 14, command = update_command)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = "Delete selected", width = 14,command = delete_command)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = "Close", width = 14, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()
#pip install pyinstaller to make a standalone executable program
#pyinstaller --onefile --windowed frontend.py
