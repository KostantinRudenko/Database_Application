from database import Database
from config import *

from tkinter import *

import tkinter.messagebox as mb

def send_query(): # This function sends query to the database
    message = mb.askyesno(title='Warning!',
                         message='Are you sure, that you want to send this query?')
    if message:
        database_name = file_name_field.get(0.0, END).strip()
        query = query_field.get(0.0, END)
        db = Database(database_name)
        db.create_query(query)
        mb.showinfo(title='Result',
                    message='Query was executed!')

window = Tk()

window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
window.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)
window.title(TITLE)

file_name_label = Label(text = 'Enter file name below:',
                        width = LABEL_WIDTH,
                        height = LABEL_HEIGHT)

file_name_field = Text(width=ENTRY_WIDTH,
                       height = ENTRY_HEIGHT)

query_label = Label(text = 'Enter query below:',
                        width = LABEL_WIDTH,
                        height = LABEL_HEIGHT)

query_field = Text(width=TEXT_WIDTH,
                   height=TEXT_HEIGHT)

query_button = Button(width=BUTTON_WIDTH,
                      height=BUTTON_HEIGHT,
                      text = 'Send!',
                      command=send_query)

widgets = [file_name_label,
           file_name_field,
           query_label,
           query_field,
           query_button]

for widget in widgets:
    widget.pack()

window.mainloop()