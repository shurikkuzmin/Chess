from chess_network import ChessServer, ChessClient

#server = ChessServer(host='10.15.3.1')
#server.start()

#server.send_move({'from': [6,4], 'to': [4,4]})

client = ChessClient(host='10.15.0.35', port=5000)
client.connect()
client.receive_move()