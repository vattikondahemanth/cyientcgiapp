
print('''
<!DOCTYPE html>
<html>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

<body>
<!-- Navigation -->
<nav class="w3-container w3-teal">
  <a href=\"http://localhost:8080/cgi-bin/home/home.py\" class="w3-button w3-bar-item">Home</a>
  <a href=\"http://localhost:8080/cgi-bin/login/login.py\" class="w3-button w3-bar-item">Sign Out</a>
</nav>

<!-- Description -->
<section class="w3-container w3-center w3-content" style="max-width:600px">
  <h2 class="w3-wide">Contact US</h2>
  <p class="w3-opacity"><i>Designing Tommorrow Together</i></p>
  <p class="w3-opacity">Contact 9223028079</p>
</section>

<!-- Footer -->
<footer>
    <div class="content-wrap"></div>
    <h2>Let's Keep in Touch!</h2>

    <!-- Social media and contact links. Add or remove any networks. -->
    <ul class="contact-list">
        <li><a href="https://www.linkedin.com/company/cyient/" target="_blank">Linkedin</a></li>
        <li><a href="https://twitter.com/Cyient" target="_blank">Twitter</a></li>
    </ul>
    </div>
</footer>

<style>
footer {
  background: #57d8bc;
  color: #ffffff;
  text-align: center;
}
.contact-list {
  list-style-type: none;
  padding: 0;
  display: flex;
  justify-content: center;
}
.contact-list a {
  padding: 15px;
  display: inline-block;
}

</style>
</body>
</html>

''')
