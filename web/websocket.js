//Create WebSocket
var ws = new WebSocket("wss://artisvideo.com");

//When it works print
ws.addEventListener('open', function (event) {
    socket.send('It be working');
    console.log('It be working')
});

//Print out message when incoming
ws.addEventListener('message', function (event) {
    console.log('Message - ', event.data);
});

//Test function
function yeet() {
    window.close();
} 

//Safe close
function bye() {
    ws.close();
} 

