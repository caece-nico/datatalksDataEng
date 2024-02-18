set -e

TAXI_TYPE=$1 #"yellow"
YEAR=$2 #2020

URL_PREFIX="https://d37ci6vzurychx.cloudfront.net/trip-data"

for MONTH in {1..12}; do
    FMONTH=`printf "%02d" ${MONTH}`
    #echo ${FMONTH}

    URL="${URL_PREFIX}/${TAXI_TYPE}_tripdata_${YEAR}-${FMONTH}.parquet"

    #echo ${URL}

    LOCAL_PREFIX="../data/raw/${TAXI_TYPE}/${YEAR}/${FMONTH}"
    LOCAL_PFILE="${TAXI_TYPE}_${YEAR}_${FMONTH}.parquet"
    LOCAL_PATH="${LOCAL_PREFIX}/${LOCAL_PFILE}"
    #echo ${LOCAL_PATH}

    wget ${URL} -P ${LOCAL_PATH}

    #gzip ${LOCAL_PATH}

done