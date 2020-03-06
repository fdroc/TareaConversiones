def test_convertirABaseDiez():
    assert convertirABaseDiez(20,8)==16
    assert convertirABaseDiez(30,7)==21
    print("pruebas exitosas")

def test_convertirABaseTal():
    assert convertirABaseTal(220,5)==1340
    print("bien")

def cd_cola(n):
    return cd_aux (n, 1)
def cd_aux(n, respuesta):
    if n<10:
        return respuesta
    else:
        return cd_aux(n//10, respuesta+1)

def convertirABaseDiez(n, b):
    if n<10:
        return n
    else:
        return convertirABaseDiez(n%10**(cd_cola(n)-1), b)+ (n//10**(cd_cola(n)-1)*b**(cd_cola(n)-1))

def convertirABaseTal(n, b):
    return convertirABaseTal_aux (n, b, 0)

def convertirABaseTal_aux (n, b, z):
    if n//b==0: 
        return z+n%b*10**(cd_cola(z))
    else: 
        return convertirABaseTal_aux (n//b, b, z+n%b*10**(cd_cola(z)))

test_convertirABaseDiez()

test_convertirABaseTal()