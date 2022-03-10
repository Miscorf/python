import pymysql
from time import strftime
import  datetime
class sqlforface:
    def insert_time_face(status='happy'):
        db = pymysql.connect("localhost", "root", "password", "face", charset='utf8')
        cursor = db.cursor()
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = """INSERT INTO 
                     face (time, status) values (%s, %s)"""
        value = [dt, status]
        cursor.execute(sql, value)
        db.commit()
        db.close()
if __name__ =='__main__':
    sqlforface.insert_time_face('happy')