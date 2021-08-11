import sys
import unicodedata

#globais uteis
IcPort= 0.072723
IcEnglish = 0.0656010
enAlphabet = "abcdefghijklmnopqrstuvwxyz"
k= 0
l = -1
frequencies = {v:k for v in enAlphabet}
minusfrequencies = {v:l for v in enAlphabet}

letToNumber= dict(zip(enAlphabet, range(len(enAlphabet))))
numberToLetter = {v:k for k, v in letToNumber.items()}

enDistrib = {
  'a': 0.08167,
  'b': 0.01492,
  'c': 0.02782,
  'd': 0.04253,
  'e': 0.12702,
  'f': 0.02228,
  'g': 0.02015,
  'h': 0.06094,
  'i': 0.06966,
  'j': 0.00153,
  'k': 0.00772,
  'l': 0.04025,
  'm': 0.02406,
  'n': 0.06749,
  'o': 0.07507,
  'p': 0.01929,
  'q': 0.00095,
  'r': 0.05987,
  's': 0.06327,
  't': 0.09056,
  'u': 0.02758,
  'v': 0.00978,
  'w': 0.02360,
  'x': 0.00150,
  'y': 0.01974,
  'z': 0.00074,
}

ptDistrib = {
  'a': 0.1463,
  'b': 0.0104,
  'c': 0.0388,
  'd': 0.0499,
  'e': 0.1257,
  'f': 0.0102,
  'g': 0.0130,
  'h': 0.0128,
  'i': 0.0618,
  'j': 0.0040,
  'k': 0.0002,
  'l': 0.0278,
  'm': 0.0474,
  'n': 0.0505,
  'o': 0.1073,
  'p': 0.0252,
  'q': 0.0120,
  'r': 0.0653,
  's': 0.0781,
  't': 0.0434,
  'u': 0.0463,
  'v': 0.0167,
  'w': 0.0001,
  'x': 0.0021,
  'y': 0.0001,
  'z': 0.0047,
}

###### funções uteis
def removeSpecialChar(message):
    m2= unicodedata.normalize("NFD", message)
    m2 = m2.encode("ascii","ignore")
    m2= m2.decode("utf-8")
    return m2

def closethis():
    print("option doesn't exist / opçao nao encontrada")
    sys.exit(0)




""" def getCurrentIC(message):
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
 """

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
    

        

def getKeyLength():
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

def calcuLateChi(ci, ei):
    aux = (ci - ei)**2

    return(aux/ei)

def getChiSquared(array, lang, messageleng):
    print("Nessa fase vamos usar a estatística de chi-squared para te dar suas possíveis letras da keyword.\n Para cada grupo, teste as com o menor indice em sua chave. Pressione qualquer tecla para começar")
    input()

    for group in array:
#Calcula a distribuição esperada para cada grupo do texto
        expectedDistr = {}

        if lang==1:
            expectedDistr = dict(ptDistrib)
        elif lang==2:
            expectedDistr = dict(enDistrib)

        for letter in enAlphabet:
            aux= expectedDistr[letter] * len(group)
            
            expectedDistr[letter] = aux
    #Pegando a frequencia de cada letra da mensagem no texto
        #calcular a freq de cada letra

        i=0
        print("Key              | sequence deciphred        |chi-sq")
        print("\n")
        for i in range(len(enAlphabet)):
            groupChi=0
            testText = ""
            #iteracao
            for letter in group:
                numberLet = (letToNumber[letter]-i)%(26)
                newletter = numberToLetter[numberLet]
                testText+= newletter

            #montar a frequencia de cada iteração de cada grupo
            letfrequencies = {v:k for v in enAlphabet}

            for letter in testText:
                letfrequencies[letter]+=1
            #pra cada letra do alfabeto calcular o chi e jogar num array
            chiList=[]
            for letter in enAlphabet:
                chiaux = calcuLateChi(letfrequencies[letter], expectedDistr[letter])
                
                groupChi += chiaux
                #chiList.append(chiaux)

            print(str(numberToLetter[i]) + "            |"+testText+"       |"+str(groupChi))
        print("Analise os resultados. Depois, aperte qualquer tecla para continuar...")
        input()



      


def findKey(keylength, Lang):

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
#divide a string em grupos
    dividedString = [(message[i:i+keylength]) for i in range(0, len(message), keylength)]
    array= [""]*keylength
    #para cada subgrupo, vou calcular a frequencia, e o chi-squared. Depois vou shiftar cada letra no grupo em 1 e fazer o mesmo.
    #quero retornar os menores chi-squares c suas respectivas letras
    #repetir isso pra todo subgrupo

    for subtext in dividedString:
        for i in range(len(subtext)):
            array[i]= array[i]+ subtext[i]
    getChiSquared(array, Lang, messageSize)


#findKey(14, 1)

print("Escolha Portugues(1) ou Ingles(2)")
choice = input()

if(choice!="1")&(choice!="2"):
    closethis()
else:
    getKeyLength()
    print("Se você já escolheu o tamanho da sua chave, escreva-o e pressione enter")
    tamanho = input()
    tamanhoInt = int(tamanho)
    language = int(choice)
    findKey(tamanhoInt, language )