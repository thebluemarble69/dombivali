import asyncio
import colorama
from websockets.asyncio.server import serve

colorama.init()

async def Run(websocket):
    #await asyncio.sleep(2)
    await websocket.send(input("give shit u idiot::: "))
    x = await websocket.recv()
    v = await websocket.recv()
    if v == "exit":
        print("\033[91mClosed.")
        await websocket.close()
    print(x + " " + v)

async def main():
    try:
        server = await serve(Run, "localhost", 8765)
        print("\033[92mlistnningg....")
        await server.serve_forever()
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    asyncio.run(main())

