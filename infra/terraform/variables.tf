variable "instance_type" {
  description = "Type d'instance EC2"
  default     = "t2.micro"
}

variable "ami" {
  description = "AMI Ubuntu 22.04 LTS"
  default     = "ami-053b0d53c279acc90"
}



variable "key_name" {
  description = "Nom de la clé SSH existante"
  default     = "mlops-key"
}
