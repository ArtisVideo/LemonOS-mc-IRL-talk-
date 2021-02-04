import asyncio
import websockets

async def hello(websocket, path):
    message = await websocket.recv()
    await websocket.broadcast(message)
    print(message)

start_server = websockets.serve(hello, "192.168.0.101", 8765)
print("server started")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()