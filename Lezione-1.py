print('hello world')
#intropython , let's have some fun
print('cocco bello')
print('cocco bello', 'cocco', sep = ' fresco ', end = ' solo 2 euro ')
var1 = 6
var2 = 9
print(' valore 1: {}, valore2: {}'.format(var1, var2))

print(2**11)
print(2^11) 
print(2*11)
#sono diversi: il '^' è lo xor sui bit del numero
#e comunque questo, come quelli sopra, è un commento: basta mettere # prima di esso
print(69%6) #% restituisce il resto della divisione del primo per il secondo operando

anni = -10/3
round(anni) # arrotonda al numero intero più vicino
abs(anni) #restituisce il valore assoluto

b = 'spacchiamo'
o = 'tutto'
j = b+o
print(j)
ack = j*2
print(ack)

h = input('quante caramelle vuoi?:') #occhio, input restituisce sempre una stringa
print('ne vuoi: {}, perchè non {}'.format(h, int(h)+1)) #e infatti qua va fatto il casting

chip = 'mai_rubare_rabarbari_in_barba_a_un_barbaro'
print(chip[5])
print(chip[-1])
print(chip[0:33])
print(chip[17:33])
print(chip[0:-5])

#Vediamo i tipi
intero = 7
floating = 7.77
stringa = 'bonjour'
booleano = True
il_niente = None
#ora convertiamo da un tipo a un altro
int(33.3)
float(12)
int('150')

#Booleani e loro operatori
basso = True
ricco = False
print(basso and ricco)
print(basso or ricco)
print(not ricco)
# se si prova 1/0 si ottiene un errore ma...
False and 1/0
True or 1/0
#il codice va, perché python è pigro
#and restituisce True solo gli input sono tutti True, python si ferma a leggere 'False and' 
#tanto il valore di verità si può calcolare a prescindere dalla seconda espressione (work smart not hard)

#lista: insieme di oggetti eterogenei
lista_x = list(range(1, 6, 2)) #creo una lista con range
lista_della_spesa = [54, 0.9, 'peperoni', lista_x] #posso anche avere una lista di liste
print(lista_della_spesa)

rap = 'lyrics coming at supersonic speed'
print(list(rap)) #creo una lista da una stringa, i cui elementi sono i singoli elementi della stringa
g = rap.split(' ') # con split, indico con quale carattere voglio separare gli elementi
print(g)

lettere1 = rap[1:10:2]
lettere2 = rap[::2]
