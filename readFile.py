## Importamos las dependencias de pandas y os
import pandas as pd
import os
import csv
import urllib3

## Declaramos varibale global
_MAIN_PATH = ""

def _init():
    # Lectura de archivos de manera normal

    _filename = ""
    _full_path = os.path.join(_MAIN_PATH, _filename)

    # Se obtiene los datos que tiene el archivo CSV
    _data = pd.read_csv(_full_name)

    # Impriminos los datos del archivo
    print(_data.head())
    
    # Termina, Lectura de archivos de manera normal


    # Lectura de archivos csv separados, cabecara y body del archivo

    ############## SE OBNTIENE EL ARCHIVO DE CABECERA ############

    _data_columns = pd.read_csv(_MAIN_PATH, "/filename")
    _data_col_list = _data_columns['Column_name'].tolist()

    _data_f2 = pd.read_csv(_fullname, header = None, _data_col_list)

    print(_data_f2.columns.values)

    
    ### METODO DE LECTURA DE ARCHIVOS CON OPEN SOURCE ###
    _date3 = open(_fullname, "r")
    _cols = _data3.readLine().strip().split(",")
    _n_cols = len(_cols)

    _counter = 0
    _main_dict = {}

    for _col in _cols:
        _main_dict[col] = []

    for _line in _date3:
        _values = line.strip().split(",")
        for _i in range(len(_cols)):
            _main_dict[_cols[_i]].append(_values[_i])
        _counter += 1

    print ("El data set tiene %d filas y %d columnas"%(_counter, _n_cols))
    
    # Convierte a tipo de dataframe
    df3 = pd.DataFrame(_main_dict)
    print(df3.head())



    #### LEER Y ESCRIBIR EN UN FICHERO EN PYTHON

    _infile = _MAIN_PATH + "/" + "filetest.txt"
    _outfile = _MAIN_PATH + "/" + "filetest1.txt"
    
    with open(_infile , "r") as infile1:
        with open(_outfile, "w") as outfile1:
            for _line in infile1:
                fields = line.split(",");
                outfile.write("\t".join(fields))
                outfile.write("\n")


    df4 = pd.read_csv(_outfile, sep = "/t")
    print (df4.head())


    ### LEER DATOS DESDE UNA URL
    
    _modals_url = "url"
    _modals_data = pd.read_csv(_modals_url)
    print (_modals_data.head())

    _http = urllib3.PoolManager()
    _r = http.request("GET", _modals_url)
    print("El estado d e la respuesta es %d"%(_r.status))
    _response = _r.data
    
    # El objeto response contiene un string binario, asi que lo convertimos a un string decodificado 
    _str_data = _response.decode('utf-8')

    # Dividimos el string en un array de filas 
    _lineas = _str_data.split("\n")

    # La primera fila contiene la cabecera,
    _col_names = _lineas[0].split(",")
    _n_cols = len(_col_names)

    # Generamos un diccionario
    _counter = 0
    _main_dict = {}
    for col in _col_names
        _main_dict[col] = []

    #
    for line in _lineas:
        # Nos saltamos la primera linea que es la que contiene la  cabecera    
        if(_counter > 0):
            # Dividimos cada string por las comas como elemento separador
            values = line.strip().split(",")
            # Añadimos cada valor a su respectiva columan del diccionario
            for _i in range(len(_col_names))
                _main_dict[_col_names[_i]].append(values[_i])
        _counter += 1

    print ("el data set tiene %d filas y %d columans"%(_counter, _n_cols))

    # Convertimos el diccionario procesado a data frame y comprobamos que los datos son correctos
    _medals_df = pd.DataFrame(_main_dict)
    print(_medals_df.head())


    ### FICHEROS XLS Y XLSX

    _filename = _MAIN_PATH + "/" + "titanic.xls"

    _titanic2 = pd.read_excel(_filename , "titanic")

    # Guardar archivos excel
    _titanic2.to_excel(_MAIN_PATH, + "/fileexcel2.xls")

    

## Verifica si el el main
if __name__ == "__main__":
    ## Iniciando funcion init
    print("Iniciando python")
    
    _init()


## Termina
