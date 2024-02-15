terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }

}
provider "google" {
  # Configuration options el archivo no lo publicamos
  credentials = file("./mis_claves/projectonleali-649724cf41f9.json")
  project     = var.project
  region      = "us-central1"
}


resource "google_storage_bucket" "auto-expire" {
  name          = var.gcs_bucket_name
  location      = var.location
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

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location

}
