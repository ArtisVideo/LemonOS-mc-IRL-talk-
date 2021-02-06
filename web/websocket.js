//Imports
const WebSocketServer = require('ws').Server;
var net = require('net');

//Create socket
const wss = new WebSocketServer({ port: 25565 });
console.log("Server up!")

//Custom broadcast function to send a message to all connected websocket clients
wss.broadcast = function(data) {
  wss.clients.forEach(client => client.send(data));
};

//When get socket message/connection echo it back to all clients
wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(message) {
      console.log(message);
      wss.broadcast(message)
    });

});
