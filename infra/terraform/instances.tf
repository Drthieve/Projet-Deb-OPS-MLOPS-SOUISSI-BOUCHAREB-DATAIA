resource "aws_instance" "ml_api" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "ml-api"
  }
}

resource "aws_instance" "ml_train" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name

  tags = {
    Name = "ml-train"
  }
}
