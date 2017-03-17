<!DOCTYPE html>
  <head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="description" content="">
		<meta name="author" content="">
		<link rel="shortcut icon" href="img/favicon1.png" type="image/x-icon" />

		<title>Best Prix</title>
		<!-- Bootstrap core CSS -->
		<link href="css/bootstrap.min.css" rel="stylesheet">
		<!-- Custom styles for this template -->
		<link href="css/style.css" rel="stylesheet">

		<link rel="stylesheet" href="css/owl.carousel.css">
		<link rel="stylesheet" href="css/responsive.css">

		<!---------------- Start for Slider ---------->
		<script src="sss/ext.js"></script>
		<script src="sss/sss.min.js"></script>
		<link rel="stylesheet" href="sss/sss.css" type="text/css" media="all">
		<script>
		jQuery(function($) {
		$('.slider').sss();
		});
		</script>
		<!---------------- End for Slider

	   <script src="js/jquery.tabSlideOut.v1.3.js"></script>

		<script>
		$(function(){
             $('.slide-out-div').tabSlideOut({
                 tabHandle: '.handle',                              //class of the element that will be your tab
                 pathToTabImage: 'images/contact_tab.gif',          //path to the image for the tab (optionaly can be set using css)
                 imageHeight: '122px',                               //height of tab image
                 imageWidth: '40px',                               //width of tab image
                 tabLocation: 'left',                               //side of screen where tab lives, top, right, bottom, or left
                 speed: 300,                                        //speed of animation
                 action: 'click',                                   //options: 'click' or 'hover', action to trigger animation
                 topPos: '200px',                                   //position from the top
                 fixedPosition: false                               //options: true makes it stick(fixed position) on scroll
             });
         });
         </script>  ---------->


   <script type="text/javascript">
			<!--
			    function toggle_visibility(id) {
			       var e = document.getElementById(id);
			       if(e.style.display == 'block')
			          e.style.display = 'none';
			       else
			          e.style.display = 'block';
			    }
			//-->
		</script>


	<script>
	jQuery(document).ready(function(){
	jQuery(".menu-trigger").click(function() {
	jQuery(".nav-menu").slideToggle(400,function(){
	jQuery(this).toggleClass("nav-expanded").css('display','');
	});
	});
	});
	</script>



<script>

function suggest(inputString){
		if(inputString.length == 0 || inputString==" ") {
			$('#suggestions').fadeOut();
		} else {
		$('#listings').addClass('load');
			$.post("autosuggest.php", {queryString: ""+inputString+""}, function(data){
				if(data.length > 0) {
					$('#suggestions').fadeIn();
					$('#suggestionsList').html(data);
					$('#listings').removeClass('load');
				}
			});
		}
	}

	function fill(thisValue) {
		$('#listings').val(thisValue);
		setTimeout("$('#suggestions').fadeOut();", 100);
	}




</script>
</head>

<body>


		<div class="top-bar">

			<div class="row">
			<div class="col-lg-3">
			<h24>India's Largest Price Comparision Website</24>
			</div>

			<div class="col-lg-6 col-lg-push-5">
			<ul class="top-list">
            <li><a href="#">Wishlist</a></li>
            <li><a href="#">My Cart</a></li>
            <li><a href="#">Help Center</a></li>
            <li><a href="#">Sell On Bestprix</a></li>
			</ul>
			</div>
			</div>

		</div>


	<div class="navigation">

		<div class="row">
			<div class="col-lg-3">
				<div class="logo">
					<a href="index.php"><img src="img/bag.png" /></a>
				</div>
			</div>

			<div class="col-lg-6">
			<div class="search">
			<form id="form" action="search_results.php" method="POST" class="new-search">
			<div class="field" id="searchform">
			<input type="text" size="25" value="" placeholder="Search Products and brands"		name="search_term" id="listings" onkeyup="suggest(this.value);" class="" />
			<button type="submit" name="submit" value="submit" id="search">Search</button >
			<div class="suggestionsBox" id="suggestions" style="display: none;">
			<div class="suggestionList" id="suggestionsList"> &nbsp; </div>
			</div>
			</div>
			</form>
			</div> <!--end of search -->
			</div>

			<div class="col-lg-3">
			<!-- <div class="account">
			<div class="outer">
			<img src="images/users.png" class="outer-img" height="20">
			</div>
			<div class="outer-2">&nbsp;&nbsp;My Account&nbsp; <span3>▼</span3></div>
			<div class="account-content">
			<a href="construction.php" class="Login">Login</a><br><p class="acc-con">New User? <span5> Sign Up</span5></p>
			</div>
			</div> -->
			</div>

		</div><!-- end of row -->

	</div> <!-- end of navigation div -->


	<span class="menu-trigger">MENU</span>

<div class="container">
	<div class="nav-menu">
		<ul class="clearfix">
		<li class="active"><a class="list_link" href="construction.php">Home</a></li>
		<li><a class="list_link" href="construction.php">Mobiles</a></li>
		<li><a class="list_link" href="construction.php">Laptop & Computers</a></li>
		<li><a class="list_link" href="construction.php">Gym Equipment</a></li>
		<li><a class="list_link" href="construction.php">Watches</a></li>
		<li><a class="list_link" href="construction.php">Baby & Kids</a></li>
		<li><a class="list_link" href="construction.php">Personal & HealthCare</a></li>
		<li><a class="list_link" href="construction.php">New Deals</a></li>
		<li><a class="list_link" href="construction.php">Shoes</a></li>
		<li><a class="list_link" href="construction.php">Jewellery</a></li>
		<li><a class="list_link" href="construction.php">Offer Zone</a></li>
		</ul>
	</div>
</div>

    <!-- Page Content -->
    <div class="container">

        <div class="row">

			<div class="col-lg-9">
				<div class="slider">
					<img src="img/new/2.jpg" />
					<img src="img/new/3.jpg" />
					<img src="img/new/1.jpg" />
				</div>

			</div>

			<div class="col-lg-3">
				<div class="long-box">


				</div>
			</div>

		</div>

</div><!-- End Of Main Container -->

 <div class="container">
<div class="row">


<div class="col-lg-9">

	<div class="product-view-1">
	<div class="title-box">
	<h12>New Products</h12>
	</div>

	<div class="latest-product">
			<div class="product-carousel">

				<div class="single-product">
					<div class="product-f-image">
						<img src="img/shoes/1.jpg" alt="">
						<div class="product-hover">

							<a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
						</div>
					</div>
					<h2><a id="prod-name" href="single-product.html">Nike Tech Shoes</a></h2>
					<div class="product-carousel-price">
						<ins>₹14000</ins>
					</div>
				</div>

				<div class="single-product">
				<div class="product-f-image">
					<img src="img/shoes/2.jpg" alt="">
					<div class="product-hover">

						<a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> View Product</a>
					</div>
				</div>
               <h2><a id="prod-name" href="single-product.html">Nike Air Shoes</a></h2>
				<div class="product-carousel-price">
					<ins>₹10000</ins>
				</div>
                </div>

				<div class="single-product">
				<div class="product-f-image">
					<img src="img/shoes/3.jpg" alt="">
					<div class="product-hover">
						<a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
						<a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
					</div>
				</div>
				<h2><a id="prod-name" href="single-product.html">Vector Air Max</a></h2>
				<div class="product-carousel-price">
						<ins>₹7000.00</ins>
					</div>
				</div>

				<div class="single-product">
					<div class="product-f-image">
						<img src="img/shoes/1.jpg" alt="">
						<div class="product-hover">
							<a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
							<a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
						</div>
					</div>
					<h2><a id="prod-name" href="single-product.html">Nike Tech Shoes</a></h2>
					<div class="product-carousel-price">
						<ins>₹14000</ins>
					</div>
				</div>

				<div class="single-product">
				<div class="product-f-image">
					<img src="img/shoes/2.jpg" alt="">
					<div class="product-hover">
						<a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
						<a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
					</div>
				</div>
			   <h2><a id="prod-name" href="single-product.html">Nike Air Shoes</a></h2>
				<div class="product-carousel-price">
					<ins>₹10000</ins>
				</div>
				</div>

				<div class="single-product">
				<div class="product-f-image">
					<img src="img/shoes/3.jpg" alt="">
					<div class="product-hover">
						<a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
						<a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
					</div>
				</div>
				<h2><a id="prod-name" href="single-product.html">Vector Air Max</a></h2>
				<div class="product-carousel-price">
						<ins>₹7000.00</ins>
					</div>
				</div>




            </div>
        </div>
   </div>		<!-- end of product-view-1  -->


			<div class="product-view-1">
				<div class="title-box">
				<h12> Popular <span4>Products</span4> </h12>
				</div>

					<div class="latest-product">
                        <div class="product-carousel">
                            <div class="single-product">
                                <div class="product-f-image">
                                    <img src="img/product-1.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2><a href="single-product.html">Samsung Galaxy s4</a></h2>

                                <div class="product-carousel-price">
                                    <ins>₹12000.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                    <img src="img/product-2.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2>Nokia Lumia 1320</h2>
                                <div class="product-carousel-price">
                                    <ins>₹9000.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                    <img src="img/product-3.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2>LG Leon 2015</h2>

                                <div class="product-carousel-price">
                                    <ins>₹9000.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                    <img src="img/product-4.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2><a href="single-product.html">Sony</a></h2>

                                <div class="product-carousel-price">
                                    <ins>₹8000.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                    <img src="img/product-5.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2>iPhone 6</h2>

                                <div class="product-carousel-price">
                                    <ins>₹35000.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                    <img src="img/product-6.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2><a href="single-product.html">Samsung gallaxy note 4</a></h2>

                                <div class="product-carousel-price">
                                    <ins>₹4000.00</ins>
                                </div>
                            </div>
                        </div>
                    </div>

			</div>		<!-- end of product-view-1  -->



			<div class="product-view-1">
				<div class="title-box">
					<h12> Womens <span4>Clothes</span4> </h12>
				</div>

					<div class="latest-product">
                        <div class="product-carousel">
                            <div class="single-product">
                                <div class="product-f-image">
                                    <img src="img/clothes/1.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2><a href="single-product.html">Green tshirt</a></h2>

                                <div class="product-carousel-price">
                                    <ins>₹1000.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                   <img src="img/clothes/2.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2>Designer Dress</h2>
                                <div class="product-carousel-price">
                                    <ins>₹1500.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                   <img src="img/clothes/3.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2>zebra One Peice</h2>

                                <div class="product-carousel-price">
                                    <ins>₹2500.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                     <img src="img/clothes/4.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2><a href="single-product.html">Yellow Dress</a></h2>

                                <div class="product-carousel-price">
                                    <ins>₹8000.00</ins>
                                </div>
                            </div>
                            <div class="single-product">
                                <div class="product-f-image">
                                   <img src="img/clothes/5.jpg" alt="">
                                    <div class="product-hover">
                                        <a href="construction.php" class="add-to-cart-link"><i class="fa fa-shopping-cart"></i> Add to cart</a>
                                        <a href="single-product.html" class="view-details-link"><i class="fa fa-link"></i> See details</a>
                                    </div>
                                </div>

                                <h2>Blue Dress</h2>

                                <div class="product-carousel-price">
                                    <ins>₹5000.00</ins>
                                </div>
                            </div>

                        </div>
                    </div>

			</div>		<!-- end of product-view-1  -->







</div><!-- end of col-lg-9  -->

<div class="col-lg-3">


	<!-- <div class="sidebar">

	<div class="sidebar-title-box ">
	<h13>Popular Price List</h13>
	</div>

				<div class="sidebar-content">

						<div class="brand-box">
						<div class="row">
						<div class="col-lg-5">
						<img src="img/brands/1.png" height="35" width="80" class="brand-img" />
				    	</div>
					    <div class="col-lg-7">
						<p class="brand">Samsung Mobile Prices</p>
						</div>
						</div>
						</div>

						<div class="brand-box">
						<div class="row">
						<div class="col-lg-5">
						<img src="img/brands/2.png" height="45"  class="brand-img" />
				    	</div>
					    <div class="col-lg-7">
						<p class="brand">Apple Mobile Prices</p>
						</div>
						</div>
						</div>

						<div class="brand-box">
						<div class="row">
						<div class="col-lg-5">
						<img src="img/brands/3.jpg" height="35" width="80" class="brand-img" />
				    	</div>
					    <div class="col-lg-7">
						<p class="brand">Lennovo Mobile Prices</p>
						</div>
						</div>
						</div>

						<div class="brand-box">
						<div class="row">
						<div class="col-lg-5">
						<img src="img/brands/4.png" height="50"  class="brand-img" />
				    	</div>
					    <div class="col-lg-7">
						<p class="brand">xiaomi Mobile Prices</p>
						</div>
						</div>
						</div>

						<div class="brand-box-last">
						<div class="row">
						<div class="col-lg-5">
						<img src="img/brands/5.png" height="35" width="80" class="brand-img" />
				    	</div>
					    <div class="col-lg-7">
						<p class="brand">Xolo Mobile Prices</p>
						</div>
						</div>
						</div>
				</div>

     </div>	 -->



	 <div class="best-seller">
	 <div class="best-seller-title">
	 <h13>BEST SELLERS</h13>
	 </div>
	 <div class="best-seller-content">

	       <div class="owl-carousel">


			<div class="best-single-sidebar">
             <img src="images/deals/p1.jpg">
			 <h17>Floral Print buttoned</h17>
			 <div class="single-price-sidebar">
			 <h18>₹ 10,000</h18>
			 </div>
			 <div class="dual-button">
			 <div class="dual-button-cart">
			 <img src="images/cart2.png" width="auto" />
			 </div>
			 <div class="dual-button-cart-text">
			 <p>View Product</p>
			</div>
			</div>
			</div>

			<div class="best-single-sidebar">
			 <img src="images/deals/p2.jpg">
			 <h17>Floral Print buttoned</h17>
			 <div class="single-price-sidebar">
			 <h18>₹ 10,000</h18>
			 </div>
			</div>

			<div class="best-single-sidebar">
			 <img src="images/deals/p3.jpg">
 				 <h17>Floral Print buttoned</h17>
			 <div class="single-price-sidebar">
			 <h18>₹ 10,000</h18>
			 </div>
			</div>








          </div>
            <script>
            $(document).ready(function() {
              var owl = $('.owl-carousel');
              owl.owlCarousel({
                items: 1,
                loop: true,
                margin: 10,
                autoplay: true,
                autoplayTimeout: 30000,
                autoplayHoverPause: true
              });

            })
          </script>


	 </div>
	 </div>


	  <div class="best-seller-2">
	 <div class="best-seller-title">
	 <h13>Popular This Week</h13>
	 </div>
	 <div class="best-seller-content">

	       <div class="owl-carousel">


			<div class="best-single">
             <img src="img/shoes/4.jpg">
			 <h17>Nike Air Shoes</h17>
			 <div class="single-price">
			 <h18>₹ 10,000</h18>
			 </div>
            </div>

			<div class="best-single">
             <img src="img/shoes/3.jpg">
			 <h17>Vecto Spike Shoes</h17>
			 <div class="single-price">
			 <h18>₹ 7,000</h18>
			 </div>
            </div>

			<div class="best-single">
             <img src="img/shoes/2.jpg">
			 <h17>snicker Shoes</h17>
			 <div class="single-price">
			 <h18>₹ 23,000</h18>
			 </div>
            </div>


			<div class="best-single">
             <img src="img/shoes/1.jpg">
			 <h17>Nike Tech Shoes</h17>
			 <div class="single-price">
			 <h18>₹ 14,000</h18>
			 </div>
            </div>






          </div>
            <script>
            $(document).ready(function() {
              var owl = $('.owl-carousel');
              owl.owlCarousel({
                items: 1,
                loop: true,
                margin: 10,
                autoplay: true,
                autoplayTimeout: 1000,
                autoplayHoverPause: true
              });

            })
          </script>


	 </div>
	 </div>





</div>	<!-- end of col-lg-3 -->
</div><!--End of Main Container -->

</div><!--End of Main Container -->


<div class="footer">

<div class="footer-top">
<div class="container">
<div class="row">

<div class="col-lg-4">
<div class="footer-box-1">
<img src="img/ruppee.png" height="55"><h14>Cash On Delivery</h14>
</div>
</div>


<div class="col-lg-4">
<div class="footer-box-2">
<img src="img/easy.png" height="60"><h14>&nbsp;&nbsp;&nbsp;Easy Returns</h14>
</div>
</div>


<div class="col-lg-4">
<div class="footer-box-3">
<img src="img/truck.png" height="60"><h14>&nbsp;&nbsp;&nbsp;Free Shipping</h14>
</div>
</div>



</div>
</div>
</div>

<div class="footer-middle">
<div class="container">
<div class="row">

<div class="col-lg-4">
<div class="footer-middle-1">
<h15>Other Links</h15>
<ul class="links">
<li><a href="construction.php">Home</a></li>
<li><a href="construction.php">About Us</a></li>
<li><a href="construction.php">Feedback</a></li>
<li><a href="construction.php">FAQ</a></li>
<li><a href="construction.php">Contact US</a></li>
<li><a href="construction.php">Disclaimer</a></li>
<li><a href="construction.php">Privacy Policy</a></li>
</ul>

</div>
</div>


<div class="col-lg-4">
<div class="footer-middle-1">
<h15>Other Links</h15>

</div>
</div>


<div class="col-lg-4">
<div class="footer-middle-1">
&nbsp;<h15>Stay Connnected</h15><br>

<div class="social-icons">

<a href="construction.php"><img alt="Like Us On facebook" src="img/icons/facebook.png" class="facebook" height="30"></a>

<a href="construction.php"><img alt="Follow us on twitter" src="img/icons/twitter.png" class="twitter" height="30"></a>

<a href="construction.php"><img alt="Join us on GooglePlus" src="img/icons/googleplus.png" class="googleplus" height="30"></a>

</div>



</div>
</div>


</div>
</div>
</div>



<div class="footer-bottom">
		<div class="container">
		<div class="row">

		  <div class="col-lg-3 pull-left">
		  <div class="copyrights">
          <p>Copyright &copy; BestPrix 2016</p>
		  </div>
		  </div>

		  <div class="col-lg-3 pull-right">
		  <div class="made">
          Made with <span class="red">❤</span> in &nbsp;<img src="img/indian_flag.gif" class="flag">
          </div>
		  </div>

		</div>
		</div>
</div>

<!--	<div class="slide-out-div">
	<a class="handle" href="#">Content</a>
	<h3>Contact Us</h3>
    <a href="mailto:bestprix@bestprix.com">bestprix@bestprix.com</a><br /><br />
    <p>Thanks for checking out our Website. I hope you find this useful.</p>
    </div> -->

	<script src="js/owl.carousel.min.js"></script>
    <script src="js/jquery.sticky.js"></script>
    <!-- jQuery easing -->
    <script src="js/jquery.easing.1.3.min.js"></script>
    <!-- Main Script -->
    <script src="js/main.js"></script>
	 <script src="js/bootstrap.min.js"></script>

  </body>
</html>
