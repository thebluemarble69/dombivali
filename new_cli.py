import websockets
import colorama
import asyncio

colorama.init()
async def send_msg(websocket):
    while True:
        x = await asyncio.to_thread(input, "Clinet >>>")
        if x.lower() == "quit":
            await websocket.close()
            break
        await websocket.send(x)


async def rec_m(websocket):
    try:
        async for msg in websocket:
            print(f"\nSevrer: {msg}")
            print("Clinet >>>", end="", flush=True)
    except websockets.ConnectionClosed:
        print("server gone")

async def main():
    async with websockets.connect("ws://localhost:8765") as s:
        print("\033[92mSevrer sconnected\033[00m")
        await asyncio.gather(send_msg(s), rec_m(s))


if __name__ == "__main__":
    asyncio.run(main())
