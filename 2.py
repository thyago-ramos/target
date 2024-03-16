def questao_2(num_check):
    
    seq_fibonacci = [0, 1]
    indice = 0

    while(seq_fibonacci[indice] <= num_check):
        if(indice > 0):
            seq_fibonacci.append(seq_fibonacci[-1] + seq_fibonacci[-2])

        indice += 1

        
    if(num_check in seq_fibonacci):
        print("{} faz parte da sequencia".format(num_check))
    else:
        print("{} NAO faz parte da sequencia".format(num_check))

if __name__ == '__main__':
    questao_2(0)
    questao_2(1)
    questao_2(2)
    questao_2(9)
    questao_2(21)