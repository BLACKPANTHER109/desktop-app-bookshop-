from tkinter import*
import backend

def get_selected_row(event):
    global selected_tuple
    index=list_box.curselection()[0]
    selected_tuple=list_box.get(index)

    title_entry.delete(0,END)
    title_entry.insert(END,selected_tuple[1])

    author_entry.delete(0,END)
    author_entry.insert(END,selected_tuple[2])

    year_entry.delete(0,END)
    year_entry.insert(END,selected_tuple[3])

    isbn_entry.delete(0,END)
    isbn_entry.insert(END,selected_tuple[4])

def close_command():
    window.destroy()

def view_all_command():
    list_box.delete(0,END)
    for row in backend.view():
        list_box.insert(END,row)

def search_command():
    list_box.delete(0,END)
    for row in backend.search(title_text_entry.get(),author_text_entry.get(),year_text_entry.get(),isbn_text_entry.get()):
        list_box.insert(END,row)

def add_entry_command():
    list_box.delete(0,END)
    backend.insert(title_text_entry.get(),author_text_entry.get(),year_text_entry.get(),isbn_text_entry.get())
    list_box.insert(END,(title_text_entry.get(),author_text_entry.get(),year_text_entry.get(),isbn_text_entry.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text_entry.get(),author_text_entry.get(),year_text_entry.get(),isbn_text_entry.get())


window=Tk()

window.title("BookStore")

title_label=Label(window,text="Title")
title_label.grid(row=0,column=0)

author_label=Label(window,text="author")
author_label.grid(row=0,column=2)

year_label=Label(window,text="Year")
year_label.grid(row=1,column=0)

isbn_label=Label(window,text="ISBN")
isbn_label.grid(row=1,column=2)

title_text_entry=StringVar()
title_entry=Entry(window,textvariable=title_text_entry)
title_entry.grid(row=0,column=1)

author_text_entry=StringVar()
author_entry=Entry(window,textvariable=author_text_entry)
author_entry.grid(row=0,column=3)

year_text_entry=StringVar()
year_entry=Entry(window,textvariable=year_text_entry)
year_entry.grid(row=1,column=1)

isbn_text_entry=StringVar()
isbn_entry=Entry(window,textvariable=isbn_text_entry)
isbn_entry.grid(row=1,column=3)

list_box=Listbox(window,height=6,width=35)
list_box.grid(row=2,column=0,rowspan=6,columnspan=2)

list_box.bind('<<ListboxSelect>>',get_selected_row)

scroll_bar=Scrollbar(window)
scroll_bar.grid(row=2,column=2,rowspan=6)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_box.yview)

view_all_button=Button(window,text="View all",width=12,command=view_all_command)
view_all_button.grid(row=2,column=3)

search_button=Button(window,text="Search",width=12,command=search_command)
search_button.grid(row=3,column=3)

add_entry_button=Button(window,text="Add entry",width=12,command=add_entry_command)
add_entry_button.grid(row=4,column=3)

update_button=Button(window,text="Update",width=12,command=update_command)
update_button.grid(row=5,column=3)

delete_button=Button(window,text="Delete",width=12,command=delete_command)
delete_button.grid(row=6,column=3)

close_button=Button(window,text="Close",width=12,command=close_command)
close_button.grid(row=7,column=3)

window.mainloop()
