def getAllQuery(connect,query):
    try:
        with connect:
             with connect.cursor() as cursor:
                 cursor.execute(query)
                 result = cursor.fetchall()
                 return result
    except Exception as e:
        print(e)


def getOneQuery(connect,query):
    try:
        with connect:
             with connect.cursor() as cursor:
                 cursor.execute(query)
                 result = cursor.fetchone()
                 print()
                 return result
    except Exception as e:
        print(e)

    


def executeQuery(connect,query):
    try:
        with connect:
             with connect.cursor() as cursor:
                 cursor.execute(query)
                 result = cursor.commit()
                 return result
    except Exception as e:
        print(e)

