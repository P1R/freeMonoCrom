'''
Modulo  Movimiento Nanometros

@author: P1R0
'''
import serial, sys;
ser = serial.Serial(0,9600)
ser.cts = True
ser.dtr = True
ser.bytesize = 8
SxN = 59.71
##atributos dentro de objeto

#Funcion para inicializar Monocromador
def init():
        ser.flushOutput()
        ser.write(unicode("A\r\n"))
        echo()
        ser.write(unicode("0A\r\n"))
        echo()
        ser.write(unicode("A\r\n"))
        echo()
        ser.write(unicode("0A\r\n"))
        echo()
        ser.write(unicode("0R\r\n"))
        echo()
        ser.write(unicode("0U1\r\n"))
        echo()
        ser.write(unicode("0V1\r\n"))
        echo()
        ser.write(unicode("0T400\r\n"))
        echo()
        ser.write(unicode("0K1\r\n"))
        echo()
        ser.write(unicode("0Y1\r\n"))
        echo()
        ser.write(unicode("0Y0\r\n"))
        echo()
        ser.write(unicode("0K0\r\n"))
        echo()
        ser.write(unicode("0V1\r\n"))
        echo()
        ser.write(unicode("0T1000\r\n"))
        echo()
        ser.write(unicode("0F-\r\n"))
        echo()
        ser.write(unicode("0V1\r\n"))
        echo()
        ser.write(unicode("0T400\r\n"))
        echo()
        ser.write(unicode("0K1\r\n"))
        echo()
        ser.write(unicode("0V1\r\n"))
        echo()
        ser.write(unicode("0T4000\r\n"))
        echo()
        ser.write(unicode("0K0\r\n"))
        echo()
        ser.write(unicode("0M99999\r\n"))
        echo()
        ser.write(unicode("0K1\r\n"))
        echo()
        ser.write(unicode("0V1\r\n"))
        echo()
        ser.write(unicode("0T400\r\n"))
        echo()
        ser.write(unicode("0M-3925\r\n")) #en la posicion cero
        echo()
        return 0
#funcion para aproximar errores    
def Error(x):
    Y = [0,
         0.010373807,
         -0.05124284,
         -0.227092782,
         -0.572418858,
         -1.150211522,
         -2.019461229,
         -3.247663205,
         -4.904050745,
         -7.062119076,
         -9.803353877,
         -13.21724083,
         -17.39877039,
         -22.45717585,
         -28.51818573,
         -35.71928571,
         -44.22644716,
         -54.22539859,
         -65.94810183,
         -79.66102345,
         95.70661095,
         -114.4980595,
         -136.5895354,
         -162.693691,
         -193.8151306,
         -231.3914014,
         -277.6754313,
         -336.5191712,
         -415.6610186,
         -536.5034235,
         -763.8268297,
         -804.7677106];
    X = [0,
         50.002,
         99.999,
         149.999,
         199.997,
         249.997,
         300.007,
         349.993,
         400.003,
         449.997,
         499.994,
         550.005,
         600.002,
         649.993,
         700.003,
         749.995,
         800.004,
         849.995,
         900.004,
         949.999,
         1000.006,
         1049.997,
         1100.004,
         1150.001,
         1200.005,
         1250.002,
         1300,
         1349.999,
         1399.998,
         449.998,
         1490,
         1492];
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
#funcion para calcular y mover el motor
def Calcula(Nm,LastPos):
    if((Nm < 1) or (Nm > 1491)):
        ser.close();
        sys.exit(0);
    Er=Error(Nm);
    NmyEr = Nm - Er;
    uS = NmyEr * SxN;
    dif = uS - int(uS);
    if dif > 0.5:
        uS = int(uS) + 1;
    else:
        uS = int(uS);
    Mover = uS - LastPos;
    print "La diferencia a mover es: %d" % Mover;
    Mueve(Mover);
    LastPos = uS;
    return LastPos 
#Funcion para llamar al eco del serial
def echo():
    line = ser.readline()
    print line    
#Funcion para mover el motor
def Mueve(Mover):
    ##mover Full Step cuando recibe como parametros microSteps 
    MoverFS = ((Mover-3) / 5);
    ser.flushOutput();
    ser.write(unicode("0U0\r\n"));
    echo();
    ser.write(unicode("0V1\r\n"));
    echo();
    ser.write(unicode("0T1000\r\n"));
    echo();
    ser.write(unicode("0M%d\r\n" % MoverFS));
    echo();
    ser.write(unicode("0U1\r\n"));
    echo();
    ser.write(unicode("0V1\r\n"));
    echo();
    ser.write(unicode("0T400\r\n"));
    echo();
    ##ultimos 3 microsteps para una aproximacion mas suave.
    ser.write(unicode("0M3\r\n"));
    echo();
    return 0;
    
N = 0;
LastPos = 0;
init();
while 1:
    while type(N)!= float:
        try:
            N = raw_input("Ingresa Nanometros o quit para cerrar:");
            if N == "quit":
                ser.close();
                sys.exit(0);
            N = float(N);
        except (ValueError, TypeError):
            print "error, el valor debe ser entero o flotante";
    LastPos = Calcula(N,LastPos);
    print "los microspasos totales son: %d" % LastPos;
    N=0

