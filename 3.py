def questao_3():
    
    print("a) Cada novo número é achado pela soma do número anterior com 2")

    val = 1
    for i in range(5):
        print(val)
        val += 2
    
    print("\nb) Cada novo número é achado multiplicando o número anterior por 2")

    val = 2
    for i in range(7):
        print(val)
        val *= 2
    
    print("\nc) A sequência é formada pelo quadrado de cada número natural")
    val = 0
    for i in range(8):
        print(val * val)
        val += 1

    print("\nd) A sequência é formada pelo quadrado de cada número natural par maior que 0")
    val = 2
    for i in range(5):
        print(val * val)
        val += 2

    print("\ne) O próximo número da sequência é a soma dos dois números antecedentes")
    val = 1
    val_anterior = 0
    for i in range(7):
        print(val)
        aux = val
        val = val + val_anterior
        val_anterior = aux

    print("\nf) A lógica não é númerica, mas linguística: apenas aparecem números cuja escrita por extenso começa com a letra D")
    print("2 - Dois")
    print("10 - Dez")
    print("12 - Doze")
    print("16 - Dezesseis")
    print("17 - Dezessete")
    print("18 - Dezoito")
    print("19 - Dezenove")
    print("200 - Duzentos")

if __name__ == '__main__':
    questao_3()