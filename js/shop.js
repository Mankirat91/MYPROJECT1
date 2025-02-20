

var filter =[{name:"price",value:1000,type:"order"},{ name:"sort",value:"asc",type:"price"},{ name:"cat",value:null,type:"find"}];
var products =[];

function getListProducts(){
  var html='';
  var productContainer= document.getElementById('product-list');
    if(products.length == 0){
      html += '<h3>No Products</h3>'
      productContainer.innerHTML=html;
      return productContainer;
    }
    else{
        products.forEach(product=>{
        var productItem= getFeaturedProduct(product)
        html += productItem.innerHTML;
      })
      productContainer.innerHTML=html
      return productContainer;
    }
  }

  function getShopCategories(){
    var catContainer=  document.getElementById('shop-categories');
   var catData= getCategoriesData();
   catData.forEach(cat=>{
    var listItem= document.createElement('li');
    var divItem= document.createElement('div');
    var anchorItem= document.createElement('a');
    var spanItem= document.createElement('span');
    var iItem= document.createElement('i');
    divItem.className="d-flex justify-content-between fruite-name";
    iItem.className="fas fa-apple-alt me-2"
    anchorItem.id="cat-anchor";
    anchorItem.setAttribute("catid",cat.id);
    var count= getProductsCountByCategory(cat.id);
    spanItem.innerText=`(${count})`
    listItem.append(divItem)
    divItem.append(anchorItem)
    anchorItem.append(iItem)
    anchorItem.append(cat.name)
    divItem.append(spanItem)
    catContainer.append(listItem)
   })
  }

  function filterProductsByPrice(){
    var rangeInput=document.querySelector('#rangeInput');
    rangeInput.value=filter.find(fil=>fil.name=="price").value;
    document.getElementById('amount').innerText=filter.find(fil=>fil.name=="price").value
    rangeInput.addEventListener('change',function(){
      var rangeValue=  document.getElementById('amount').innerText;
      for(var i=0;i<filter.length;i++){
        filter[i].value=rangeValue;
      }
      products= getProductsDataByFilter(filter);
      getListProducts();
    })
    products= getProductsDataByFilter(filter);
    getListProducts();
  }

  function sortProductByPrice(){
    var sortFilter=document.querySelector('#sort-price');
    sortFilter.addEventListener('change',()=>{
      var sortValue=document.getElementById('sort-price').value;
      for(var i=0;i<filter.length;i++){
        if(filter[i].name=="sort")
         filter[i].value=sortValue;
      }
      products= getProductsDataByFilter(filter);
      getListProducts();
    })
  }


  function sortProductByName(){
    var sortFilter=document.querySelector('#sort-name');
    sortFilter.addEventListener('change',()=>{
      var sortValue=document.getElementById('sort-name').value;
      for(var i=0;i<filter.length;i++){
        if(filter[i].name=="sort")
         filter[i].value=sortValue;
      }
      products= getProductsDataByFilter(filter);
      getListProducts();
    })
  }



  function filterProductByCategory(){
    var catQuery=document.querySelectorAll('#cat-anchor');
    catQuery.forEach(catQu=>{
      catQu.addEventListener('click',(e)=>{
        e.preventDefault();
        var cat= catQu.getAttribute('catid');
        catQu.className="active";
        for(var i=0;i<filter.length;i++){
          if(filter[i].name=="cat")
            filter[i].value=cat;
        }
        products= getProductsDataByFilter(filter);
        getListProducts();
      })
    })

  }
