import sys
import unicodedata

IcPort= 0.072723
IcEnglish = 0.0656010
enAlphabet = "abcdefghijklmnopqrstuvwxyz"
k= 0
l = -1
frequencies = {v:k for v in enAlphabet}
minusfrequencies = {v:l for v in enAlphabet}


def removeSpecialChar(message):
    m2= unicodedata.normalize("NFD", message)
    m2 = m2.encode("ascii","ignore")
    m2= m2.decode("utf-8")
    return m2

def closethis():
    print("option doesn't exist / opçao nao encontrada")
    sys.exit(0)

def totalFreq():
    totalFreq=0
    for letter in enAlphabet:
        totalFreq += frequencies[letter]
    return totalFreq

def getFreqletter(myfreq):
    totalFreq=0
    for letter in enAlphabet:
        totalFreq += myfreq[letter]
    return totalFreq


def getCurrentIC(message):
    for letter in message:
        frequencies[letter]+=1
        minusfrequencies[letter]+=1
    #fazer a somatoria de n* n-1
    numerator = 0
    totalFrequ = totalFreq()
    for letter in enAlphabet:
        if(frequencies[letter]!=0):
            aux = frequencies[letter] * (frequencies[letter]-1)
            numerator +=aux
            print(numerator)
    denumerator = totalFrequ*(totalFrequ-1)
    indice = numerator/denumerator
    return indice

def findPossibleKeyL(totalFreq, indice, choice):
    if(choice=="1"):
        numerator = 0.0347 * totalFreq
        denum = (totalFreq-1)*indice + 0.0727 - (0.038*totalFreq)
        return(numerator/denum)
    else:
        numerator = 0.027 * totalFreq
        denum = (totalFreq-1)*indice + 0.065 - (0.038*totalFreq)
        return(numerator/denum)

###############
def calculateIcMedia(array):
    totalIC = 0
    #Calcular o ic de cada grupo
    for group in array:
        #calcular a freq de cada letra
        numerador=0
        letfrequencies = {v:k for v in enAlphabet}
        for letter in group:
            letfrequencies[letter]+=1
        for key in letfrequencies:
            prod = (letfrequencies[key]*(letfrequencies[key]-1))
            numerador+=prod
        denum = len(group)*(len(group)-1)
        groupIC= numerador/denum
        totalIC+=groupIC
    media = totalIC/len(array)
    return media
    

        

    pass

def getKeyLength(supposedKey, choice):
    #Assume a keylegth minimum 2 (lets go to 20)
    #split th cipher into groups with the keylength length
    #example, froup of 3 ABREMOSOREMOS; Gupor 1: AESES
    #for each group calculate the index of coincidence
    #Calculate the average index
    #Verify proximity to the IC
    #If the average is not close to the ic go to n++
    print("Ola, esse é o programa de crack da cifra de vigenere.\n INFORMAÇÕES: Esse programa utiliza-se do Indice de Coincidencia.\n Iremos supor chaves de tamanhos de 2 a 20 e retornar a media dos indices para o tamanho escolhido. Compare o indice com os fornecidos para os idiomas ingles(0.0656010) e portugues(0.072723) e escolha o que mais se aproximar.\n\nEscreva sua mensagem cifrada no arquivo cifraDesconhecida e pressione qualquer tecla para continuar...")
    input()

    #limpando o texto

    f = open("cifraDesconhecida.txt",'r', encoding='utf-8')
    text= f.read()
    f.close()
    lowertext = removeSpecialChar(text).lower()

    message=''
        #remove graphic signs and spaces
    for char in lowertext:
        if char in enAlphabet:
            message+=char
    messageSize = len(message)

    for chute in range(2, 20):
        array= [""]*chute
        dividedString = [(message[i:i+chute]) for i in range(0, len(message), chute)]
        
        for subtext in dividedString:
            for i in range(len(subtext)):
                array[i]= array[i]+ subtext[i]
        
        med = calculateIcMedia(array)
        st_chute = str(chute)
        st_med = str(med)
        print("keylenght: "+ st_chute +"|| IC= "+st_med)
        print("\nIC Ingles: 0.0656010\n IC Port: 0.072723")

    pass

print("Escolha Portugues(1) ou Ingles(2)")
choice = input()

if(choice=="1"):
    getKeyLength(IcPort, choice)

elif(choice=="2"):
    getKeyLength(IcEnglish, choice)

else:
    closethis()