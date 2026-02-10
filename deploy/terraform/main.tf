provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

resource "aws_s3_bucket" "data" {
  bucket = "inboxops-customer-data"
  acl    = "public-read"
}

resource "aws_security_group" "web" {
  name = "inboxops-web-sg"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "main" {
  engine               = "postgres"
  instance_class       = "db.t3.medium"
  allocated_storage    = 100
  storage_encrypted    = false
  publicly_accessible  = true
  skip_final_snapshot  = true
  username             = "inboxops_admin"
  password             = "Pr0d_DB_P4ssw0rd2024"
}
