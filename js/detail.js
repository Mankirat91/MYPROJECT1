function getProductFullImage(){

}

function getProductDetail(){
   var currentUrl= getFullUrl();
   var url= new URL(currentUrl)
   var params= new URLSearchParams(url.search);
   var productId=params.get("id");
  var product= getProductById(productId)
  getProduct(product);


function getProduct(_product){
    var html ="";
    var productContainer= document.createElement('div');
    productContainer.id='feature-product';
    productContainer.className='row g-4';
    getProductImage(clickedProduct);
  

}
 function getProductImage(_clickedProduct){
    var productImg= document.createElement('div');
    var anchorImg= document.createElement('a');
    anchorImg.href=`/shop-detail?id=${product.id}`
    anchorImg.setAttribute('onclick',`routeTo('/shop-detail?id=${product.id}')`)
    productImg.className= 'product-thumb-img';
    var containerProductImg =document.createElement('img');
    containerProductImg.className ="img-fluid w-100 rounded-top";
    containerProductImg.src =product.thumbnailImage;
    anchorImg.append(containerProductImg);
    productImg.append(anchorImg);
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
}