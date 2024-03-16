'''Desenvolvido por Giovanni Galarda Strasser
ENUNCIADO
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de operações, operações com dados diferentes, e operações em ordem 
diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
ambiente repl.it quanto no ambiente Github.
Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
no mínimo um arquivo de testes criado pelo próprio professor.'''

import os

#Functions
def line_to_array(line):
    values = []
    values = line.split(",")
    for i in range(len(values)):
        values[i] = values[i].strip()
    return values

#Union
def U(g1, g2):
    temp = g1.copy()
    for i in range(len(g2)):
        if g2[i] not in temp:
            temp.append(g2[i])
    return temp
    #return list(set(g1) | set(g2)) Wrong sorting!
    
#Intersection
def I(g1, g2):
    return list(set(g1) & set(g2))

#Difference
def D(g1,g2):
    temp = g1.copy()
    size = len(g2)
    for i in range(size):
        if g2[i] in temp:
            temp.remove(g2[i])
    return temp

#Cartesian
def C(g1,g2):
    temp = []
    for i in range(len(g1)):
        for j in range(len(g2)):
            element = "(" + g1[i] + "," + g2[j] + ")"
            temp.append(element)
    return temp
    
    
def print_group(g, header):
    print(header, end=" ")
    print("{", end="")
    #print(g)
    for i in range(len(g)):
        if i > 0:
            print(" ", end="")
        print(g[i], end="")
        if i < len(g) - 1:
            print(",", end="")
    print("}", end="")

filedir = "demofile.txt"
valid = False

while not valid:
    print("Bem-vindo! Por favor entre o nome do arquivo que contém as operações a serem realizadas! (sem incluir a extensão .txt)")
    print("P.S Um campo vazio carregará o arquivo \'demofile.txt\'")
    temp_input = str(input(">")).replace(" ","")
    if temp_input == "": #Check for Empty
            if os.path.isfile(filedir):
                valid = True
                break
            else:
                print("! Parece que o arquivo de leitura padrão \'" + "demofile.txt" + "\' foi removido.")
                print("! Por favor refira-se ao Readme para mais informações.")
    temp_input += ".txt"
    if os.path.isfile(temp_input):
        filedir = temp_input
        valid = True
    else:
        print("Error! Não foi possível encontrar o arquivo \'" + temp_input + "\'!")


f = open(filedir, "r")


print("Mostrando resultados para o arquivo \"" + filedir + "\"...")
#Treat lines
lines = []
lines = f.read().split("\n")

to_execute = int(lines.pop(0).strip())

remove_list = ['\n', ' ']
for l in range(len(lines)):
    lines[l] = lines[l].strip(' ')
    


#Logic Variables
i = 0
result_count = 0

#Operation Variables
operator = ""
group1 = []
group2 = []

while(i < len(lines) and result_count < to_execute):
    if operator == ""  and operator.capitalize() in "UIDC":
        operator = lines[i].capitalize()
    else:
        if len(group1) == 0:
            group1 = line_to_array(lines[i])
        else:
            group2 = line_to_array(lines[i])
            
        
    #Print
    if operator != "" and len(group1) > 0 and len(group2) > 0:
        
        operation = ""
        result = ['INVALID']
        
        match operator:
            case "U":
                operation = "União"
                result = U(group1, group2)
            case "I":
                operation = "Interseção"
                result = I(group1, group2)
            case "D":
                operation = "Diferença"
                result = D(group1, group2)
            case "C":
                operation = "Produto Cartesiano"
                result = C(group1, group2)
        
        #Print Results
        print(operation, end=": ")
        print_group(group1, "conjunto 1")
        print(", ", end="")
        print_group(group2, "conjunto 2")
        print_group(result, ". Resultado:")
        result_count += 1
        print() #Line Break
        
        #Do functions call here
        
        operator = ""
        group1 = []
        group2 = []
    i += 1