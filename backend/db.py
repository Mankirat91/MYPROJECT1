import pymysql.cursors
#from helper import encrypt,decrypt

def getConnection(host,user,password,database):
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database,
                                     cursorclass=pymysql.cursors.DictCursor)
        print("Database connected successfully")
        return connection
    except Exception as e:
        print(e)


def dbQuery(query,connect):
    try:
        with connect:
             with connect.cursor() as cursor:
                 cursor.execute(query)
                 result = cursor.fetchone()
                 return result
    except Exception as e:
        print(e)


