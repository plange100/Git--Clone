How To Send Emails Using Python

https://blog.ashutoshkrris.in/how-to-send-emails-using-python

Table of contents
Getting Started
Setting up Gmail for Sending Emails
How To Secure Your Email Connections?
Using SMTP_SSL()
Using .starttls()
How To Send Plain-Text Emails?
How To Send Fancy Emails?
Multipurpose Internet Mail Extensions (MIME)
Including Attachments
Including HTML Content
How To Send Bulk Emails?

How To Secure Your Email Connections?
When you're sending emails with Python, it's crucial to keep your messages and login details 
safe from prying eyes. To do this, you can use encryption to protect your communication. Two 
common methods for encrypting your email connection are SSL (Secure Sockets Layer) and TLS 
(Transport Layer Security).

To establish a secure connection with your email server, you have two options:

Using SMTP_SSL()
This method creates a secure connection right from the start, ensuring your communication 
is encrypted. The default port for this is 465. Thus, if port is zero, or not specified,
 .SMTP_SSL() will use this standard port for SMTP over SSL.