import pymysql.cursors

def getConnection(host, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Database connected successfully")

        with connection.cursor() as cursor:
            sql=("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    age INT,
                    city VARCHAR(255)
                )
            """)
            cursor.execute(sql)
            print("Table 'customers' created successfully")
        connection.commit()

        # with connection.cursor() as cursor:
        #     sql = "INSERT INTO customers (name,city) VALUE (%s,%s)"
        #     values = ("rajesh","Amritsar")
        #     cursor.execute(sql,values)
        #     connection.commit()
        #     print(cursor.rowcount)

        # with connection.cursor() as cursor:
        #     sql = "SELECT name,city FROM customers"
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
        #     for x in result:
        #         print(x)

        # with connection.cursor() as cursor:
        #     sql ="SELECT * FROM customers WHERE city LIKE '%AM%'"
        #     cursor.execute(sql)
        #     result = cursor.fetchall()
        #     for x in result:
        #         print(x)

        with connection.cursor() as cursor: 
            sql = "SELECT * FROM customers ORDER BY name DESC"
            cursor.execute(sql)
            result = cursor.fetchall()
            for x in result:
                print(x)

        with connection.cursor() as cursor:
            sql ="SELECT MAX(salary)            "
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            
        return connection

        

    except pymysql.MySQLError as e:
        print("Error:", e)
        return None

# Usage
conn = getConnection("localhost", "root", "Mankirat@91", "mydatabase")
if conn:
    conn.close()
