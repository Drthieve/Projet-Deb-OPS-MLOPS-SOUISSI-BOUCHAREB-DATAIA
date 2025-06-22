module "provider" {
  source = "./provider.tf"
}

module "instances" {
  source = "./instances.tf"
}
