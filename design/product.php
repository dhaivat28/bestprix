<!DOCTYPE html>
<?php
		$keyword=$_GET['key'];	
		include('mysqli_connect.php');
?>
  <head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
		<meta name="description" content="">
		<meta name="author" content="">
		<link rel="shortcut icon" href="img/favicon1.png" type="image/x-icon" />
		
	<!--	<link href='http://fonts.googleapis.com/css?family=Ovo' rel='stylesheet' type='text/css' /> -->
	
	
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
		<!---------------- End for Slider ---------->
			
			
<!----------------technologies Slider ---------->
    <script src="script/jquery-1.11.1.js"></script>
    <script src="script/jquery.easing-1.3.js"></script>
    <script src="script/jquery.mousewheel-3.1.12.js"></script>
    <script src="script/jquery.jcarousellite.js"></script>
	
	
		
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
         </script>
   
   
   
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
	$(document).ready(
	
    function() {
        $(".account").click(function() {
            $(".account-content").fadeToggle();
        });
		
$('.account').mouseleave(function() {
    setTimeout(function () {
        $('.account-content').hide();
    }, 100);
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

	<!--<div class="top-border"></div> -->
	<div class="navigation">
	
		<a href="index.php"><img src="img/logo_new.png" class="logo" /></a>
	
				<div class="search">
		
		<form id="form" action="search_results.php" method="POST" class="new-search">
		<div class="field" id="searchform">
		<input type="text" size="25" value="" name="search_term" id="listings" onKeyUp="suggest(this.value);" class="" />
		<button type="submit" name="submit" value="submit" id="search">Search</button >  
		<div class="suggestionsBox" id="suggestions" style="display: none;"> 
        <div class="suggestionList" id="suggestionsList"> &nbsp; </div>
		</div>
		</div>
		</form>
	
		</div> <!--end of search -->
		
		
		<div class="account">
		
		<div class="outer">
		<img src="images/users.png" class="outer-img" height="20">
		</div>
		<div class="outer-2">&nbsp;&nbsp;My Account&nbsp; <span3>▼</span3></div>
		<div class="account-content">
		<a href="#" class="Login">Login</a><br><p class="acc-con">New User? <span5> Sign Up</span5></p>
		</div>
		</div>
		
		
		
		</div>
		
	</div>
	
	<span class="menu-trigger">MENU</span>	
					
	<div class="nav-menu">
		<ul class="clearfix">
		
								<li><a class="list_link" href="">Mobiles</a></li>
								<li><a class="list_link" href="#">Laptop & Computers</a></li>
								<li><a class="list_link" href="#">Computer Peripherals</a></li>
								<li><a class="list_link" href="#">Fashion & Accesories</a></li>
								<li><a class="list_link" href="#">Cameras</a></li>
								<li><a class="list_link" href="#">Tv & Entertainment</a></li>
								<li><a class="list_link" href="#">Gym Equipment</a></li>
								<li><a class="list_link" href="#">Personal & HealthCare</a></li>
								
		</ul>
	</div>

	
	<div class="container">
	<div class="row">
	
	
	<div class="col-lg-12">
	<div class="product-content">
	<div class="product-result">
	<div class="row">	
	<div class="col-lg-4">
		<div class="part-1">
		<?php
			$q="SELECT name,img FROM snapdeal_data where keyword='$keyword' LIMIT 1";	
			$result=mysqli_query($dbcon,$q);	
			while($row=mysqli_fetch_array($result, MYSQL_NUM))
			{
				$name=$row[0];
				$img=$row[1];		
				echo '<div class="part1-title"><h19>'.$name.'</h19></div>
				<img src="'.$img.'" class="product-img" />
			</div>';			
			}		
		?>			
		</div>	
		<div class="col-lg-4">	
			<?php
				$q1="SELECT price,url FROM snapdeal_data where keyword='$keyword' LIMIT 1";					
				$result1=mysqli_query($dbcon,$q1);	
				while($row1=mysqli_fetch_array($result1, MYSQL_NUM))
				{
					$price=$row1[0];
					$url=$row1[1];
					echo '<div class="part-2">
						<img src="img/snapdeal.png" class="snapdeal-img" >
						<div class="snapdeal-price">
							<h20>Rs. '.$price.'</h20>
						</div>
						<a href="'.$url.'" class="btn1">Buy Now</a><br>
					</div>';														
				}			
			?>
			
		</div>	
		<div class="col-lg-4">
		<?php
		$words = explode(" ", $keyword);
		//echo sizeof($words);
		$c=0;
		$keyword_new="";
			function callme()
			{		
					$limit=count($GLOBALS['words'])-$GLOBALS['c'];
					if($limit<2)
					{
						echo '<div class="part-3">
								<img src="img/infibeam.png" class="infibeam-img" />
								<div class="infibeam-price">
									<h20> Not Available</h20>
								</div>								
							</div>';	
					}
					else
					{		
					$db = new mysqli('localhost', 'root' ,'', 'bestprix');
					$GLOBALS['keyword_new']="";	
					for($i=0;$i<$limit;$i++)
					{
						$GLOBALS['keyword_new'].="%".$GLOBALS['words'][$i];
						//echo "<br>inside";
					}
					//echo $GLOBALS['keyword_new'];
					$q2="SELECT price,url FROM infibeam_data where keyword like '".$GLOBALS['keyword_new']."%' limit 1";					
					$result2=mysqli_query($db,$q2);	
					if(mysqli_num_rows($result2)<1)
					{
						$GLOBALS['c']++;
						//echo "<br>here";
						callme();						
					}
					else
					{
						while($row2=mysqli_fetch_array($result2, MYSQL_NUM))
						{
							$price=$row2[0];
							$url=$row2[1];
							echo '<div class="part-3">
								<img src="img/infibeam.png" class="infibeam-img" />
								<div class="infibeam-price">
									<h20>Rs. '.$price.'</h20>
								</div>
								<a href="'.$url.'" class="btn1">Buy Now</a><br>
							</div>';	
									mysqli_close($db);											
						}
					}
					}
				}
			callme();	
			mysqli_close($dbcon);		
			?>
		</div>	
		</div>
		</div>

	<div class="search-result">
	</div>
	
	<div class="search-result">
	</div>
	
	
	</div>
	</div>	
	
	</div>
	</div>



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
<li><a href="#">Home</a></li>
<li><a href="#">About Us</a></li>
<li><a href="#">Feedback</a></li>
<li><a href="#">FAQ</a></li>
<li><a href="#">Contact US</a></li>
<li><a href="#">Disclaimer</a></li>
<li><a href="#">Privacy Policy</a></li>
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

<a href="#"><img alt="Like Us On facebook" src="img/icons/facebook.png" class="facebook" height="30"></a>
<a href="#"><img alt="Follow us on twitter" src="img/icons/twitter.png" class="twitter" height="30"></a>
<a href="#"><img alt="Join us on GooglePlus" src="img/icons/googleplus.png" class="googleplus" height="30"></a>
</div>

<div class="newsletter">
<h16>Join Our Newsletter</h16><br>
<form>
<input type="text" class="news-input" placeholder="What's your email? ">
<input type="submit" value="Sign Up" class="btn">

</form>
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
	
	<div class="slide-out-div">
	<a class="handle" href="#">Content</a>
	<h3>Contact me</h3>
    <a href="mailto:wpaoli@gmail.com">wpaoli@gmail.com</a><br /><br />
    <p>Thanks for checking out my jQuery plugin, I hope you find this useful.</p>
    <p>This can be a form to submit feedback, or contact info</p>
    </div> 

	<script src="js/owl.carousel.min.js"></script>
    <script src="js/jquery.sticky.js"></script>
    <!-- jQuery easing -->
    <script src="js/jquery.easing.1.3.min.js"></script>
    <!-- Main Script -->
    <script src="js/main.js"></script>
	 <script src="js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="js/ie10.js"></script>
  </body>
</html>
