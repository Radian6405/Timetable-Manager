import mysql.connector as con

def DB_init(Password):
    #Initialising connector
    global mycon
    global mycursor
    mycon = con.connect(host="localhost",user="root",passwd=Password)
    mycursor = mycon.cursor()
    
    #Initialising database
    DBname = "Timetables"
    mycursor.execute(f"CREATE DATABASE if not exists {DBname}")
    mycursor.execute(f"USE {DBname}")

    #Creating a default table
    DefaultTable = "Table1"
    ifTableExists(DefaultTable)
    if not ifTableExists(DefaultTable):
        createTable(DefaultTable)
def runCMD(command):
    mycursor.execute(command)
    mycon.commit()
    
def ifTableExists(TableName):
    #Getting list of tables
    Tables = getTableList()

    #Checking for specified 
    if TableName.lower() in Tables:
        return True
    else:
        return False

def getTableList():
    Tables = []

    #Getting list of tables from sql commands
    sql = "SHOW TABLES"
    mycursor.execute(sql)
    TablesList = mycursor.fetchall()

    for i in TablesList:
        Tables.append(i[0])
    return Tables
    
def createTable(Tablename):
    #Creating columns
    Clms = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    sql = f"CREATE TABLE {Tablename}(Time VARCHAR(255)"
    for i in Clms:
        sql = sql + "," + str(i) + " VARCHAR(255)"  
    sql = sql + ")"
    mycursor.execute(sql)

    #Creating Rows
    Rows = ["8 AM","9 AM","10 AM","11 AM","12 PM","1 PM","2 PM","3 PM","4 PM","5 PM"]

    for Time in Rows:
        sql = f"INSERT INTO {Tablename} VALUES(\"{Time}\""+(",NULL"*len(Clms)) + ")"   
        mycursor.execute(sql)
        mycon.commit()

def getTableData(Tablename):
    #List of rows
    sql = (f"SELECT * FROM {Tablename}")
    mycursor.execute(sql)
    rows_data = mycursor.fetchall()
    row_count = len(rows_data)

    #List of clms
    sql = (f"DESC {Tablename}")
    mycursor.execute(sql)
    clmslist = mycursor.fetchall()
    clms = []
    
    for i in clmslist:
        clms.append(i[0])
    clm_count = len(clms)

    return rows_data,clms,row_count,clm_count
