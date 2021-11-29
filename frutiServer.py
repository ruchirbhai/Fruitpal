import socketio
import frutipal

sio = socketio.AsyncServer(async_mode='asgi')
app = socketio.ASGIApp(sio, static_files={
    '/': './public/'
})


@sio.event
async def connect(sid, environ):
    print(sid, 'connected')


@sio.event
async def disconnect(sid):
    print(sid, 'disconnected')

@sio.event
async def priceAPI(sid,data):
    print(sid,data)
    print(frutipal.parseDoc('api-description.apib',attrib=data))
    # result = data['num'][0] + data['num'][1]
    # await sio.emit('sum_result', {'result':result}, to=sid)
# working socket server no websocket
# import socketio

# sio = socketio.Server()
# app = socketio.WSGIApp(sio, static_files={
#     '/': './public/'
# })


# @sio.event
# def connect(sid, environ):
#     print(sid, 'connected')


# @sio.event
# def disconnect(sid):
#     print(sid, 'disconnected')

# @sio.event
# def priceAPI(sid, data):
#     print(sid,data)

## working Python server
# import socketserver
# import sys
# import traceback

# # Create a Request Handler

# # In this TCP server case - the request handler is derived from StreamRequestHandler

# class MyTCPRequestHandler(socketserver.StreamRequestHandler):
# # handle() method will be called once per connection
#     def handle(self):
#         # Receive and print the data received from client
#         print("Recieved one request from {}".format(self.client_address[0]))
#         msg = self.rfile.readline().strip()
#         print("Data Recieved from client is:".format(msg))
#         print(msg)
#         # Send some data to client
#         self.wfile.write("Hello Client....Got your message".encode())

# # Create a TCP Server instance
# # aServer = socketserver.TCPServer(("127.0.0.1", 9091), MyTCPRequestHandler)
# try:
#     # Start the server
#     socketserver.TCPServer.allow_reuse_address = True
#     aServer = socketserver.TCPServer(("127.0.0.1", 9090), MyTCPRequestHandler)
#     print('Starting fruit Python server')
#     sys.stdout.flush()
#     aServer.serve_forever()
# except KeyboardInterrupt:
#     aServer.shutdown()
#     aServer.server_close()
#     print("FruitServer handler shutdown")
#     sys.stdout.flush()
# except Exception:
#     traceback.print_exc(file=sys.stderr)
#     sys.stderr.flush()
#     raise
# # Listen for ever

# aServer.serve_forever()






# import socketserver as SocketServer
# import sys
# import traceback


# HOST = '127.0.0.1'
# PORT = 77777

# # def main(files, host=HOST, port=PORT):
# host=HOST 
# port=PORT
# global server
# global hooks
# # hooks = Hooks()
# # # Load hook files
# # for f in files:
# #     load_hook_files(f)

# try:
#     # Start the server
#     SocketServer.TCPServer.allow_reuse_address = True
#     # server = SocketServer.TCPServer((host, port), HookHandler)
#     server = SocketServer.TCPServer((host, port))
#     print('Starting frutipal Python hooks handler')
#     sys.stdout.flush()
#     server.serve_forever()
# except KeyboardInterrupt:
#     server.shutdown()
#     server.server_close()
#     print("frutipal Python hooks handler shutdown")
#     sys.stdout.flush()
# except Exception:
#     traceback.print_exc(file=sys.stderr)
#     sys.stderr.flush()
#     raise

