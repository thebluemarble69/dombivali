import colorama
import time
import asyncio
import websockets
colorama.init()

async def send_msg(websocket):
    while True:
        msg = await asyncio.to_thread(input, "Server >>>")
        if msg.lower == 'quit':
            await websocket.close()
            break
            print("QUIT")
        await websocket.send(msg)
async def rec_msg(websocket):
    try:
        async for msg in websocket:
            print(f"\nClient: {msg}")
            print("Server >>>", end="", flush=True)
    except websockets.ConnectionClosed:
        print("quit")

async def handle(websocket):
    print("\033[92mClient connected\033[00m")
    await asyncio.gather(send_msg(websocket), rec_msg(websocket))
async def s():
    async with websockets.serve(handle, "localhost", 8765):
        print("\033[92mrunning...\033[00m")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(s())
        
        
