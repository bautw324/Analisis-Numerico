def f(x):
    return x**2 + 3*x - 6

def biseccion(a,b,err,max_i):
    x = (a+b)/2
    # Caso base
    if -err < f(x) < err or max_i<0: 
        return x
    # Opciones
    if f(x) > 0:
        x = biseccion(a,x,err,max_i-1)
    elif f(x) < 0:
        x = biseccion(x,b,err,max_i-1)
    return x

print('x ≈ ',biseccion(0,3,0.01,10))