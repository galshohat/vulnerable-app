provider "aws" {
  region     = "us-east-1"
  # VULN-85: AWS credentials hardcoded in Terraform
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

# VULN-86: S3 bucket with public access
resource "aws_s3_bucket" "data" {
  bucket = "inboxops-customer-data"
  acl    = "public-read"
}

# VULN-87: Security group allows all inbound traffic
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

# VULN-88: RDS instance with no encryption
resource "aws_db_instance" "main" {
  engine               = "postgres"
  instance_class       = "db.t3.medium"
  allocated_storage    = 100
  storage_encrypted    = false
  publicly_accessible  = true
  skip_final_snapshot  = true
  # VULN-89: Database master password in Terraform
  username             = "inboxops_admin"
  password             = "Pr0d_DB_P4ssw0rd2024"
}
