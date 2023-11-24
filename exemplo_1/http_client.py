# import socket

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# socket para transferências em texto

# client.connect(("example.com", 80))# usando a porta 80

# # request
# cmd = "GET http://example.com/index.html HTTP/1.0\r\n\r\n".encode() # encode para a serialização dos dados
# client.send(cmd)# enviando a requisição

# while True:
#     data = client.recv(300) # tamanho do dado recebido
#     if len(data) < 1:
#         break
#     print(data.decode(), end="") # decode para a conversão em utf-8


# client.close()

import httpx

response = httpx.get("http://example.com/index.html")

print(response.status_code)
print(response.headers)
print(response.content)