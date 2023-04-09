# barbero-durmiente

El link de este repositorio es el siguiente: [GitHub](https://github.com/joseluis031/barbero-durmiente.git)

## Codigo del barbero

```
#codigo barbero durmiente

import threading
import time
import random

#semaforos
silla = threading.Semaphore(1)  #solo puede haber un cliente en la silla
cortar = threading.Semaphore(0) #el barbero no puede cortar hasta que el cliente se siente
cortado = threading.Semaphore(0)    #el cliente no puede irse hasta que el barbero termine de cortar
mutex = threading.Semaphore(1)  #para controlar el numero de clientes

#variables
clientes = 0    #numero de clientes en la barberia
barbero = 0 #estado del barbero
lista_cortes = 0

def barbero():  #funcion del barbero

    global clientes     #variables globales
    global barbero      
    global lista_cortes
    
    while True:     
        silla.acquire()     #el barbero espera a que el cliente se siente
        cortar.release()        #el barbero puede cortar
        barbero = 1     #el barbero esta cortando
        print("\nBarbero esta cortando el pelo al cliente {}".format(lista_cortes))      
        time.sleep(2)       #el barbero tarda 2 segundos en cortar
        cortado.release()    #el cliente puede irse
        barbero = 0    #el barbero termino de cortar
        
def cliente():  #funcion del cliente
    

    global clientes
    global barbero
    global lista_cortes
    
    while True: 
        mutex.acquire()#para controlar el numero de clientes

        if clientes < 3:    #si hay menos de 3 clientes en la barberia
            clientes += 1   #se suma un cliente
            lista_cortes += 1
            print("\nCliente {} llega a la barberia".format(lista_cortes))
            silla.release()    #el cliente se sienta
            mutex.release()   #se libera el mutex
            cortar.acquire()    #el cliente espera a que el barbero lo atienda
            print("\nCliente {} esta siendo atendido".format(lista_cortes)) 
            cortado.acquire()   #el cliente espera a que el barbero termine de cortar
            mutex.acquire()    #se libera el mutex
            clientes -= 1   #se resta un cliente
            print("\nCliente {} se va de la barberia con corte nuevo".format(lista_cortes))
            mutex.release()   #se libera el mutex
        else:   #si hay mas de 3 clientes en la barberia
            lista_cortes += 1   
            mutex.release()  #se libera el mutex
            print("\nCliente {} se va de la barberia porque esta llena".format(lista_cortes))
            time.sleep(5)   #el cliente espera 5 segundos y vuelve a intentar entrar
            if barbero == 0:
                clientes == 0
                cliente()
            else:
                print("\nCliente {} se va de la barberia porque esta llena".format(lista_cortes))



def main():
    
    
    
    hilo_barbero = threading.Thread(target=barbero)  #se crea el hilo del barbero
    hilo_barbero.start()    #se inicia el hilo del barbero

    while True: 
        hilo_cliente = threading.Thread(target=cliente)   #se crea el hilo del cliente
        hilo_cliente.start()    #se inicia el hilo del cliente
        time.sleep(5)   #el cliente llega cada 5 segundos
```

## Codigo del main

```
from barbero import main

if __name__ == "__main__":
    main()
```



## Ejecucion del codigo

```
Cliente 1 llega a la barberia

Cliente 1 esta siendo atendido

Barbero esta cortando el pelo al cliente 1

Cliente 1 se va de la barberia con corte nuevo

Cliente 2 llega a la barberia

Cliente 2 esta siendo atendido

Barbero esta cortando el pelo al cliente 2
Cliente 2 se va de la barberia con corte nuevo
```


```
Cliente 17 llega a la barberia

Barbero esta cortando el pelo al cliente 17

Cliente 17 esta siendo atendido
Cliente 17 se va de la barberia con corte nuevo


Cliente 18 llega a la barberia

Cliente 18 se va de la barberia porque esta llena

Cliente 19 se va de la barberia porque esta llena

Cliente 20 se va de la barberia porque esta llena
```
