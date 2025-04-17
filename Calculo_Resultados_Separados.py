# Caminhos dos arquivos (ajuste o caminho conforme sua máquina)
entrada = open(r"C:\Users\Aluno\Desktop\python\notas.txt", "r")
saida = open(r"C:\Users\Aluno\Desktop\python\medias.txt", "w")

# Lê a primeira linha do arquivo
linha = entrada.readline()

# Enquanto a linha não for vazia
while len(linha.strip()) > 0:
    # Divide a linha pelas ;
    partes = linha.strip().split(";")
    
    # Converte as partes para float
    nota1 = float(partes[0])
    nota2 = float(partes[1])
    nota3 = float(partes[2])
    
    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3
    
    # Cria uma nova linha com as notas e a média
    nova_linha = f"{nota1};{nota2};{nota3};{media:.2f}\n"
    
    # Escreve no arquivo de saída
    saida.write(nova_linha)
    
    # Lê a próxima linha
    linha = entrada.readline()

# Fecha os arquivos
entrada.close()
saida.close()