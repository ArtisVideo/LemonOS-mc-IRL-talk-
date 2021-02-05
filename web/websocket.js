const WebSocketServer = require('ws').Server;
const wss = new WebSocketServer({ port: 25565 });
  

wss.on('connection', function connection(ws) {
    ws.on('message', function incoming(message) {
      console.log(message);
    });
  
    ws.send('something');
  });