function confirmOrder(cart, customer,shipping){
	console.log('User is authenticated, sending data...')

		var url = '/check_out/process_order/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'cart':cart, 'customer':customer,'shipping':shipping})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
			console.log(data)
			localStorage.clear()
		    location.replace('/check_out/thankyou/'+data['order_id'])
		});
}


$( document ).ready(function() {

	var html = ""
	    html += "<tr>";
        html += "<th>Name</th>";
        html += "<th>Price</th>";
        html += "<th>Quantity</th>";
        html += "<th>Total</th>";
        html += "</tr>";
	for (product in cart ) {
	    html += "<tr>";
		html += "<td>"+ cart[product].name+"</td>";
		html += "<td>"+ cart[product].price+"</td>";
		html += "<td>"+ cart[product].quantity+"</td>";
		html += "<td><span id='total-amount'> "+productTotal(product)+"</span></td>";
		html += "<br/>";
		html += "</tr>";
	}


	$('#display-checkout').html(html)

    function productTotal(item){
        var sum = 0;
            sum += cart[item].quantity * cart[item].price
        return parseFloat(sum).toFixed(2);
    }

    function calculate_total(){
        var sum = 0;
        for (item in cart){
            sum += cart[item].quantity * cart[item].price
        }
        return parseFloat(sum).toFixed(2);
    }


    $('#cart-total').html(calculate_total(JSON.parse(localStorage.getItem('cart'))));

    $('#confirm-order').click(function(){
        console.log(($('#id_name').val()))
        console.log(($('#id_email').val()))
    })

    $('#checkout').submit(function(e){
		e.preventDefault()
		customer = {
			"name":$('#id_name').val(),
			"email":$('#id_email').val()
		}
		shipping = {
				"address":$('#id_address').val(),
				"city":$('#id_city').val(),
				"state":$('#id_state').val(),
				"zipcode":$('#id_zipcode').val()
		}
		console.log(cart)
		confirmOrder(cart,customer,shipping);
	})

});