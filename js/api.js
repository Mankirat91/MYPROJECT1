function getCurrentUrl(){
    return window.location.pathname;
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
    data=getProductsDataByCategory(catItem.value)
  }
  return data;
}
function getSortDataAsc(param,data){
  return data.sort((a,b)=> a[param] - b[param]);
}

function getSortDataDec(param,data){
  return data.sort((a,b)=> b[param] - a[param]);
}

function getProductsCountByCategory(catid){
  var data= getProductsDataByCategory(catid);
  return data.length;
}
  
function getProductsDataByCategory(catid){
   var products= getProductsData();
   return products.filter(product=>product.categoryId == catid)
}
  