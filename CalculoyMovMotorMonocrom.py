'''
Modulo  Movimiento Nanometros

@author: P1R0
'''
    
def metodo(x):
    Y = [0.0,
    1195.0,
    1200.0,
    1211.0,
    1228.0,
    1252.0,
    1285.0,
    1327.0,
    1381.0,
    1453.0,
    1549.0,
    1682.0,
    1877.0,
    2195.0,
    2842.0,
    5747.0];
    X = [0.0,
    100.0,
    200.0,
    300.0,
    400.0,
    500.0,
    600.0,
    700.0,
    800.0,
    900.0,
    1000.0,
    1100.0,
    1200.0,
    1300.0,
    1400.0,
    1492.0];
    i = 0;
    while x > X[i]:
        x0=X[i];
        y0=Y[i];
        x1=X[i+1];
        y1=Y[i+1];
        i=i+1;
    r=y1-y0;
    d=r/(x1-x0);
    y=y0+(d*(x-x0));
    return y

N = raw_input( "Ingresa Nanometros:");
N = float(N);
print "el error es de %f" % metodo(N);
raw_input()
