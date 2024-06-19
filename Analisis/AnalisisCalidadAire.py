import pandas as pd 
import matplotlib.pyplot as plt

from generators.generatorICA import generarDatosICA
def construirDataICA():
    #creando un dataFrame 
    datosICA=generarDatosICA()
    dataFrameICA=pd.DataFrame(datosICA,columns=["comuna","ica","fecha","id"])
    dataFrameICA.to_csv("datosica.csv",index=False)
    print(dataFrameICA)


# generando gráfica de los datos por comuna    
    datosOrdenadosPorcomuna=dataFrameICA.groupby("comuna")["ica"].mean()
    plt.figure(figsize=(20,20))
    datosOrdenadosPorcomuna.plot(kind="bar",color="green")
    plt.show()
construirDataICA() 