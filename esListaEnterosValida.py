def esListaEnterosValida(lista):
    """test todo dato es tipo <int>"""
    if not lista: return True
    if type(lista[0]) != type(11):
        return False
    else:
        return True and esListaEnterosValida(lista[1:])

if __name__ == "__main__":

    presunta = [11,22,33]       # True
    presunta = [11,"piedra",33] # False 
    presunta = [11,22,"piedra"] # False
    presunta = ["piedra",22,33] # False
    presunta = ["piedra"] # False
    presunta = [11] # True
    presunta = []   # True

    print(esListaEnterosValida(presunta))



