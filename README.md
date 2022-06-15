# pdf_flask_site
A site inteded to accept user information, which then generates a pdf for download. It uses the python reportlab library to generate the pdf, and pyqrcode to create a unique qr code for each pdf, which is based off of the form data. 

This was made to satisfy a requirement that each student turn in a reciept with their chromebook at the end of the school year. It worked very well. 
Here is the initial page:
Index:
===
<p align="center">
  <img src='/static/index.png' width='700px'>
</p>

After the user inputs the required information, it generates a pdf and returns the page below:
Download:
===
<p align="center">
  <img src='/static/user.png' width='700px'>
</p>

Below is the final product:
PDF:
===

<p align="center">
  <img src='/static/ABCD1234.pdf' width='700px'>
</p>

