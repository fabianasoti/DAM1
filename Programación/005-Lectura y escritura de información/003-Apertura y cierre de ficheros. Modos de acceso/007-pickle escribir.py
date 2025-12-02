# pip3 install pickle | pip install pickle
import pickle

archivo = open("datos.bin", "wb")
cadena =  "Fabiana"

pickle.dump(cadena, archivo)

archivo.close()
