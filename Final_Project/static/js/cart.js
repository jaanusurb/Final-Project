var updateBtns = document.getElementsByClassName('add-to-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){

        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            addCookieItem(productId, action)
        }else{
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log("User is authenticated...sending data")
    var url = '/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((data)=>{
        location.reload()
    });
}

function addCookieItem(productId, action){
    console.log("User is not authenticated")
}