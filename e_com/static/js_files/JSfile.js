//Toggling the search wrapper area after icon is clicked

$( document ).ready(function() {
	$('[data-toggle=search-form]').click(function() {
	    $('.search-form-wrapper').toggleClass('open');
	    $('.search-form-wrapper .search').focus();
	    $('html').toggleClass('search-form-open');
	  });
	
	$('.search-close').click(function(event) {
	  $('.search-form-wrapper').removeClass('open');
	  $('html').removeClass('search-form-open');
	});
	});

//Scrolling Animation

var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos < currentScrollPos) {
 	document.getElementById("navbar").style.top = "-100px";
 	document.getElementById("navbar").style.transition = "all 0.5s";
  } else {
  	document.getElementById("navbar").style.top = "0px";
  }
  prevScrollpos = currentScrollPos;
}

//Owl-carousel scrolling animation

$(document).ready(function(){
  
	$('.owl-carousel').owlCarousel({
		loop:true,
		margin:100,
		nav:true,
		autoPlay: 1000,
		responsive:{
			0:{
				items:1
			},
			600:{
				items:3
			},
			1000:{
				items:5
			}
		}
	})
	});



	var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)
		}else{
			updateUserOrder(productId, action)
		}
	})
}

function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}