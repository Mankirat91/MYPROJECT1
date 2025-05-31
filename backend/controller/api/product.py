from helper import getMessage,sendResponse,handle_bad_request
from services.query import getAllQueryWithCondition

def getProductsByCategory(category_id,cursor):
    try:
        data=getAllQueryWithCondition(cursor,'SELECT p.name,p.link, p.thumbnail_image,p.short_description,p.price,p.qty, c.name as category_name  from products p LEFT JOIN categories c ON  p.category_id = c.id WHERE  p.category_id = %s AND p.is_active = %s AND c.is_active = %s',(category_id,True,True))
        return sendResponse("",data)
    except Exception as e:
        print(e)
        return handle_bad_request(e)
    


def getProductsAll(cursor,filter):
    try:
        qry ='SELECT p.name,p.link, p.thumbnail_image,p.short_description,p.price,p.qty, c.name as category_name  from products p LEFT JOIN categories c ON  p.category_id = c.id WHERE  p.is_active = %s AND c.is_active = %s'
        values =(True,True)
      
        # filter.items()
        if "cat_id" in filter:
            qry += ' AND p.category_id = % s'
            values=(True,True,filter['cat_id'])
        if "price" in filter or "sort" in filter:
           opt =' ORDER BY'
        if "price" in filter and filter['price'] == 1:
            opt += ' p.price ASC'
        if "price" in filter and filter['price'] == 0:
            opt += ' p.price DESC'
        if "sort" in filter and filter['sort'] == 1:
            opt += ' p.name ASC'
        if "sort" in filter and filter['sort'] == 0:
            opt += ' p.name DESC'
        qry += opt
        data=getAllQueryWithCondition(cursor,qry,values)
        return sendResponse("",data)
    except Exception as e:
        print(e)
        return handle_bad_request(e)
    


    

    
