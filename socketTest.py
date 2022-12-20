import socket as sc

s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

host = 'localhost'
portas = range(0, 65535)

for porta in portas:
    r = s.connect_ex((host,porta))

if r == 0:
    print('Porta Aberta ==> {} ' .format(porta))