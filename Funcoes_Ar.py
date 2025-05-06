#Funções para cálculo do arquivo:

def funcaoCalculoAr(IInicial, IFinal, CInicial, CFinal, CCalc):

    return IInicial + ((IFinal - IInicial)/(CFinal - CInicial)) * (CCalc - CInicial)
    
def gasPM10(CCalculado):
            
    match CCalculado:

        case CCalculado if 0 < CCalculado <= 45:
            return funcaoCalculoAr(0, 40, 0, 45, CCalculado)

        case CCalculado if 45 < CCalculado <= 100:
            return funcaoCalculoAr(41, 80, 46, 100, CCalculado)  

        case CCalculado if 100 < CCalculado <= 150:
            return funcaoCalculoAr(81, 120, 101, 150, CCalculado)


        case CCalculado if 150 < CCalculado <= 250:
            return funcaoCalculoAr(121, 200, 151, 250, CCalculado)
                    

        case CCalculado if 250 < CCalculado <= 600:
            return funcaoCalculoAr(201, 400, 251, 600, CCalculado)

def gasPM2_5(CCalculado):
    
    match CCalculado:
        case CCalculado if 0 < CCalculado <= 15:
            return funcaoCalculoAr(0, 40, 0, 15, CCalculado)

        case CCalculado if 15 < CCalculado <= 50:
            return funcaoCalculoAr(41, 80 ,16, 50, CCalculado)  

        case CCalculado if 50 < CCalculado <= 75:
            return funcaoCalculoAr(81, 120, 51, 75, CCalculado)


        case CCalculado if 75 < CCalculado <= 125:
            return funcaoCalculoAr(121, 200, 76, 125, CCalculado)
                    

        case CCalculado if 125 < CCalculado <= 300:
            return funcaoCalculoAr(201, 400, 126, 300, CCalculado)


def gasNO2(CCalculado):

    match CCalculado:
        case CCalculado if 0 < CCalculado <= 200:
            return funcaoCalculoAr(0, 40, 0, 200, CCalculado)

        case CCalculado if 200 < CCalculado <= 240:
            return funcaoCalculoAr(41, 80, 201, 240, CCalculado)  

        case CCalculado if 240 < CCalculado <= 320:
            return funcaoCalculoAr(81, 120, 241, 320, CCalculado)


        case CCalculado if 320 < CCalculado <= 1130:
            return funcaoCalculoAr(121, 200, 321, 1130, CCalculado)
                    

        case CCalculado if 1130 < CCalculado <= 3750:
            return funcaoCalculoAr(201, 400, 1130, 3750, CCalculado)

def gasSO2(CCalculado):

    match CCalculado:

        case CCalculado if 0 < CCalculado <= 40:
            return funcaoCalculoAr(0, 40, 0, 40, CCalculado)

        case CCalculado if 40 < CCalculado <= 50:
            return funcaoCalculoAr(41, 80, 41, 50, CCalculado)  

        case CCalculado if 50 < CCalculado <= 125:
            return funcaoCalculoAr(81, 120, 51, 125, CCalculado)


        case CCalculado if 125 < CCalculado <= 800:
            return funcaoCalculoAr(121, 200, 126, 800, CCalculado)
                    

        case CCalculado if 800 < CCalculado <= 2620:
            return funcaoCalculoAr(201, 400, 801, 2620, CCalculado)

def gasCO(CCalculado):

    match CCalculado:

        case CCalculado if 0 < CCalculado <= 9:
            return funcaoCalculoAr(0, 40, 0, 9, CCalculado)

        case CCalculado if 9 < CCalculado <= 11:
            return funcaoCalculoAr(41, 80, 10, 11, CCalculado)  

        case CCalculado if 11 < CCalculado <= 13:
            return funcaoCalculoAr(81, 120, 12, 13, CCalculado)


        case CCalculado if 13 < CCalculado <= 15:
            return funcaoCalculoAr(121, 200, 14, 15, CCalculado)
                    

        case CCalculado if 15 < CCalculado <= 50:
            return funcaoCalculoAr(201, 400, 16, 50, CCalculado)

        

    

    
    

    
    


#print(calculoTaxaDoAr(210, "PM10"))

        
