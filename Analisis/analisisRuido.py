import pandas as pd 

from generators.generadorDecibelios import generarDatosRuido
def construirDataRuido():
    #creando un dataFrame 
    datosRuido=generarDatosRuido()
    ruidoDataFrame=pd.DataFrame(datosRuido,columns=["id,nivelRuido,comuna"])
    ruidoDataFrame.to_csv("ruido.csv",index=False)
 
    
construirDataRuido()