
import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.43.226"
port=2222
s.bind((ip,port))
def receiver():
    while True:
        x=s.recvfrom(100)
        msg=x[0].decode()
        client=x[1][0]
        print("\t\t\t\t{0}-->{1}\t\t".format(client,msg))
        
def sender():
    while True:
        x=input("")
        r.sendto(x.encode(),("192.168.43.22",1111))
        
if __name__=="__main__":
    print()
    print("sended message\t\t\treceived message")
    print()
    t1=threading.Thread(target=receiver)
    t1.start()
    t2=threading.Thread(target=sender)
    t2.start()

