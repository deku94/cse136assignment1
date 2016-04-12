#!/usr/bin/node
'use strict';

var filterVars = new RegExp('(^REQUEST)', 'i');
var browserVars = [];
var serverVars = [];

console.log("Content-Type: text/html\n");
console.log("<!doctype html>");
console.log("<html><head><title>Environment Var Node-CGI</title></head><body>");

for ( let x in process.env ) {
	if(filterVars.test(x)) {
		browserVars[x] = process.env;
	}
	else {
		serverVars[x] = process.env;
	}
}

let serverdata = '';
Object.keys(serverVars).sort().forEach(function(key, i) {
	serverdata += '<tr><td>' + key + '</td><td>' + process.env[key] + '</td></tr>'});

let browserdata ='';
Object.keys(browserVars).sort().forEach(function(key, i) {
	browserdata += '<tr><td>' + key + '</td><td>' + process.env[key] + '</td></tr>'});

console.log("<h1>Variables Sent By Server</h1>");

console.log("<table><tr><th>Variable</th><th>Value</th></tr>" + serverdata + "</table>");

console.log("<h1>Variables Sent By Browser</h1>");

console.log("<table><tr><th>Variable</th><th>Value</th></tr>" + browserdata + "</table>");

console.log("</body></html>");

