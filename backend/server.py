# server 
# php javascript python(Popular) java
# database: mySql(Ecommerce) ,Posgresql , Mongodb ,Graphql,Redis
# Python is a server side programming langauage . It works in threads 

a = 65
b = 69
# if a > b:
#     print("Greater")
# elif b > a:
#     print("Shorter")
# else:
#     print("Invalid")

# c = [{ "name":"Brinjal" ,"qty":5,"desc":"ge","price":8},{ "name":"Brinjal" ,"qty":5,"desc":"ge","price":8}]
# print(c[0]['name'])
# d= [ 4,5,10,11]

# for i in c:
#     print(i['name'])


#functions

def getProducts():
    c = [{ "id":1,"name":"Brinjal" ,"qty":5,"desc":"ge","price":8},{"id":2, "name":"Brinjal" ,"qty":5,"desc":"ge","price":8}]
    return c

def getProductById(id):
    products = getProducts()
    for i in products:
        if i['id'] == id:
            return i
        # else:
        #     print("No Product")

#numpy panda opencv tessract