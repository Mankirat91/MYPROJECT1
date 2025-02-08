function urlRequest(path){
  var req = new XMLHttpRequest();
  req.open('GET',path,false);
  req.send(null);
  return req.responseText;
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

function include(path,tempName){
    var obj=urlRequest(path)
    document.getElementById(`${tempName}-container`).innerHTML=obj;
}


function getMenuItems(){
 var items= document.getElementById('nav-items');
 var navItems=getNavData();
 for(var i=0;i<navItems.length;i++){
    var anchor =document.createElement('a'); // <a> </a>
    var  path =getCurrentUrl();
    anchor.href=navItems[i].link;
    if(navItems[i].link == path){
        var classList=navItems[i].class;
        classList += ' active';
    }
    else{
        var classList=navItems[i].class;
    }
    anchor.setAttribute('onclick','route()');
    anchor.className=classList;
    anchor.innerText=navItems[i].name
    items.append(anchor);
 }
}

function getCurrentUrl(){
 return window.location.pathname;
}

function getHeaderSlider(){
  var carousel= document.getElementById('carousel-slider');
  var categories =getCategoriesData();
  for(var i=0;i<categories.length;i++){
    var slideContainer =document.createElement('div');
    var slideImage =   document.createElement('img');
    var slideAnchor =  document.createElement('a');
    if(i==0){
        slideContainer.className ='carousel-item active rounded';
    }
    else{
        slideContainer.className ='carousel-item rounded';
    }
    
    slideImage.src =categories[i].img;
    slideImage.className ='img-fluid w-100 h-100 bg-secondary rounded';
    slideAnchor.href="javascript:void(0);";
    slideAnchor.className="btn px-4 py-2 text-white rounded";
    slideAnchor.innerText=categories[i].name;
    
    slideContainer.append(slideImage, slideAnchor);
    carousel.append(slideContainer);
   }

}

function getFeaturedCategories(){
    var catItems= document.getElementById('cat-items');
    var categories =getCategoriesData();
     for(var i=0;i<categories.length;i++){
      var containerCat =document.createElement('li');
      var anchorCat =   document.createElement('a');
      var spanCat =  document.createElement('span');
       containerCat.className ='nav-item';
      if(i == 0){
        anchorCat.className ='d-flex m-2 py-2 bg-light rounded-pill active';
      }
      else{
        anchorCat.className ='d-flex m-2 py-2 bg-light rounded-pill';
      }
       anchorCat.href=`#tab-${categories[i].id}`;
       anchorCat.setAttribute('data-bs-toggle','pill');
       spanCat.className ='text-dark';
       spanCat.style.width ='130px';
       spanCat.innerText=categories[i].name;
       anchorCat.append(spanCat);
       containerCat.append(anchorCat);
       catItems.append(containerCat);
      }
  }

  function getFeaturedProduct(product){
    var categories =getCategoriesData();
    var productItem= document.createElement('div');
    var productInnerContainer= document.createElement('div');
    var productCatContainer= document.createElement('div');
    var productNameContainer= document.createElement('div');
    var productPriceContainer= document.createElement('div');
    var productCartContainer= document.createElement('div');
    var productCartAction= document.createElement('a');
    var productCartIcon= document.createElement('i');

    productCatContainer.className="text-white bg-secondary px-3 py-1 rounded position-absolute";
    productCatContainer.id= 'product-category-name';
    productCatContainer.style.top="10px";
    productCatContainer.style.left="10px";

    var catObj=categories.find(cat=> cat.id == product.categoryId) ;
    productCatContainer.innerText=catObj.name;
   
    productInnerContainer.className ='rounded position-relative fruite-item';
    productItem.className= 'col-md-6 col-lg-4 col-xl-3';
    productItem.id='product-item';

    productNameContainer.className="p-4 border border-secondary border-top-0 rounded-bottom";

    productPriceContainer.className="text-dark fs-5 fw-bold mb-0";
    productPriceContainer.id="price-container";
  
    productCartAction.className="btn border border-secondary rounded-pill px-3 text-primary"
    productCartIcon.className="fa fa-shopping-bag me-2 text-primary";
    productCartIcon.setAttribute('onclick',`addToCart(${product.id})`);
    productCartIcon.innerText="Add to cart"

    productCartContainer.className="d-flex justify-content-between flex-lg-wrap";
    
    var img=getFeatureProductImage(product);
    var name= getFeatureProductName(product);
    var desc= getFeatureProductShortDescription(product);
    var price= getFeatureProductPrice(product);
    
    productCartAction.append(productCartIcon);
    productPriceContainer.append(price);
    productNameContainer.append(name);
    productNameContainer.append(desc);
    productItem.append(productInnerContainer);
    productInnerContainer.append(img);
    productInnerContainer.append(productCatContainer);
    productInnerContainer.append(productNameContainer);
    productNameContainer.append(productCartContainer)
    productCartContainer.append(productPriceContainer)
    productCartContainer.append(productCartAction);
    return productItem;
  }

function getFeaturedProducts(){
  var productContainer= document.getElementById('feature-product-container');
  var products=getProductsData();
  console.log(products)
    products.forEach(product=>{
      var productItem= getFeaturedProduct(product)
      productContainer.append(productItem);
    })
  }
  
function getFeatureProductImage(product){
  var productImg= document.createElement('div');
  productImg.className= 'product-thumb-img';
  var containerProductImg =document.createElement('img');
  containerProductImg.className ="img-fluid w-100 rounded-top";
  containerProductImg.src =product.thumbnailImage;
  productImg.append(containerProductImg);
  return productImg;
}

function getFeatureProductName(product){
  var productName= document.createElement('h4');
  productName.innerText=product.name;
  return productName;
}

function getFeatureProductPrice(product){
  var productPrice=document.createElement('p');
  productPrice.innerText=`$ ${product.price}/kg`
  return productPrice;
}
function getFeatureProductShortDescription(product){
  var productDec= document.createElement('p');
  product.id="short-description"
  productDec.innerText=product.shortDescription
  return productDec;
}

//Events

function addToCart(id){
console.log(id);
}

// GET DATA


include('/template/partial/header.html','header');
include('/template/partial/header.html','footer');
include('/template/partial/navbar.html','navbar');
getCategoriesData();
getMenuItems();
getCurrentUrl();
getHeaderSlider();
getFeaturedCategories();
getFeaturedProducts();

