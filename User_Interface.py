from tkinter import *
from database_connector import *

#Colors
bg_clr = "#383838"
bg_clr2 = "#212121"
black = "#000000"
white = "#ffffff"
    
def displayTable(Tablename):
    #Getting table's items
    rows_data,clms,row_count,clm_count = getTableData(Tablename)
    
    #-------User Interface-------

    #---Display window---
    global root
    root = Tk()
    root.title(Tablename)
    root.configure(background=bg_clr)
    root.iconbitmap("UI_elements\Icon.ico")

    #Main frame
    Grid.rowconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    frame = Frame(root, bg = bg_clr2)
    label = Label(root,text = Tablename.upper(),height = 1,font=("Arial", 25),bg = bg_clr2,fg = white)
    frame.grid(row=1, column=1, sticky=N+S+E+W,padx = 20, pady = 10,columnspan = 5)
    label.grid(row=0, column=3,sticky=E+W,padx = 1, pady = 1,ipadx = 1, ipady = 10)
    
    #Creating Table
    for row_index in range(row_count+1):#for rows
        Grid.rowconfigure(frame, row_index, weight=1)
        
        #creating first row
        if row_index == 0:
            #creating columns in first row
            for col_index in range(clm_count):
                Grid.columnconfigure(frame, col_index, weight=1)
                btn = Button(frame,text = clms[col_index],
                             activebackground=bg_clr2, activeforeground=white,
                             bg = bg_clr2,fg = white,width = 15,height = 1)
                btn.grid(row=row_index, column=col_index,
                         padx = 0, pady = 0,ipadx = 10, ipady = 10)
                
        #creating data rows
        else:
            #creating columns in data rows
            for col_index in range(clm_count):
                Grid.columnconfigure(frame, col_index, weight=1)
                btn = Button(frame,text = rows_data[row_index-1][col_index],
                             command = lambda row=row_index,col=col_index:updateTable(Tablename,row,col),
                             activebackground=bg_clr2, activeforeground=white,
                             bg = bg_clr2 ,fg = white,width = 16,height = 1)
                btn.grid(row=row_index, column=col_index,
                         padx = 0, pady = 0,ipadx = 5, ipady = 5)

    root.mainloop()

def getInput(DisplayText):
    #Functions for buttons
    def Confirm():
        global item
        item = entry.get()
        root1.quit()
        root1.destroy()
    def Cancel():
        global item
        item = False
        root1.quit()
        root1.destroy()

    #-------User Interface-------
    root1 = Tk()
    root1.title("Input")
    root1.configure(background=bg_clr)
    root1.iconbitmap("UI_elements\Icon.ico")

    #Main frame
    frame = Frame(root1, bg = bg_clr2)
    label = Label(frame,text = DisplayText,font=("Arial", 12),bg = bg_clr2,fg = white)
    entry = Entry(frame,width = 40, borderwidth = 2,bg = bg_clr2,fg = white)
    Button_confirm = Button(frame,text = "Confirm",width = 10, command = Confirm,
                            activebackground=bg_clr2, activeforeground=white,
                            bg = bg_clr2,fg = white)
    Button_cancel = Button(frame,text = "Cancel",width = 10, command = Cancel,
                           activebackground=bg_clr2, activeforeground=white,
                           bg = bg_clr2,fg = white)
    #Placing in grids
    frame.grid(row=1, column=1, sticky=N+S+E+W,padx = 20, pady = 20)
    label.grid(row=0, column=0)
    entry.grid(row=1,column = 0,padx = 5, pady = 5, sticky=N+S+E+W)
    Button_confirm.grid(row=1, column=1, padx = 2, pady = 2, sticky=N+S+E+W)
    Button_cancel.grid(row=1, column=2, padx = 2,pady = 2, sticky=N+S+E+W)

    root1.mainloop()

    return item

def updateTable(Tablename,r,c):
    #Getting table's items
    rows_data,clms,row_count,clm_count = getTableData(Tablename)
    c_name = clms[c]
    r_name = rows_data[r-1][0]

    #Prompting user to enter new value
    if c <= 0 or r < 0:
        return 
    getInput("Enter New Value")
    
    if not item:
        return
    #Updating the Database
    sql = f"UPDATE {Tablename} SET {c_name} = \"{item}\" WHERE Time = \"{r_name}\" "
    runCMD(sql)
    #Removing current table and displaying Updated one
    root.destroy()
    displayTable(Tablename)





