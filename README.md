# pdf_flask_site
A site inteded to accept user information, which then generates a pdf for download. It uses the python reportlab library to generate the pdf, and pyqrcode to create a unique qr code for each pdf, which is based off of the form data. 

This was made to satisfy a requirement that each student turn in a reciept with their chromebook at the end of the school year. It worked very well. 

Index page:
===
<p align="center">
  <img src='/static/index.png' width='500px'>
</p>

After the user inputs the required information, it generates a pdf and returns the page below:

Download page:
===
<p align="center">
  <img src='/static/user.png' width='500px'>
</p>

Below is an example of the downloaded PDF:

Success!:
===

<p align="center">
  <img src='/static/ABCD1234.png' width='500px'>
</p>

If you want to edit this for yourself, alter the contents of the reportqr.py file. This is the file which needs to be run from the cli.

A bit of knowledge of the reportlab for python library is suggested, but not required. You could easily modify the language and keep the formatting as is.

If you want to modify the qrcode, then alter the app.py file. Specifically, the index() function, which takes the form data and generates a qrcode. 
