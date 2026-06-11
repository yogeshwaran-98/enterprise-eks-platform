resource "aws_ecr_repository" "frontend" {
  name = "frontend"
}

resource "aws_ecr_repository" "users" {
  name = "users"
}

resource "aws_ecr_repository" "orders" {
  name = "orders"
}

resource "aws_ecr_repository" "payments" {
  name = "payments"
}