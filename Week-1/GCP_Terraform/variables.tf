variable "project" {
  default     = "projectonleali"
  description = "Este es el proyecto de Google"
}

variable "bq_dataset_name" {
  default     = "demo_dataset_nleali"
  description = "My bigQuery Dataset"
}




variable "gcs_bucket_name" {
  description = "Nombre del bucket"
  default     = "projectonleali-mibucket"
}

variable "location" {
  description = "Este bucket esta en US"
  default     = "US"
}