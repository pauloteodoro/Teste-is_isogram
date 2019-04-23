
def is_isogram(palavra) :                              #  função que fará a verificação da palavra.
    
    if palavra == "":                                  #  condiçional se palavra e vazia.
            return True                                #  retorna valor verdeiro caso string tiver vazia.

    elif palavra.isalpha() == False :                  #  condiçional caso a palavra contenha algum numero.
        return False

    elif palavra.isalpha() == True :                   #  condiçional caso a palavra não tenha nenhum numero
        aux = set(palavra)
        len(palavra)
        return len(palavra)==len(aux)                  #  Retorna True or false de acordo com a verificação de
                                                       #  letras repetidas.
   



        