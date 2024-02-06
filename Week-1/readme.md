# Primer semana de curso.

1. [Refrsh rápido](#1.-refresh-rapido)
2. [Creacion del entorno](#2.-creacion-del-entorno)
3. [creacion del entorno con python-entrypoint](#3.-creacion-del-entorno-con-python-entrypoint)
4. [Cargar datos en Postgres](#4.-cargar-datos-en-postgres)
5. [Bajar un archivo usando Shell](#5.-bajar-un-archivo-usando-shell)
6. [Primer ETL usando PANDAS](#6.-primer-etl-usando-pandas)
7. [Ingesting data into Docker](#7.-ingesting-data-into-docker)

7.  [Otros](#problemas-de-memoria)
    * [Creacion de un entorno virtual](#creacion-y-activacion-de-un-entorno-virtual)
    * [Instalar PgAdmin y Red en Docker](#instalar-pgadmin-y-red-en-docker)
    * [Redes con Docker-Compose](#redes-con-docker-compose)

8. [Ejecucion del proyecto desde localhost](#8.-ejecucion-del-proyecto-desde-localhost)


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


## 7. Ingesting data inot Docker.

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

## Instalar PgAdmin y Red en Docker

1. Para instalar un contenedor con PgAdmin vamos a usar una imagen ya existente en el repo de Docker.

__dpage/pgadmin4__

+ Descargamos la imagen

```
docker pull dpage/pgadmin4
```

+ Una vez creada la imagen, inciamos el contenedor.

```
docker run -t -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 dpage/pgadmin4
```

Una vez iniciado el _contenedor_ podemos entrar a 

__localhost:8080_ pero no podremos crear una conexión con postgres porque al poner _localhost_ en pgadmin busca dentro del container cuando en realidad deberiamos buscar la _ip del container de postgres_ para conectar__

### Creación de una RED entre contenedores.

[Tutorial de creacion de networks en docker](https://docs.docker.com/engine/reference/commandline/network_create/)
[Video de DataTalks de creacion de networks](https://www.youtube.com/watch?v=tOr4hTsHOzU&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)

1. creamos una red

```
docker network create pg-network
```

2. Ejecutamos el primer contenedor especificando la red

+ postgres

_Especificar __network__ y __name___

```
docker run -t -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root"  -e POSTGRES_DB="ny_taxi" -v D:/Proyectos/datatalksDataEng/Week-1/ny_postgres_postgres_data:/var/lib/postgresql/data -p 5432:5432 --network=pg-network --name=pg-database postgres:13
```

+ pgadmin

_Especificar __network__ y __name___


```
docker run -t -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" -e PGADMIN_DEFAULT_PASSWORD="root" -p 8080:80 --network pg-network --name=pdadmin dpage/pgadmin4
```

Ahora podemos crear una conexion usando el nombre de la conexón de postgres __pg-database__

**UN MEJOR ENFOQUE ES USAR DOCKER COMPOSE**


## Redes con Docker-Compose

```
Igual que el ejemplo anterior pero suando Docker-Compose.
```

## 8. Ejecucion del proyecto desde localhost

```
Para probar que el script de python funciona lo vamos a probar desde nuestro -venv local antes de subirlo a docker.
```

Para esto debemos tener levantados los contenedores de postgres y pgadmin en red
LUego en otro terminar ejecutar:

```cmd
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"


python ingest_data.py \
--user=root \
--password=root \
--host=localhost \
--port=5432 \
--db=ny_taxi \
--table_name=yellow_taxi_ny \
--url=${URL} \
--csv_name=yellow_tripdata_2021-01.csv
```

Para esta prueba tenemos el archivo .csv.gz local porque desde la terminal no funciona __wget__
pero cuando lo pasamos descomentamos esa linea.


## Para Ejecutar en Docker.

1. COnstruimos la imagen

```
docker build -t taxi_ingest:v001 .
```

2. Ejecutamos con todos los comandos.

```
docker run -t 
```

URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"


docker run -t --network=pg-network taxi_ingest:v001 \
--user=root \
--password=root \
--host=pg-database \
--port=5432 \
--db=ny_taxi \
--table_name=yellow_taxi_ny \
--url=${URL} \
--csv_name=yellow_tripdata_2021-01.csv

**IMPORTANTE** El contenedor de python debe estar en la misma red.