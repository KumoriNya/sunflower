import asyncio
import websockets
import time

text = """Three  Rings  for  the  Elven-kings  under  the  sky, 
Seven  for  the  Dwarf-lords  in  their  halls  of  stone, 
Nine  for  Mortal  Men  doomed  to  die, 
One  for  the  Dark  Lord  on  his  dark  throne 
In  the  Land  of  Mordor  where  the  Shadows  lie. 
One  Ring  to  rule  them  all,  One  Ring  to  find  them, 
One  Ring  to  bring  them  all  and  in  the  darkness  bind  them 
In  the  Land  of  Mordor  where  the  Shadows  lie. """

splitted_text = text.split(' ')

async def handle_websocket(websocket, path):
    # while True:
    #     # message = await websocket.recv()
    #     # reply = f"Received message: {message}"
    #     # print(reply)
    #     await websocket.send("Hi!")
    #     # Handle the message as needed
    client_address = websocket.remote_address
    print(f"Connection from {client_address}")
    while True:
        for word in splitted_text:
            time.sleep(0.2)
            await websocket.send(f'{word} ')
        message = await websocket.recv()
        # reply = f"Received message: {message}"
        # print(reply)

async def main():
    server = await websockets.serve(handle_websocket, "0.0.0.0", 8000)
    print("WebSocket server started")
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())

