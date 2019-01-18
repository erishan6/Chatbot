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
    with open('data_file.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        i = 3
        for item in data:
            category = item[0]
            qa = item[1]
            # print(category, qa)
            # print("********************************")
            for row in qa.items():
                answer = ""
                for x in row[1]:
                    answer += x + "|"
                answer = answer[:len(answer) - 1]
                data_writer.writerow([i,row[0],answer,category])
                i+=1

            # print(row[0], "********", answer)

            # cur.execute("INSERT INTO chatapp_chatinfo (question, answer, category) VALUES (?, ?,?)",(row[0], answer,category))



    # for row in data.items():
    #     cur.execute("INSERT INTO chatData (Questions, Answers) VALUES (?, ?)",
    #         (row[0], row[1]))
    #
    # cur.execute("SELECT * FROM chatData")
    # rows = cur.fetchall()
    #
    # for row in rows:
    #     print(row)


def main():
    database = "../djangoChatbot/Chatbot_TT/db.sqlite3"
    #fileLoc = "/home/anurag/Documents/ArtificialIntelligence.csv"
    conn = create_connection(database)
    #print(conn)
    preData = preprocess('./english/*.yml')
    #with conn:
    #    print("1. Query task by priority:")
    insert_into_the_db(conn,preData)
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
