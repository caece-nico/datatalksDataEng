# Desarrollamos el mismo proyecto que Week 1 pero usando Docker Compose.

1. Creacion de Docker Compose

```yaml
services:
  pgdatabase:
    build: /Postgres
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxy
    volumes:
      - "./volumen_postgres/:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"
```

2. Ejecución de Docker-Compose

Ejecución en modo dettach

```shell
docker-compose up -d
```

Detenemos la ejecución.

````shell
docker-compose down
```