#!/usr/bin/node

var colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", 
	"lime", "maroon", "navy", "olive", "purple", "red", "silver", 
	"teal", "white", "yellow"];

var randomNumber = Math.floor((Math.random() * 16));

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1;

var yyyy = today.getFullYear();
if(dd<10){
	dd = '0'+dd;
}
if(mm<10){
	mm = '0'+mm;
}

var hours = today.getHours();
var minutes = today.getMinutes();

var today = dd+'/'+mm+'/'+yyyy + ' at ' +hours+':'+minutes;

console.log("Content-Type: text/html\n");
console.log("<!doctype html>");
console.log("<html><head><title>Hello Node-CGI Based CGI World!</title></head>");
console.log("<body style='background-color: " + colors[randomNumber] + "'><h1>Hello World from Node-CGI @ " + today + "</h1>");
console.log("</body></html>");
