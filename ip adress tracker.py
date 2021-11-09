import socket
hostn = socket.gethostname()
print(hostn)
IPAd = socket.gethostbyname(hostn)
print("IP ADRESS IS:" + IPAd)