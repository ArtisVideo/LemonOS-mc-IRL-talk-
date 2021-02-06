import asyncio
import websockets

async def hello(websocket, path):
    message = await websocket.recv()
    await websocket.send(message)
    print(message)

start_server = websockets.serve(hello, "Oscar-PC", 25565)
print("server started")

Text = input("Please gib me some text - ")
await websocket.send(Text)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()