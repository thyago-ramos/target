def questao_5(palavra):
    tamanho = len(palavra)
    palavra_invertida = ""
    
    for i in range(tamanho - 1, -1, -1):
        palavra_invertida += palavra[i]

    print(palavra_invertida)

if __name__ == '__main__':
    questao_5("Target")