# Creación de un Entorno en GCP

1. [Introducción](#1.-introducción)
2. [Creación del entorno GCP](#4.-creacion-del-entorno-gcp)
    - [Creacion de VM](#.-creacion-de-vm)
    - [Instalacion de Anaconda](#.-instalacion-de-anaconda)
    - [Instalacion de Docker](#.-instalacon-de-docker)
    - [Instalar gcloud y gsutil](#.-gcloud-y-gsutil)
    - [Crear una sesión con permisos gcloud](#.-gcloud-y-gsutil)
    


## 1. Introducción

Primero es necesario crar una clave shh para poder conectarnos a los servicios de GCP.

[Creacion clave ssh](https://cloud.google.com/compute/docs/connect/create-ssh-keys?hl=es-419)


```
generate ssh key

add it to metadata

HOST de-mio
    HotName: IP
    User nlealiapp
    IdentifyFile C:/users/leali/.ssh/gcp
```

_gcp_ es el nombre que yo decido ponerle al .shh de google

```bash
 ssh-keygen -t rsa -f gcp -C nlealiapp -b 2048
```

### Poner la clave en gcp

metadeta -> ssh key

```
cat gcp.pub #copiar y pegar.
```

### Cómo logearme a una VM de google

```
ssh -i gcp nlealiapp@34.134.173.41 #la ip la sacamos de la consola de gcp cuando se crea la imagen de la VM
```

nlealiapp es el usuario que usamos para creala

### Comandos básicos dentro de la VM

- htop para ver uqe maquina tenemos
- gcloud --version 


## 2. Instalacion de Anaconda.

[Link a aanaconda para linux](https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh)


```
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
```

Lo escribimos en la VM y luego de la descarga instalamos anaconda.

```
bash Anaconda ...
```

## En nuestro GITBASH LOCAL creamos un archivo config para configurar nuestro .ssh

```
Host de-zoomcamp
	HostName 34.134.173.41
	User nlealiapp
	IdentityFile gcp
```

IdentifyFile es la ruta del archivo, si vamos a crear config en .shh lo pondemos así, sino debemos poner la ruta completa.

__IMPORTANTE__ Vcode pide la ruta completa: ~/.ssh/gcp sinó no funciona.

### Ejecución.

```bash
shh de-zoomcamp
```


#### INstalamos Docker

```bash
sudo apt-get update
sudo apt-get install docker.io
```

#### VS

Instalamos la extencion remote ssh open folder on remote.

