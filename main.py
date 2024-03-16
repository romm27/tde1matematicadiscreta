import os

#Functions
def line_to_array(line):
    values = []
    values = line.split(",")
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
    for c in range(len(remove_list)):
        lines[l] = lines[l].replace(remove_list[c], "")
    


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