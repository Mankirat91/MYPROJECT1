import pymysql.cursors
from helper import encrypt,decrypt
# Connect to the database


try:
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='inder123',
                             database='fruitable',
                             cursorclass=pymysql.cursors.DictCursor)
    with connection:
        with connection.cursor() as cursor:
        # Create a new record
            sql = "INSERT INTO `userss` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('inder@gmail.com', encrypt("inder1234","password")))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
        connection.commit()

        with connection.cursor() as cursor:
        # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('inder@gmail.com'))
            result = cursor.fetchone()
            print(decrypt(result['password'],"password"))

except Exception as e:
    print(e)


    #class in python (encapulation , inheritance,datahiding,objects,constructors )