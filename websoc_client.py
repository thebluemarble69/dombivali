import asyncio
import colorama
import websockets
colorama.init()
async def main():
    while True:
        async with websockets.connect("ws://localhost:8765") as ws:
            async for msg in ws:
                print(f"Received the msg: {msg}")
                await ws.send("Received tha msg.")
                x = input("Chat: ")
                if x == "exit":
                    exit()
                await ws.send(x)

if __name__ == "__main__":
    print("\033[92mRunnned.")
    asyncio.run(main())
