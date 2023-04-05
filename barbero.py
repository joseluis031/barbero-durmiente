#codigo barbero durmiente

import threading
import time
import random

#semaforos
silla = threading.Semaphore(1)
cortar = threading.Semaphore(0)
cortado = threading.Semaphore(0)
mutex = threading.Semaphore(1)

#variables
clientes = 0
barbero = 0

def barbero():

    global clientes
    global barbero

    while True:
        silla.acquire()
        cortar.release()
        barbero = 1
        print("Barbero esta cortando el pelo")
        time.sleep(2)
        cortado.release()
        barbero = 0
        
def cliente():
    

    global clientes
    global barbero

    while True:
        mutex.acquire()
        if clientes < 3:
            clientes += 1
            print("Cliente llega a la barberia")
            silla.release()
            mutex.release()
            cortar.acquire()
            print("Cliente esta siendo atendido")
            cortado.acquire()
            mutex.acquire()
            clientes -= 1
            print("Cliente se va de la barberia")
            mutex.release()
        else:
            mutex.release()
            print("Cliente se va de la barberia")
            time.sleep(2)
            
def main():
    
    
    
    hilo_barbero = threading.Thread(target=barbero)
    hilo_barbero.start()
    
    while True:
        hilo_cliente = threading.Thread(target=cliente)
        hilo_cliente.start()
        time.sleep(2)

if __name__ == "__main__":
    main()