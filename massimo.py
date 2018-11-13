#Programma che individua il massimo tra 10 interi.

i = 2

N = input('Inserisci 1° valore:  ')
N = int(N)
M = N

while i<11:
   N = input('Inserisci ' + str(i) +'° valore:  ')
   N = int(N)
   if N>M:
      M = N
	
   i += 1 

print ('il valore più alto inserito è: ' + str(M))

      