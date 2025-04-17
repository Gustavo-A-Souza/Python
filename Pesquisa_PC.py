import tkinter as tk
from tkinter import filedialog

def calcular_media_arquivo():
    # Cria a janela oculta do tkinter
    root = tk.Tk()
    root.withdraw()

    # Abre o diálogo para selecionar o arquivo
    arquivo = filedialog.askopenfilename(title="Selecione o arquivo com os números")

    if not arquivo:
        print("Nenhum arquivo selecionado.")
        return

    numeros = []

    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                # Tenta extrair todos os números da linha (separados por espaço ou vírgulas)
                partes = linha.replace(',', ' ').split()
                for parte in partes:
                    try:
                        numeros.append(float(parte))
                    except ValueError:
                        pass  # Ignora valores não numéricos

        if numeros:
            media = sum(numeros) / len(numeros)
            print(f"Média dos números: {media}")
        else:
            print("Nenhum número válido encontrado no arquivo.")

    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

# Executa a função
calcular_media_arquivo()