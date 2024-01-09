import asyncio
import websockets
import time
import os
import signal
import datetime

connected_clients = set()
lock = asyncio.Lock()

text = """Concerning  Hobbits 

This  book  is  largely  concerned  with  Hobbits,  and  from  its 
pages  a  reader  may  discover  much  of  their  character  and  a 
little  of  their  history.  Further  information  will  also  be  found 
in  the  selection  from  the  Red  Book  of  Westmarch  that  has 
already  been  published,  under  the  title  of  The  Hobbit.  That 
story  was  derived  from  the  earlier  chapters  of  the  Red  Book, 
composed  by  Bilbo  himself,  the  first  Hobbit  to  become 
famous  in  the  world  at  large,  and  called  by  him  There  and 
Back  Again ,  since  they  told  of  his  journey  into  the  East  and 
his  return:  an  adventure  which  later  involved  all  the  Hobbits 
in  the  great  events  of  that  Age  that  are  here  related. 

Many,  however,  may  wish  to  know  more  about  this  re¬ 
markable  people  from  the  outset,  while  some  may  not  possess 
the  earlier  book.  For  such  readers  a  few  notes  on  the  more 
important  points  are  here  collected  from  Hobbit-lore,  and 
the  first  adventure  is  briefly  recalled. 

Hobbits  are  an  unobtrusive  but  very  ancient  people,  more 
numerous  formerly  than  they  are  today;  for  they  love  peace 
and  quiet  and  good  tilled  earth:  a  well-ordered  and  well- 
farmed  countryside  was  their  favourite  haunt.  They  do  not 
and  did  not  understand  or  like  machines  more  complicated 
than  a  forge-bellows,  a  water-mill,  or  a  hand-loom,  though 
they  were  skilful  with  tools.  Even  in  ancient  days  they 
were,  as  a  rule,  shy  of  ‘the  Big  Folk’,  as  they  call  us,  and 
now  they  avoid  us  with  dismay  and  are  becoming  hard  to 
find.  They  are  quick  of  hearing  and  sharp-eyed,  and  though 
they  are  inclined  to  be  fat  and  do  not  hurry  unnecessarily,  they 
are  nonetheless  nimble  and  deft  in  their  movements.  They """

splitted_text = text.split(' ')

delivering_text = []

async def broadcast_message(websocket, message, connected):
    websockets.broadcast(connected, message)

async def deliver(websocket):
    connected_clients.add(websocket)
    try:
        client_address = websocket.remote_address
        print(f"Connection from {client_address}")
        # websockets.broadcast(connected_clients, text)
        for word in splitted_text:
            try:
                await asyncio.sleep(0.2)
                # time.sleep(0.2)
                await websocket.send(f'{word} ')
                print(f'Sending "{word} "')
            except websockets.exceptions.ConnectionClosedError:
                print(f"Connection from {client_address} closed during transmission")
                connected_clients.remove(websocket)
    except websockets.exceptions.ConnectionClosedError:
            # Remove the client from the set when the connection is closed
            print(f"Connection from {client_address} closed")
            connected_clients.remove(websocket)
    except websockets.exceptions.ConnectionClosedOK:
            # Remove the client from the set when the connection is closed
            print(f"Connection from {client_address} closed OK")
            connected_clients.remove(websocket)

async def handle_websocket(websocket, path):
    # while True:
    #     # message = await websocket.recv()
    #     # reply = f"Received message: {message}"
    #     # print(reply)
    #     await websocket.send("Hi!")
    #     # Handle the message as needed\
    await deliver(websocket)

def process_input(new_text):
    if len(delivering_text) > 50:
        delivering_text.pop(0)
    delivering_text.append({
        'text': new_text,
        'time': datetime.datetime.now(),
    })

'''
This function needs to be tested
'''
def clean_outdated():
    i = 0
    l = len(delivering_text)
    delete_prev = False
    while i < l:
        if delete_prev:
            delivering_text.pop(i)
            l -= 1
            if (i == l):
                break
        record = delivering_text[i]
        if record['time'] - datetime.timedelta(seconds = 3) > datetime.datetime.now():
            delete_prev = True
        

async def main():
    print("WebSocket connection is available")
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    port = int(os.environ.get("PORT", "8000"))
    async with websockets.serve(handle_websocket, "", port):
        await stop
    # server = await websockets.serve(handle_websocket, "0.0.0.0", 8000)
    # print("WebSocket server started")
    # await server.wait_closed()
    # exit(0)

if __name__ == "__main__":
    asyncio.run(main())

