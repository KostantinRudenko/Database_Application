from database import Database
from engine import *
from config import *
from exceptions import *

from tkinter import *

import tkinter.messagebox as mb
import os

window = Tk()

window.geometry(f'{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}')
window.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)
window.title(TITLE)

def open_query_window():
    def send_query(): # This function sends query to the database
        message = mb.askyesno(title='Warning!',
                            message='Are you sure, that you want to send this query?')
        if message:
            database_name = file_name_field.get(0.0, END).strip()
            query = query_field.get(0.0, END).strip()
            for error_value in ERROR_VALUES:
                if error_value in database_name:
                    mb.showerror(title = 'Error',
                                 message = 'Database name consist incorrect values!')
                    raise IncorrectDbNameError
            if len(database_name) == 0 or len(query) == 0:
                mb.showerror(title = 'Error',
                             message = 'Fields cannot be empty!')
            else:
                db = Database(database_name) 
                mb.showinfo(
                            title='Result',
                            message='Query was executed!')
                db.execute_queries(query)  
                if 'SELECT' in query or 'select' in query or 'Select' in query:
                    select_result = db.execute_queries(query, True)
                    if os.path.exists(SAVE_TXT_PATH):
                        rewrite_value = mb.askyesno(title='Question',
                                                    message = 'Do you want to rewrite your changes?')
                        if rewrite_value:
                            save_txt_file(select_result, SELECT_FILENAME)
                        else:
                            save_txt_file(select_result, SELECT_FILENAME, 'a')
                    mb.showinfo(title='Save result',
                                message = 'Result of the "SELECT" value was saved in the "save.txt" file!')
            if save_var.get() == 1:
                query_filename = query_name_field.get(0.0, END).strip() + '.txt'
                write_txt_file(query, query_filename)
                mb.showinfo(title='Result',
                            message='Query was saved in the file!')
    alt_window = Toplevel()
    alt_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    alt_window.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)
    file_name_label = Label(alt_window,
                            text = 'Enter database name below:',
                            width = LABEL_WIDTH,
                            height = LABEL_HEIGHT)

    file_name_field = Text(alt_window,
                           width=ENTRY_WIDTH,
                           height = ENTRY_HEIGHT)

    query_label = Label(alt_window,
                        text = 'Enter query below:',
                        width = LABEL_WIDTH,
                        height = LABEL_HEIGHT)

    query_field = Text(alt_window,
                       width=TEXT_WIDTH,
                       height=TEXT_HEIGHT)
    save_var = IntVar()

    save_query_box = Checkbutton(alt_window, 
                                 text='Save query',
                                 variable = save_var)
    query_name_field = Text(alt_window,
                       width=ENTRY_WIDTH,
                       height=ENTRY_HEIGHT)

    query_button = Button(alt_window,
                        width=BUTTON_WIDTH,
                        height=BUTTON_HEIGHT,
                        text = 'Send!',
                        command=send_query)

    widgets = [file_name_label,
            file_name_field,
            query_label,
            query_field,
            save_query_box,
            query_name_field,
            query_button]

    for widget in widgets:
        widget.pack(anchor='n')

def open_simple_window():
    def send_query(): # This function sends query to the database
        message = mb.askyesno(title='Warning!',
                            message='Are you sure, that you want to send this query?')
        if message:
            database_name = database_field.get(0.0, END).strip()
            table_names_list = tables_field.get(0.0, END).replace(' ', '').strip().split(',')
            for error_value in ERROR_VALUES:
                if error_value in database_name:
                    mb.showerror(title = 'Error',
                                 message = 'Database name consist incorrect values!')
                    raise IncorrectDbNameError
            if len(database_name) == 0 or len(table_names_list) == 0:
                mb.showerror(title = 'Error',
                             message = 'Fields cannot be empty!')
            else:
                db = Database(database_name)
                ddl = ''

                for table_name in table_names_list:
                    ddl += f'CREATE TABLE {table_name} (ID INTEGER);\n'

                print(ddl)
                db.execute_queries(ddl)
                    
                mb.showinfo(title='Result',
                            message='Query was executed!')
                if save_var.get() == 1:
                    query_filename = query_name_field.get(0.0, END).strip() + '.txt'
                    write_txt_file(ddl, query_filename)
                    mb.showinfo(title='Result',
                                message='Query was saved in the file!')
    simple_window = Toplevel()
    simple_window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    simple_window.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)

    database_label = Label(simple_window,
                           text='Enter your database name below:',
                           width=LABEL_WIDTH,
                           height=LABEL_HEIGHT)
    
    database_field = Text(simple_window, 
                           width=ENTRY_WIDTH,
                           height = ENTRY_HEIGHT)

    tables_label = Label(simple_window, 
                         text='Enter your table names below:')
    tables_field = Text(simple_window, 
                         width=SIMPLE_MODE_TEXT_WIDTH,
                         height=SIMPLE_MODE_TEXT_HEIGHT)
    
    save_var = IntVar()

    save_query_box = Checkbutton(simple_window, 
                                 text='Save query',
                                 variable = save_var)
    
    query_name_field = Text(simple_window,
                       width=ENTRY_WIDTH,
                       height=ENTRY_HEIGHT)
    
    submit_button = Button(simple_window,
                           text='Submit!',
                           width=BUTTON_WIDTH,
                           height=BUTTON_HEIGHT,
                           command=send_query)
    
    widgets = [database_label, database_field,
               tables_label, tables_field,
               save_query_box, query_name_field, submit_button]
    
    for widget in widgets:
        widget.pack()

def open_migration_window():
    def migrate():
        ask = mb.askyesno(title='Question',
                          message='Are you sure, that you want to migrate data?')
        try:
            if ask:
                new_db_name = target_field.get(0.0, END).strip()
                file_name = file_name_field.get(0.0, END).strip()
                for error_value in ERROR_VALUES:
                    if error_value in new_db_name or error_value in file_name:
                        mb.showerror(title = 'Error',
                                    message = 'Database name or file name consist incorrect values!')
                        raise IncorrectDbNameError
                if len(new_db_name) == 0 or len(file_name) == 0:
                    mb.showerror(title = 'Error',
                                 message = 'Fields cannot be empty!')
                else:
                    new_db = Database(new_db_name)
                    query = read_txt_file(file_name)
                    new_db.migration_function(new_db_name, query)
                    mb.showinfo(title='Status',
                                message=f'Data was saved to the {new_db_name}.db database!')
        except:
            mb.showerror(title='Error',
                         message='An error was occured, during the migration process.')

    mig_win = Toplevel()
    mig_win.title('Migration')
    mig_win.resizable(RESIZABLE_WIDTH, RESIZABLE_HEIGHT)
    mig_win.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT // 2}')
    
    target_label = Label(mig_win,
                         width=LABEL_WIDTH,
                         height=LABEL_HEIGHT,
                         text='Enter your new database name below:')
    target_field = Text(mig_win,
                        width=ENTRY_WIDTH,
                        height=ENTRY_HEIGHT)
    file_name_label = Label(mig_win,
                         width=LABEL_WIDTH,
                         height=LABEL_HEIGHT,
                         text='Enter your file name:')
    file_name_field = Text(mig_win,
                           width=ENTRY_WIDTH,
                           height=ENTRY_HEIGHT)
    
    start_button = Button(mig_win,
                          width=BUTTON_WIDTH,
                          height=BUTTON_HEIGHT,
                          text='Migrate',
                          command=migrate)
    widgets = [target_label, target_field,
               file_name_label, file_name_field,
               start_button]
    for widget in widgets:
        widget.pack()

main_label = Label(width=LABEL_WIDTH,
                   height=LABEL_HEIGHT,
                   text='Select your option below.')

empty_label1 = Label(width=LABEL_WIDTH,
                    height = LABEL_HEIGHT)

query_button = Button(width=BUTTON_WIDTH,
                     height=BUTTON_HEIGHT,
                     text='Query Mode',
                     command=open_query_window)

empty_label2 = Label(width=LABEL_WIDTH,
                    height=LABEL_HEIGHT)

simple_button = Button(width=BUTTON_WIDTH,
                       height=BUTTON_HEIGHT,
                       text='Simple Mode',
                       command=open_simple_window)

empty_label3 = Label(width=LABEL_WIDTH,
                     height=LABEL_HEIGHT)

migration_button = Button(width=BUTTON_WIDTH,
                          height=BUTTON_HEIGHT,
                          text = 'Migration',
                          command=open_migration_window)
empty_label4 = Label(width=LABEL_WIDTH,
                     height=LABEL_HEIGHT)

help_button = Button(width=BUTTON_WIDTH,
                     height=BUTTON_HEIGHT,
                     text='Help',
                     command=open_help_link)

widgets = [main_label, empty_label1,
           query_button, empty_label2,
           simple_button, empty_label3,
           migration_button, empty_label4,
           help_button]

for widget in widgets:
    widget.pack()

window.mainloop()