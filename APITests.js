import io from "socket.io-client"

const socket = io("http://127.0.0.1:9090");

socket.emit("hello", "world")
// var net = require('net');

// var client = new net.Socket();
// client.connect(8484, '127.0.0.1', function() {
//    console.log('Connected');
//    client.write('Hello, server! Love, Client.');
// });

// client.on('data', function(data) {
//    console.log('Received: ' + data);
//    client.destroy(); // kill client after server's response
// });