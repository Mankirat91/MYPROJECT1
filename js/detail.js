function getProductFullImage(){

}

function getProductDetail(){
   var currentUrl= getFullUrl();
   var url= new URL(currentUrl)
   var params= new URLSearchParams(url.search);
   var productId=params.get("id");
  var product= getProductById(productId)
  getProduct(product);
}

function getProduct(product){
   

}