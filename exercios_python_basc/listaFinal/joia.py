hf,hdf,ha = None, None, None
cont = 0

while hf != "FIM" and hdf != "FIM" and ha != "FIM":
    hf, hdf, ha = input().split()
    if hf == "NAO" and hdf == "SIM" and ha == "NAO":
        cont += 1

if cont > 0:
    print("VITORIA")
else:
    print("DERROTA")       