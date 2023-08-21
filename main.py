from tkinter import *
from tkinter import messagebox
from User_Interface import *
from database_connector import *

def makeTable():
    Table_name = ""
    EnteredName = getInput("Enter Table name:")

    #Checking for empty table names and names with spaces
    if EnteredName == "" or not EnteredName:#for empty names
        return
    Tablelist = list(EnteredName)
    for i in range(len(Tablelist)):#removing spaces
        if Tablelist[i] == " ":
            Tablelist[i] = "_"
        Table_name += Tablelist[i]

    #Creating and displaying new tables
    createTable(Table_name)
    displayTable(Table_name)
    
def MainWindow():
    #Getting list of tables available
    Tables = getTableList()
    if len(Tables) == 0:
        FirstVal = ""
    else:
        FirstVal = Tables[0]

    #Functions for buttons
    def Exit():
        response = messagebox.askyesno("Exit","Are you sure you want to exit?")
        if response:
            root_main.quit()
            root_main.destroy()

    def selectTable():
        Table = Option.get()
        displayTable(Table)
    
    #-------User Interface-------
    root_main = Tk()
    root_main.title("TimeTable Manager")
    root_main.configure(background=bg_clr)
    root_main.iconbitmap("UI_elements\Icon.ico")
    root_main.geometry("440x560")

    Option = StringVar(root_main)
    Option.set(FirstVal)

    #main frame
    frame = Frame(root_main,bg = bg_clr2)
    title = Label(frame,text = "TimeTable \nManager",font=("Arial", 36),
                  bg = bg_clr2,fg = white)
    empty = Label(frame,text = "                 ",font=("Arial", 36),
                  bg = bg_clr2,fg = white)
    #table selecting frame
    frame_tselect = Frame(frame,bg = bg_clr2)
    Choose = Label(frame_tselect,text = "Choose Table:",font=("Arial", 16),
                  bg = bg_clr2,fg = white)
    drop = OptionMenu(frame_tselect,Option,*Tables)
    drop.config(bg = bg_clr2,fg = white,borderwidth = 0,width = 15,
                highlightbackground=bg_clr, highlightthickness=3,
                activebackground=bg_clr, activeforeground=white,
                font=("Arial", 10))
    drop["menu"].config(bg=bg_clr,fg = white,borderwidth = 0,
                        activebackground=bg_clr2, activeforeground=white,
                        font=("Arial", 10))
    Button_Confirm = Button(frame_tselect,text = "Confirm",width = 10,
                            activebackground=bg_clr2, activeforeground=white,
                            font=("Arial", 10),bg=bg_clr2,fg=white,
                            command = selectTable)
    #Create and Exit button frame
    frame_CE = Frame(frame,bg = bg_clr2)
    Button_Create = Button(frame_CE,text = "Create Table",width =15,height = 2,
                           activebackground=bg_clr2, activeforeground=white,
                           font=("Arial", 10), bg=bg_clr2,fg=white,
                           command = makeTable)
    Button_Exit = Button(frame_CE,text = "Exit",width =15,height = 2,
                         activebackground=bg_clr2, activeforeground=white,
                         font=("Arial", 10), bg=bg_clr2,fg=white,
                         command = Exit)

    #Placing in grids
    frame.grid(row=0,column=0,padx = 30, pady = 30)
    title.grid(row=0,column=0,padx = 20, pady = 50)
    
    frame_tselect.grid(row=2,column=0,padx = 20, pady = 10)
    Choose.grid(row=0,column=0,padx = 100, pady = 5)
    drop.grid(row=1,column=0,padx = 1, pady = 10)
    Button_Confirm.grid(row=2,column=0,padx = 1, pady = 10)

    frame_CE.grid(row=3,column=0, pady = 40)
    Button_Create.grid(row=0,column=0,padx = 15)
    Button_Exit.grid(row=0,column=1,padx = 15)

    root_main.mainloop()

def Login():
    #Prompting user for password
    Password = getInput("Enter database password:")

    #Initialising with password
    if Password == "" or not Password:
        return
    DB_init(Password)
    MainWindow()
    
    
Login()

