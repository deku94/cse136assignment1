Set up your hosting. We'll be using AWS default Linux instance.

If using AWS don't forget to add HTTP and HTTPS:
- Inbound Rules in AWS (EC2 -> Security Group -> Choose Instance -> Inbound -> Add HTTP and HTTPS)

Install Apache web server locally:

	sudo yum install httpd24
	sudo service httpd start

In /etc/httpd/conf/httpd.conf set up executable files folder by adding the following lines (for Perl):

	<Directory "/var/www/cgi-bin">
	   Options +ExecCGI
	</Directory>

	AddHandler cgi-script .cgi .pl

Restart the web server:

	sudo service httpd restart

Then add all your executable files into /var/www/cgi-bin or whatever folder you prefer. Cloning git repository is pretty convenient.

Change the permissions to the executable files you have added, i.e.:
    
    chmod 775 *.cgi

That should give you a working "static-dynamic" backend, either local or deployed.
