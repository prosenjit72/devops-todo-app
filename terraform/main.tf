# কোন cloud use করব — AWS
provider "aws" {
  region = "ap-southeast-1"
}

# Security Group — server এ কোন port খোলা থাকবে
resource "aws_security_group" "todo_sg" {
  name = "todo-app-sg"

  # Port 80 — internet থেকে app access করা যাবে
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Port 22 — SSH দিয়ে server এ ঢোকা যাবে
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # সব outbound traffic allow
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Server — free tier t3.micro
resource "aws_instance" "todo_server" {
  ami           = "ami-0497a974f8d5dcef8"
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.todo_sg.id]

  # Server চালু হলে Docker install করো
  user_data = <<-EOF
    #!/bin/bash
    apt-get update -y
    apt-get install -y docker.io
    systemctl start docker
    docker run -d -p 80:5000 prosenjit72/todo-app:latest
  EOF

  tags = {
    Name = "todo-app-server"
  }
}

# Server এর IP address দেখাবে
output "server_ip" {
  value = aws_instance.todo_server.public_ip
}