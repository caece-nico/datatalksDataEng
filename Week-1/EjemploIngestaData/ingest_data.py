import pandas as pd
import time
from sqlalchemy import create_engine
import psycopg2
import argparse
import os


def main(parametros):
    
    user = parametros.user
    password = parametros.password
    db = parametros.db
    host = parametros.host
    port = parametros.port
    table_name = parametros.table_name
    url = parametros.url
    csv_name = parametros.csv_name


    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    engine.connect()

    os.system(f"wget {url}") # para ejecutar en Docker
    
    
    print('Bajo el archivo')
    
    # Para ejecutar en windows 
    #os.system('cp /d/Proyectos/datatalksDataEng/yellow_tripdata_2021-01.csv.gz yellow_tripdata_2021-01.csv.gz')
    # os.system(f"gunzip -f yellow_tripdata_2021-01.csv.gz")
    os.system("gzip -d yellow_tripdata_2021-01.csv.gz")
    

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    
    df = next(df_iter)


    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)



    df.to_sql(name=f"{table_name}", con=engine, if_exists='replace')


    while True:
        
        t_start = time.time()
        
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        try:
        
            df.to_sql(name=f'{table_name}', con=engine, if_exists='append', )
        except (Exception) as e:
            pass
        
        t_end = time.time()
        print('inserted another chunk..took %.3f' % (t_end - t_start))
        
        df = next(df_iter)
        
    
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Ingest CSV dato to Postgres')
    
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db',help='databsae name for postgres')
    parser.add_argument('--table_name', help='name of the table where to write the result')
    parser.add_argument('--url',help='url to .csv')
    parser.add_argument('--csv_name', help='Nombre del archivo')
    
    
    args = parser.parse_args()
    main(args)