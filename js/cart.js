
function cartAction(){
    var cartActionBtns=document.querySelectorAll('.cart-btn');
    cartActionBtns.forEach(cartAction=>{
      cartAction.addEventListener('click',function(e){
        e.preventDefault();
        var productId=this.getAttribute('product-id');
        var cartValue=   document.getElementById('shopping-bag').innerText;
        cartValue++;
        document.getElementById('shopping-bag').innerText=cartValue;
        setLocalData('cartCount',cartValue);
      });
    })
  }


function getCartCount(){
    document.getElementById('shopping-bag').innerText=getLocalData('cartCount') || 0;
}
