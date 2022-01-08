//var updateBtns = document.getElementsByClassName('add-to-cart')
//
//for (i = 0; i < updateBtns.length; i++) {
//    updateBtns[i].addEventListener('click', function(){
//
//        var productId = this.dataset.product
//        var action = this.dataset.action
//        console.log('USER:', user)
//
//        if (user == 'AnonymousUser'){
//            addCookieItem(productId, action)
//        }else{
//            updateUserOrder(productId, action)
//        }
//    })
//}
//
//function updateUserOrder(productId, action){
//    console.log("User is authenticated...sending data")
//    var url = '/update_item/'
//    fetch(url,{
//        method:'POST',
//        headers:{
//            'Content-Type':'application/json',
//            'X-CSRFToken':csrftoken,
//        },
//        body:JSON.stringify({'productId':productId,'action':action})
//    })
//    .then((data)=>{
//        location.reload()
//    });
//}
//
//function addCookieItem(productId, action){
//    console.log("User is not authenticated")
//}

console.log('working')
if(localStorage.getItem('cart') == null)
{
	var cart={};
}
else{
	cart= JSON.parse(localStorage.getItem('cart'));
}

$( document ).ready(function() {

    function cartLength(obj) {
        var count = 0;
        for ( var key in obj){
            count += obj[key].quantity
        }
        return count;
    }

    function cartTotal(obj) {
        var count = 0;
        for ( var key in obj){
            count += obj[key].total
        }
        return count;
    }

    //javascript
    // document.getElementById("cart-items").innerHTML = cartLength(JSON.parse(localStorage.getItem('cart')));
    // jquery
    $('#cart-items').html(cartLength(JSON.parse(localStorage.getItem('cart'))));
    $('#cart-total').html(cartTotal(JSON.parse(localStorage.getItem('cart'))));
    // jquery
    $('.add-to-cart').click(function(){
		console.log(this.dataset.pk);
        var idstr= this.dataset.pk.toString();
		// the cart attributes(quantity) is being updated
        if(cart[idstr]!= undefined) {

			quantity = cart[idstr].quantity
			price = cart[idstr].price
            cart[idstr].quantity =  quantity + 1;
            total =  cart[idstr].quantity * parseFloat(price);
            cart[idstr].total =  parseFloat(total);
        }
        else {
			// cart being inititlzied
            cart[idstr] = {quantity: 1, pk: this.dataset.pk, name: this.dataset.name,price: this.dataset.price,category: this.dataset.category,image:this.dataset.image, total:parseFloat(this.dataset.price)};
        }

        console.log(cart)
        localStorage.setItem('cart', JSON.stringify(cart));
        $('#cart-items').html(cartLength(cart));
        $('#cart-total').html(cartTotal(cart));
    });
});