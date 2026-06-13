resource "aws_ecr_repository" "frontend" {
  name = "frontend"
}

resource "aws_ecr_repository" "users" {
  name = "users-service"
}

resource "aws_ecr_repository" "orders" {
  name = "orders-service"
}

resource "aws_ecr_repository" "payments" {
  name = "payments-service"
}

resource "aws_ecr_repository" "inventory" {
  name = "inventory-service"
}