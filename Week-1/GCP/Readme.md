# Google Cloud Y terraform



+ Big Data
+ Storage Database

## Tipos de cuenta en GCP

1. Service acount -> es un tipo de cuenta que solo deberia ser acedida por software
2. User Account -> es una cuenta para usuarios con privilegios.

¿Cómo crear una cuenta de servicio?

|Pasos|descripcion|
|-----|-----------|
|IAM and admin| service account -> create services acoount|
|Otorgar permisos| GCP Bucket - storage admin|
|BigQuery|Admin|
|COmpute Engine|Admin|

__Generamos la clave como JSON y la guadardamos en un lugar seguro__


## Terraform 

Se usa para crear infraestructura en la nube.

+ Infraestructura como código.

```
Util para eliminar los recursos que creamos y no necesitamos mas (No ser cargados con los pagos de los mismos).
```

1. No está hecho para deployar software.
2. No está pensado para manejar recrusos que no están especificados en el _terraform file_

¿ Qué es Terraform?

Es infraestructura como código.


- providers -> Es el código que permite a terraform comunicarse y manejar recursos con:

1. AWS
2. AZURE
3. GCP


## Comandos claves

|command|descripción|
|-------|-----------|
|init|Get all the providers I need|
|plan|what am I about to do?|
|apply|Do what is in the _tf_ files|
|destroy|Remove everything defined in the tf files|



## Creacion de un archivo Terraform para Google Provider

Buscamos en google un modelo de __provider de terraform para google y le empezamos a añadir servicios__


```terraform
provider "google" {
    # Configuration options
        } 
```


Desde la consola un comando que nos puede ayudar a que todo se vea mejor es 

terraform fmt

debemos estar en la carpeta del main.tf

## Ejecucion de terraform

1. Primero debemos instalarlo. Es un archivo ejecutable, lo descargamos en una carpeta y creamos una variabe de sistema.
2. En este ejemplo no está funcionando desde gitbash asique lo hacemos desde __cmd__ situados en el directorio del main.tf

```shell
tarraform init
```



```
Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/google versions matching "5.6.0"...
- Installing hashicorp/google v5.6.0...
- Installed hashicorp/google v5.6.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

### Creacion de un BUcket en GCP

- para saber como crear un Bucket lo buscamos en Intener (Google)
- El nombre de un bucket debe ser único, podemos unier el nombre del proyecto + Bucket.

```json
resource "google_storage_bucket" "auto-expire" {
  name          = "auto-expiring-bucket"
  location      = "US"
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
```

* age -> está en dias

+ ¿Qué es Terraform plan?

Es un plan de ejecución que muestra lo que va a hacer y el orden.
Se ejecuta desde la consola sobre el directorio que está el __main.tr__


```
terraform plan
```

### Ejecutamos terraform

```
terraform apply
```

```
google_storage_bucket.auto-expire: Creating...
google_storage_bucket.auto-expire: Creation complete after 2s [id=proyectoaatatalk-mi_primer_bucket]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

__IMPORTANTE__ tuvimos que ejecutar el archivo con un nuevo usuario con permisos de edit.

### Destruimos el todo lo que creamos.

Cuando ejecutamos __apply__ se crea un archivo de estados con información de lo que ejecutó _terreform_ __terraform.tfstate__
Para hacer el __DESTROY__ LLAMA A ESTE ARCHIVO y consulta lo que debe eliminar.

```
terraform destroy
```
```
google_storage_bucket.auto-expire: Destroying... [id=proyectoaatatalk-mi_primer_bucket]
google_storage_bucket.auto-expire: Destruction complete after 3s

Destroy complete! Resources: 1 destroyed.
```

### Creacion de un Dataset  - BigQuery

```
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = "demo_dataset"
}
```

En este ejemplo creamos n _bucket_ y un _biqquery_

```
google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.auto-expire: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 2s [id=projects/projectonleali/datasets/demo_dataset]
google_storage_bucket.auto-expire: Creation complete after 2s [id=proyectoaatatalk-mi_primer_bucket]

```