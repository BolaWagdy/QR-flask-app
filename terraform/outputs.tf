output "instance_public_ip" {
  value = aws_instance.web.public_ip
}
output "instance_public_dns" {
  value = aws_instance.web.public_dns
}
