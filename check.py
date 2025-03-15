import time
while True:
    f = open('log2.txt','r')
    mes = f.readline()
    f.close()
    print(mes)
    time.sleep(1)
