'''
Modulo  Movimiento Nanometros

@author: P1R0
'''
##atributos dentro de objeto

def metodo(x):
    f = i = 0;
    '''
    Y = [[0,0],
         [597,1],
         [597,4],
         [599,1],
         [601,1],
         [604,0],
         [607,3],
         [611,3],
         [617,0],
         [622,4],
         [629,4],
         [638,0],
         [647,0],
         [657,2],
         [669,3],
         [683,0],
         [698,4],
         [716,2],
         [737,1],
         [760,4],
         [788,4],
         [821,2],
         [861,0],
         [908,4],
         [968,4],
         [1045,4],
         [1149,4],
         [1299,4],
         [1542,1],
         [2040,1],
         [3707,1]]; '''
    Y = [0,
         597,
         597,
         599,
         601,
         604,
         607,
         611,
         617,
         622,
         629,
         638,
         647,
         657,
         669,
         683,
         698,
         716,
         737,
         760,
         788,
         821,
         861,
         908,
         968,
         1045,
         1149,
         1299,
         1542,
         2040,
         3707];
    X = [0.0,
         50,
         100.0,
         150.0,
         200.0,
         250.0,
         300.0,
         350.0,
         400.0,
         450.0,
         500.0,
         550.0,
         600.0,
         650.0,
         700.0,
         750.0,
         800.0,
         850.0,
         900.0,
         950.0,
         1000.0,
         1050.0,
         1100.0,
         1150.0,
         1200.0,
         1250.0,
         1300.0,
         1350.0,
         1400.0,
         1450.0,
         1492.0];
    
    while x > X[i]:
        x0=X[i];
        y0=Y[i];
        x1=X[i+1];
        y1=Y[i+1];
        ''' metodo'''
        r=y1-y0;
        d=r/(x1-x0);
        y=y0+(d*(x-x0));
        f=f+y1
        i+=1;
    
    return (5*f)

def calcula():
    lastpos = 0
    actualpos = 0
    carry = 0 
    
'''
    if (carry == 1):
        carry = 0
        y-=1
         
    if((y-int(y))>0.5):
        y+=1
        carry = 1
'''

N = raw_input( "Ingresa Nanometros:");
N = int(N);
print "el motor se mueve %d halfsteps" % metodo(N);
raw_input()