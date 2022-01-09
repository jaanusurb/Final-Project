$( document ).ready(function() {

	var html = ""
	    html += "<tr>";
        html += "<th>PK</th>";
        html += "<th>Image</th>";
        html += "<th>Name</th>";
        html += "<th>Price</th>";
        html += "<th>Category</th>";
        html += "<th>Quantity</th>";
        html += "<th>Total</th>";
        html += "<th>Delete</th>";
        html += "</tr>";
	for (product in cart ) {
	    html += "<tr>";
		html += "<td>"+ cart[product].pk+"</td>";
		html += "<td><img src="+ cart[product].image+" width=50 height=50 class='product'  alt='My image'></td>"
		html += "<td>"+ cart[product].name+"</td>";
		html += "<td>"+ cart[product].price+"</td>";
		html += "<td>"+ cart[product].category+"</td>";
		html += "<td>"+ cart[product].quantity+"</td>";
		html += "<td><span id='total-amount'> "+productTotal(product)+"</span></td>";
        html += "<td><button class='btn remove-from-cart' data-id='"+product+"'><i class='fa fa-trash'></i></button></td>"
		html += "<br/>";
		html += "</tr>";
	}
    html += "<tr><td colspan='5'></td><td> <b>Grand Total:</b> <span id='total-amount'> "+calculate_total()+"</span></td></tr>"


	$('#display-cart').html(html)

    $('.remove-from-cart').click(function(){
        if(cart[this.dataset.id].quantity === 1){
            delete cart[this.dataset.id]
        }else{
            cart[this.dataset.id].quantity = cart[this.dataset.id].quantity - 1
        }
        localStorage.setItem('cart', JSON.stringify(cart));
        // reloads the page from cache, faster but not up to date
        // location.reload();
        // reloads the page from server, slower but always uptp date
        location.reload(true);
    });

    function calculate_total(){
        var sum = 0;
        for (item in cart){
            sum += cart[item].quantity * cart[item].price
        }
        return sum;
    }

    function productTotal(item){
        var sum = 0;
            sum += cart[item].quantity * cart[item].price
        return sum;
    }

    function cartTotal(obj) {
        var count = 0;
        for ( var key in obj){
            count += obj[key].total
        }
        return count;
    }

    $('#cart-total').html(cartTotal(JSON.parse(localStorage.getItem('cart'))));

});