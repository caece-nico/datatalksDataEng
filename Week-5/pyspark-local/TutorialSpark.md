# Tutorial Batch Processing

1. [Introducción a Batch Processing](#1.-Introduccion-a-batch-processing)
2. [Intro a Apache Spark](#2.-introduccion-a-apache-spark)
    - [INstalar jupyter Notebooks](#.-instalar-jupyter-notebooks)
3. [Data de ejemplo](#3.-dataos-de-ejemplo)


## 1. Introduccion a Batch Processing

```
Hay dos formas de procesamiento de datos.
1. Batch
2. Streaming
```

El procesamiento _batch_ se refiere a procesar grandes cantidades de datos _chuncks_ de una vez.
Por otro lado el procesamiento _streaming_ procesa menos cantidades de datos pero de forma continua, consumiendo _eventos_ que son generados por un _publicador_ hacia un _consumidor_

Un proceso Batch generalemnte procesa datos con distinta granularidad. Las más comunes son Diaria, Semanal o por cada n horas.


|Tecnologias mas usadas.|
|-----------------------|
|Python Scripts|
|SQL|
|Spark|
|Flink|

Estos procesos pueden ejecutarse sobre distintas plataformas como _kubernetes_, _aws_ y son orquestados con _airflow_

```
Una ventaja del proceso Batch es que se le puede pedir al motor de orquestación repetir un batch si ocurre un suceso. Esto no es posible en Streaming.
```

Una desventaja es el Delay o el tiempo de ejecución entre Batch.



## 2. Introduccion a Apache Spark

```
Spark es un Motor de procesamiento distribuido en varios clusters (Data Processing Engine)
```

El principal uso de Spark es _Batch Jobs_ pero tambien se puede usar para _Streaming_.

Normalmente usamos Spark cuando nuestra data está en un _datalake_ como _S3/GCP(parquet)_ y queremos volver a escribirlo en un _datalake_


**Si podemos expresar algo en SQL lo usamos, sinó usamos Spark**

### Instalar Jupyter Notebooks

Para poder instalar __Jupyter Notebooks__ debemos tener actualizado Ubuntu y lugo instalar Python3 pip

```shell
sudo apt-get update
sudo apt-get install python3-pip
```
+ Luego instalamos el Kernel

```shell
/bin/python3 -m pip install ipykernel -U --user --force-reinstall
```

## 3. Datos de ejemplo

