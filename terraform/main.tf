resource "aws_instance" "web" {
  ami           = "ami-04a81a99f5ec58529" 
  instance_type = "t2.micro"

  key_name        = "vockey"
  security_groups = [aws_security_group.terraform_sg.name]

  tags = {
    Name = "Terraform-EC2"
  }
}

