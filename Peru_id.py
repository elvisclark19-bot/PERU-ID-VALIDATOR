def validar_dni(dni: str) -> bool:
    return len(dni) == 8 and dni.isdigit()

def validar_ruc(ruc: str) -> bool:
    if len(ruc) != 11 or not ruc.isdigit():
        return False
    pesos = [5,4,3,2,7,6,5,4,3,2]
    suma = sum(int(ruc[i]) * pesos[i] for i in range(10))
    resto = 11 - (suma % 11)
    if resto == 11: resto = 1
    if resto == 10: resto = 0
    return resto == int(ruc[10])
