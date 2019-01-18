import sqlite3
import csv
import pandas as pd
import glob
    

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def insert_into_the_db(conn,data):
    cur = conn.cursor()
    #cur.execute("INSERT INTO tbl_chatData VALUES (2,'Gaurav',28)")
    #cur.execute("Select * from chatData")
    for row in data.items():
        cur.execute("INSERT INTO chatData (Questions, Answers) VALUES (?, ?)",
            (row[0], row[1]))
    
    cur.execute("SELECT * FROM chatData")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)


def main():
    #database = "/home/anurag/Documents/chattest"
    #fileLoc = "/home/anurag/Documents/ArtificialIntelligence.csv"
    #conn = create_connection(database)
    #print(conn)
    preData = preprocess('./english/*.yml')
    #with conn:
    #    print("1. Query task by priority:")
    #    insert_into_the_db(conn,preData)
        
def preprocess(folder):
    chatData=[]
    for filepath in glob.iglob(folder):
        d = {}
        with open(filepath, "r") as f:
           text=f.read()
        lines=text.split("\n")
        cat = lines[1][2:]
        nodash = 0
        while nodash < 2:
		    if lines[0][0] != "-":
			    nodash +=1
		    lines.remove(lines[0])
        answer = []
        question=0
        for line in lines:
            if line =='':
				continue
            if line[0]=="-":
                if question==line[4:].lower():
                    continue
                question=line[4:].lower()
                d[question] = []
            if line[0]==" ":
                d[question].append(line[4:])
        fileData=[cat,d]
        chatData.append(fileData)
    #print(chatData)[:2]
    return chatData
    
if __name__ == '__main__':
    main()
