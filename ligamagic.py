import csv

with open('C:\\File Path\\Spreadsheet.csv', mode = 'r', encoding = 'utf-8') as file: #Leitura do arquivo
    csv_reader = csv.reader(file, delimiter = ',') #Transformação do arquivo em uma lista
    for row in csv_reader: #Comando de loop para repetir a criação de lista para cada linha do arquivo (se adicionar a linha "print(row)", o terminal irá exibir cada linha como uma lista diferente)
        indice, nome_carta, idioma, quantidade, edicao, extras, numero, cor, qualidade, armazenamento = row #aqui, foram atribuídas uma variável para cada elemento da linha do arquivo, armazenando seus valores em cada uma respectiva
        if idioma == "BR": #Comando condicional para direcionar o nome da carta (nome_carta) para uma coluna diferente (entre PT e EN) dependendo de qual idioma compõe a carta
            cardpt = nome_carta
            carden = ""
        elif idioma == "EN":
            cardpt = ""
            carden = nome_carta
        elif idioma == "JP":
            cardpt = ""
            carden = nome_carta
        else:
            cardpt = nome_carta
            carden = ""
        print ('"",', '"",', '"', edicao, '",', '"', cardpt, '",', '"', carden, '",', '"', quantidade, '",', '"', qualidade, '",' '"', idioma, '",', '"",', '"', cor, '",', '"', extras, '",', '"', numero, '",', '""', sep="")
#Aqui foi registrado e exibido no terminal o modelo correto aceito pelo site para cada linha existente no arquivo ("", "", Edição(sigla), Nome da carta (PTBR), Nome da carta (EN), Quantidade, Qualidade (NM, SP, etc), Idioma (BR, EN, ES, FR, JP, etc), Cor (R, G, U, etc), Extras (Foil, etc), Número de identificação, "".)
#As linhas estavam exibindo incorretamente a formatação, adicionando um espaço entre cada separador, o comando 'sep' foi adicionado a fim de remover esses espaços e corrigir a formatação.
#Comando no CMD para transformar os valores em um arquivo separado: "cd + (caminho do arquivo)" > Enter > "py ligamagic.py > 'nome do novo arquivo'.csv"