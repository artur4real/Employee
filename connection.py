import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="777")

def get_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM post join employee on post.id_post= employee.id_post")
    res = cursor.fetchall()
    print(res)
    return res
