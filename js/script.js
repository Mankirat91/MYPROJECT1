
var navItems = [{name:"home",link:"/",class:"nav-item nav-link"},{ name:"shop",link:"/shop.html",class:"nav-item nav-link"},{name:"shop-detail",link:"/shop-detail.html",class:"nav-item nav-link"}];
var categories = [{id:1,name:"Vegetables",link:"/vegetables",img:"/img/cat/vegetable.png"},{id:2,name:"Fruits",link:"/fruit",img:"/img/cat/fruit.png"},{id:3,name:"Bread",link:"/bread",img:"/img/cat/bread1.png"},{id:4,name:"Meat",link:"/meat",img:"/img/cat/meat1.png"}];
// var products = [{name:"home",link:"/",class:"nav-item nav-link"},{ name:"shop",link:"/shop.html",class:"nav-item nav-link"},{name:"shop-detail",link:"/shop-detail.html",class:"nav-item nav-link"}];


function include(path,tempName){
    var req = new XMLHttpRequest();
    req.open('GET',path,false);
    req.send(null);
    document.getElementById(`${tempName}-container`).innerHTML=req.responseText;
  }
  include('/partial/header.html','header');
  include('/partial/navbar.html','navbar');
  include('/partial/footer.html','footer');
  


function getMenuItems(){
 var items= document.getElementById('nav-items');
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
    anchor.className=classList;
    anchor.innerText=navItems[i].name
    items.append(anchor);
 }
}

function getCurrentUrl(){
    console.log(window.location)
 return window.location.pathname;
}

function getHeaderSlider(){
  var carousel= document.getElementById('carousel-slider');
  console.log(categories);
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

getMenuItems();
getCurrentUrl();
getHeaderSlider();
getFeaturedCategories();



{/* <li class="nav-item">
<a class="d-flex m-2 py-2 bg-light rounded-pill active" data-bs-toggle="pill" href="#tab-1">
    <span class="text-dark" style="width: 130px;">All Products</span>
</a>
</li>
<li class="nav-item">
<a class="d-flex py-2 m-2 bg-light rounded-pill" data-bs-toggle="pill" href="#tab-2">
    <span class="text-dark" style="width: 130px;">Vegetables</span>
</a>
</li>
<li class="nav-item">
<a class="d-flex m-2 py-2 bg-light rounded-pill" data-bs-toggle="pill" href="#tab-3">
    <span class="text-dark" style="width: 130px;">Fruits</span>
</a>
</li>
<li class="nav-item">
<a class="d-flex m-2 py-2 bg-light rounded-pill" data-bs-toggle="pill" href="#tab-4">
    <span class="text-dark" style="width: 130px;">Bread</span>
</a>
</li>
<li class="nav-item">
<a class="d-flex m-2 py-2 bg-light rounded-pill" data-bs-toggle="pill" href="#tab-5">
    <span class="text-dark" style="width: 130px;">Meat</span>
</a>
</li> */}