local ws, err = http.websocket("ws://192.168.0.101:25565")
if ws then
    io.write("Input text - ")
    local msg = io.read()
    ws.send(msg)
    ws.close()
end