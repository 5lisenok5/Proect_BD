import sqlite3
import os
import json

'''
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e:
        print(f"The error '{e}' occured")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
'''
#Путь к данныx
path = "C:\Users\aavur\AppData\Roaming\Opera Software\Opera Stable\History"

#Закладка
class BookMark:
    def __init__(self,chromePath = path):
        self.chromePath = chromePath
        with open(os.path.join(path,'Bookmarks'),encoding = 'utf-8') as f:
            bookmarks = json.loads(f.read())
        self.bookmarks = bookmarks
        self.folders = self.get_folders()
    
    def get_folders(self):
        names = [
            (i,self.bookmarks['roots'][i]['name'])
            for i in self.bookmarks['roots']
                  ]
        return names
    
    def get_folder_data(self,folder=0):
        return self.bookmarks['roots'][self.folders[folder][0]]['children']
    
    def set_chrome_path(self,chromePath):
        self.chromePath = chromePath

    #Обновление
    def refresh(self):
        with open(os.path.join(path,'Bookmarks'),encoding = 'utf-8') as f:
            bookmarks = json.loads(f.read())
        self.bookmarks = bookmarks

class History:
    def __init__(self,chromePath = path):
        self.chromePath = chromePath

    #Подключение
    def connect(self):
        self.conn = sqlite3.connect(os.path.join(self.chromePath,'History'))
        self.cousor = self.conn.cursor()

    #После пробега курсора закрыть
    def close(self):
        self.conn.close()

    #Вывод данных по ссылкам и количеству посещений
    def get_history(self):
        cursor = self.conn.execute('SELECT id,url,title,visit_count from urls')
        rows = []
        for _id,url,title,visit_count in cursor:
            row = {}
            row['id'] = _id
            row['url'] = url
            row['title'] = title
            row['visit_count'] = visit_count
            rows.append(row)
        return rows

#Проверка алгоритма
if __name__ == "__main__":
    book = BookMark(path)
    names = book.get_folders()
    print(names)
    items = book.get_folder_data(0)
    print(items[-1])
    book.refresh()
    book.set_chrome_path(path)

    history = History(path)
    items = history.get_history()
    print(items[-1])







