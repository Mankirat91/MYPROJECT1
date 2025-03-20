import pymysql.cursors

from helper import encrypt,decrypt

def getConnection(host,user,password,database):
    try:
        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database=database,
                                     cursorclass=pymysql.cursors.DictCursor)
        print("Database connected successfully")
        return connection
    # with connection:
    #     with connection.cursor() as cursor:
    #         return cursor
    #     connection.commit()
    #     with connection.cursor() as cursor:
        # Read a single record
            # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            # cursor.execute(sql, ('inder@gmail.com'))
            # result = cursor.fetchone()
            # print(decrypt(result['password'],"password"))

    except Exception as e:
        print(e)


    #class in python (encapulation , inheritance,datahiding,objects,constructors )


def dbQuery(query):
    connection=getConnection()
    with connection:
         with connection.cursor() as cursor:
            return cursor
         connection.commit()
         with connection.cursor() as cursor:
            # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
             cursor.execute(query)
             result = cursor.fetchone()
             