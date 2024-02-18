# Introducción al TP de la Semana.

1. [Origen de los datos](#1.-origen-de-los-datos)


# 1. Origen de los datos

El origen de los datos es el sitio 

[NEW YORK DATA](https://www.nyc.gov/)

Los datasets se pueden encontrar en:

[LINK DATASETS](https://www.nyc.gov/)

donde todos tiene la misma estructura de URL:

```
https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet
```

+ TIPO_TAXI
+ ANIO
+ MES

Para descargar estos datasets usamos un script .bash __/code/download.sh__

## Como se ejecuta este script?

Desde la linea de comando hacemos

```shell
./download_data.sh yellow 2021
```

