# Primer semana de curso.

1. [Refrsh rápido](#1.-refresh-rapido)
2. [Creacion del entorno](#2.-creacion-del-entorno)
3. [creacion del entorno con python-entrypoint](#3.-creacion-del-entorno-con-python-entrypoint)
4. [Cargar datos en Postgres](#4.-cargar-datos-en-postgres)
5. [Bajar un archivo usando Shell](#5.-bajar-un-archivo-usando-shell)
6. [Primer ETL usando PANDAS](#6.-primer-etl-usando-pandas)

    [Otros](#problemas-de-memoria)
    [Creacion de un entorno virtual](#creacion-y-activacion-de-un-entorno-virtual)

## 1. Refresh rapido

### Ejemplo para ejecutar una imagen en modo interactivo.

Previamente creamos una imagen de python simple sin nada instalado.

```bash
docker run -it python:3.9
```

Al ejecutar el contenedor vemos que no tiene pandas, se lo podemos instalar para eso debemos salir y hacemos:

```bash
docker run -it entrypoint=bash python:3.9
```

Una vez dentro del container hacemos

```
pip install pandas
```

Ahora tenemos pandas. Pero cuando salimos del contenedor y lo inciamos otra vez el mismo toma la imagen base y estará vacio.

## 2. Creacion del entorno

```docker
FROM python:3.9

WORKDIR/app

COPY pipeline.py pipeline.py

RUN pip install pandas

ENTRYPOINT [ "bash" ]
```

+ Para ejecutarla en modo test

 1. _nombre de la imagen_ test 

2. _label_ pandas

```cmd
docker build test:pandas .
```

+ Ejecución de la imagen

```cmd
docker run -it test:pandas
```

## 3. Creacion del entorno con Python Entrypoint

+ Es similar al paso 2 pero ahora le vamos a decir que queremos ejecutar el archivo _pipeline.py_ cuando corremos el contenedor pidiendo un _input_

```docker
docker run -i python:entrypoint 2023-01-04
```

_IMPORTANTE_ no usamos _-it_ porque puede dar error. Se reemplaza por _-i_


## 4. Cargar datos en Postgres


1. ¿Cómo pasar variables en _docker run_?

```
docker run -t -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root"  -e POSTGRES_DB="ny_taxi" -v D:/Proyectos/datatalksDataEng/Week-1/ny_postgres_postgres_data:/var/lib/postgresql/data -p 5432:5432 postgres:13
```

2. filesystem -> Postgers necesita guardar los datos en un _voumen_

2. ¿Cómo nos logeamos en la bd sin usar _dbeaver_?

```
desde la linea de comando usamos pgcli.
python.exe -m pip install --upgrade pip
pip install pgcli
```

```bash
pgcli -h localhost -p 5432 -u root -d ny_taxi
```

[Solucion de problemas con pgcli](https://youtu.be/3IkfkTwqHx4?si=mZBePAmvRUuXYlsM)

## 5. Bajar un archivo usando Shell


```bash
wget https://s3..../yellow_tripdata_2021-01.csv
```
si no funciona usamos _curl_

```
curl https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz 
```

```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz 
```

wget -P D://Proyectos//datatalksDataEng//Week-1// https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz 

*IMPORTANTE* para este curso ya no se usa .csv todos los archivos están en _PARQUET_ asique los bajamos del repo de git.

## Copiar el archivo y descomprimirlo

```
cp /ruta/archivo /ruta/
gunzip archivo
```

_para ver el archivo_

```
less archivo.csv
```
_para ver los primero 100_

```
head -n 100 archivo.csv
```

_guardar los primero 10 registros en otro archivo_

```shell
head -n 10 archivo.csv > otro_archivo.csv
```

_contar numero de lineas en el archivo_
+ wc es word count
+ l indica lineas

```shell
wc -l archivo.csv
```

## 6. Primer ETL usando Pandas.

```
En este primer Ejemplo vamos a cargar una tabla en postgres usnado el archivo descargado y pandas en chunks.
```

[ver notebook](Week-1\quersPostgresJupyter.ipynb)

## Problemas de memoria.

```
Simply set up memory limit for WSL2:

close docker desktop
execute wsl --shutdown
add following to %UserProfile%\.wslconfig file (create one if there is none):
[wsl2]
memory=2GB
restart docker desktop
Of course you can change 2GB to whatever you like.
```

## Creacion y activacion de un entorno virtual

```shell
python -m venv mi_entorno_virtual
\mi_entorno_virtual\scrpts\activate #desde windows
. /mi_entorno_virtual/scripts/activate #desde git
code .
```