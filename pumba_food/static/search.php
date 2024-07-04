<!DOCTYPE html>
<html lang="en">
     <head>
     <title>Search</title>
     <meta charset="utf-8">
     <meta name = "format-detection" content = "telephone=no" />
     <link rel="icon" href="images/favicon.ico">
     <link rel="shortcut icon" href="images/favicon.ico" />
     <link rel="stylesheet" href="css/style.css">
     <script src="js/jquery.js"></script>
     <script src="js/jquery-migrate-1.1.1.js"></script>
     <script src="js/script.js"></script> 
     <script src="js/superfish.js"></script>
     <script src="search/search.js"></script>
     <script src="js/jquery.equalheights.js"></script>
     <script src="js/jquery.mobilemenu.js"></script>
     <script src="js/jquery.easing.1.3.js"></script>
     <script src="js/jquery.ui.totop.js"></script>
     <script>
       $(document).ready(function(){
        $().UItoTop({ easingType: 'easeOutQuart' });
     }); 

     </script>
        
   
    <!--[if lt IE 8]>
       <div style=' clear: both; text-align:center; position: relative;'>
         <a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
           <img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
         </a>
      </div>
    <![endif]-->
    <!--[if lt IE 9]>
      <script src="js/html5shiv.js"></script>
      <link rel="stylesheet" media="screen" href="css/ie.css">


    <![endif]-->
     </head>

     <body>


  <div class="container_12">
    <div class="grid_12"><header>
    <h1>
        <a href="index.html">
          <img src="images/logo.png" alt="Your Happy Family">
        </a>
      </h1>
      <div class="h_phone">
        1 (800) 123 1234
      </div>
      <div class="clear"></div>
    <!--==============================header=================================-->
      <div class="menu_block ">
        <nav class="horizontal-nav full-width horizontalNav-notprocessed">
        <ul class="sf-menu">
         <li><a href="index.html">Home</a></li>
         <li><a href="index-1.html">about us</a></li>
         <li><a href="index-2.html">menu &amp; specials</a>
           <ul>
              <li><a href="#">columns 01</a></li>
              <li><a href="#">columns 02</a></li>
              <li><a href="#">columns 03</a>
                <ul>
                  <li><a href="#">columns 04</a></li>
                  <li><a href="#">columns 05</a></li>
                </ul>
              </li>
           </ul>
         </li>
         <li><a href="index-3.html">price list</a></li>
         <li><a href="index-4.html">contact us</a></li>
        </ul>
        </nav>
        <div class="clear"></div>       
      </div>

      
         </header>
    </div>
  </div>
<!--==============================Content=================================-->
<div class="content prv">
  <div class="container_12">
    <div class="grid_12 ">
        <h3>Search result:</h3>
			   <div id="search-results"></div>
    </div>
 </div>
</div>

<!--==============================footer=================================-->

  <footer>   
    <div class="container_12">
      <div class="grid_12">
        
        <a href="index.html" class="f_logo">
          <img src="images/f_logo.png" alt="">
        </a>
        <div class="copy">
        &copy; <span id="copyright-year"></span> <br> <a href="index-5.html">Privacy Policy</a><div></div>
        </div>
      </div>
    </div>  
  </footer>
</body>
</html>

