
$('.plus-cart').click(function() {const id = $(this).attr("pid").toString();
    const eml = this.parentNode.children[2];
    console.log( 'pid=', id)
        $.ajax({
            type: "GET",
            url: "/pluscart/",
            data: {
                prod_id: id
            },
            success: function(data) {
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
            }
        });
    });

    $('.minus-cart').click(function() {
        const id = $(this).attr("pid").toString();
        const eml = this.parentNode.children[2];
        $.ajax({
            type: "GET",
            url: "/minuscart/",
            data: {
                prod_id: id
            },
            success: function(data) {
                eml.innerText = data.quantity;
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
            }
        });
    });

   $('.remove-cart').click(function() {
    console.log('butto click')
        const id = $(this).attr("pid").toString();
        const eml = this;
        $.ajax({
            type: "GET",
            url: "/removecart/",
            data: {
                prod_id: id
            },
            success: function(data) {
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
                eml.parentNode.parentNode.parentNode.parentNode.remove();
            }
        });
    });

    $('.plus-wishlist').click(function() {
        const id = $(this).attr("pid").toString();
        $.ajax({
            type: "GET",
            url: "/pluswishlist",
            data: {
                prod_id: id
            },
            success: function(data) {
                window.location.href = `http://localhost:8000/ProductDetail/${id}`;
            }
        });
    });

    $('.minus-wishlist').click(function() {
        const id = $(this).attr("pid").toString();
        $.ajax({
            type: "GET",
            url: "/minuswishlist",
            data: {
                prod_id: id
            },
            success: function(data) {
                window.location.href = `http://localhost:8000/ProductDetail/${id}`;
            }
        });
    });

