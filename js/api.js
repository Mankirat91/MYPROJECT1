function getGeolcation(){
  var obj=urlRequest('http://ip-api.com/json')
  var data= JSON.parse(obj);
  return data.country;
}
function getUsers(){
  var obj=urlRequest('/data/user.json')
  var data= JSON.parse(obj);
  return data;
}

function getUserByEmail(email){
  var data=getUsers()
  var email= data.find(dat=>dat.email == email)
  return email;
}

function getUserByPassword(password){
  var data=getUsers()
  var password= data.find(dat=>dat.password == password)
  return password;
}

function getCurrentUrl(){
    return window.location.pathname;
   }
   function getFullUrl(){
    return window.location.href;
   }
   
   function setLocalData(name,value){
     localStorage.setItem(name,value);
   }
   
   function getLocalData(name){
    return localStorage.getItem(name);
   }
   
function include(path,tempName){
    var obj=urlRequest(path)
    document.getElementById(`${tempName}-container`).innerHTML=obj;
}

function urlRequest(path){
    var req = new XMLHttpRequest();
    req.open('GET',path,false);
    req.send(null);
    return req.responseText;
  }

  function getTemplateData(){
    var obj=urlRequest('/data/templates.json')
    var data= JSON.parse(obj);
    return data;
  }

function getNavData(){
    var obj=urlRequest('/data/nav.json')
    var data= JSON.parse(obj);
    return data;
  }
  
  
function getCategoriesData(){
    var obj=urlRequest('/data/categories.json')
    var data= JSON.parse(obj);
    return data;
}
  
  
function getProductsData(){
    var obj=urlRequest('/data/products.json')
    var data= JSON.parse(obj);
    return data;
}

function getProductsDataByFilter(filter){
  var obj=urlRequest('/data/products.json')
  var data= JSON.parse(obj);
  var priceItem=filter.find(fil=>fil.name=="price");
  var sortItem=filter.find(fil=>fil.name=="sort");
  var catItem=filter.find(fil=>fil.name=="cat");
  if(priceItem){
    data= data.filter(dat=>dat.price < priceItem.value);
  }
  if(sortItem &&  sortItem.value == "asc"){
    data=getSortDataAsc(sortItem.type,data)
  }
  if(sortItem &&  sortItem.value == "dec"){
    data=getSortDataDec(sortItem.type,data)
  }
  if(catItem && catItem.type =='find' && catItem.value){
    data=getSortDataByCategory(catItem.value,data)
  }
  return data;
}
function getSortDataAsc(param,data){
  return data.sort((a,b)=> a[param] - b[param]);
}

function getSortDataDec(param,data){
  return data.sort((a,b)=> b[param] - a[param]);
}
function getSortDataByCategory(param,data){
  return data.filter(product=>product.categoryId == param)
}
function getProductsCountByCategory(catid){
  var data= getProductsDataByCategory(catid);
  return data.length;
}
  
function getProductsDataByCategory(catid){
   var products= getProductsData();
   return products.filter(product=>product.categoryId == catid)
}
  
function getProductById(productid){
  var products= getProductsData();
  return products.find(product=>product.id == productid)
}

function getCategoryById(catid){
  var categories= getCategoriesData();
  return categories.find(category=>category.id == catid)
}
 

function getShipping(){
  var obj=urlRequest('/data/shipping.json')
  var data= JSON.parse(obj);
  return data;
}
 


function getCoupons(){
  var obj=urlRequest('/data/coupon.json')
  var data= JSON.parse(obj);
  return data;
}


function getMessages(){
  var obj=urlRequest('/data/messages.json')
  var data= JSON.parse(obj);
  return data;
}



function getErrorContainer(text){
 var error=  document.createElement('div');
 error.id="error";
 error.innerHTML=text;
 return error;
}



function getSuccessContainer(text){
  var error=  document.createElement('div');
  error.id="success";
  error.innerHTML=text;
  return error;
 }
 
 function messageHandler(message,type){
  var messages= document.getElementById('messages');
  if(type == 'error') {
    var errorContainer= getErrorContainer(message)
    messages.innerHTML =errorContainer.outerHTML;
  } 
  else{
    var successContainer= getSuccessContainer(message)
    messages.innerHTML = successContainer.outerHTML;
  }
 }

 function checkCartItem(productId){
  var productsData=getLocalData('products');
  var products=productsData ? JSON.parse(productsData) : [];
  var product= products.find(product=>product.id == productId)
  if(product) return true;
   return false;
}
