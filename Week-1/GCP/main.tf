terraform {
    required_providers {
      google = {
        source = "hashicorp/google"
        version = "5.6.0"
      }
    }
    
}

provider "google" {
    # Configuration options el archivo no lo publicamos
    credentials = file("archivo.....")
    project = "proyectoDataTalk"
    region = "us-central1"

}

resource "google_storage_bucket" "auto-expire" {
  name          = "proyectoaatatalk-mi_primer_bucket"
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



