#!/usr/bin/node
'use strict';

var querystring = require('querystring');

console.log("Content-Type: text/html\n");
console.log("<!doctype html>");
console.log("<html><head><title>Hello Node-CGI based CGI World!</title></head><body>");

if( process.env.REQUEST_METHOD==="POST" ) {
	var data = '';

	// Needed Variables are in the body..
	process.stdin.on('data', function(chunk) {
		data += chunk;
	});

	process.stdin.on('end', function() {
		var d = querystring.parse(data);
		printBody(d.username, d.password, d.magicnumber);
	});
}

else if( process.env.REQUEST_METHOD==="GET") {
	// Needed Variables are in the query string..
	var data = querystring.parse(process.env['QUERY_STRING']);
	printBody(data.username, data.password, data.magicnumber);
}

function printBody(username, password, magicnumber) {
	// var string = sayHello(username, password, magicnumber);
	for( var i = 0; i < magicnumber; i++) {
		console.log('<h1>Hello' + username + 'with a password of ' + password + '!<h1>');
	}
	console.log("</body></html>");
}

