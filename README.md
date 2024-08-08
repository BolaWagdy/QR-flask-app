# QR-Code Generator
![example workflow](https://github.com/BolaWagdy/QR-flask-app/actions/workflows/main.yml/badge.svg)

# Features

- Generate QR codes for any text or URL.
- Save QR codes in image formats.

# Installation

## 1. Python3
- Ensure you have Python installed. Download it from [python.org](https://www.python.org/downloads/).

### Documentation

#### Step1: Clone the repository

```bash
git clone https://github.com/BolaWagdy/QR-Code.git
cd QR-Code
```

#### Step2: Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step3: Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Docker
- For Docker-based installation, ensure Docker is installed from this steps.

```bash
# Install docker, buildx, and docker-compose
sudo apt install docker.io docker-compose docker-buildx

# Post installation steps: to run docker without sudo
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# Test installation
docker run hello-world
```
### Build & Run Docker Image

```bash
docker build -t app_py .
docker run -p8080:8080 app_py
```

### Push to Docker Hub
> [!NOTE]  
> Link on Dockerhub: https://hub.docker.com/repository/docker/bola278/app_py/general            

#### Step 1: Tag Your Docker Image

```bash
docker tag app_py:latest bola278/app_py:latest
```

#### Step 2: Login to Docker Hub

```bash
docker login
```

#### Step 3: Push to Docker Hub

```bash
docker push bola278/app_py:latest
```

#### Step4: Pull from Docker Hub

```bash
docker pull bola278/app_py
```
## 3. Jenkins

- Jenkins Installation

    > Docs: <https://www.jenkins.io/doc/book/installing/linux>

    ```bash
    # Installing jenkins and dependencies
    sudo apt-get update && sudo apt-get install -y fontconfig openjdk-17-jre
    sudo wget -O /usr/share/keyrings/jenkins-keyring.asc   https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]"   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
    sudo apt-get update && sudo apt-get install -y jenkins
    
    # Verify installation
    sudo systemctl status jenkins
    
    # Get admin password
    sudo cat /var/lib/jenkins/secrets/initialAdminPassword
    ```

## 4. Ansible

- Ansible installation

    > Reference: <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>


- They recommend using `pipx` to have Ansible CLI tools (`ansible`, `ansible-playbook`, etc.) available globally.

  ```bash
  pipx install --include-deps ansible
  ```

- You may also want to install the plugin for VSCode and `ansible-lint`

  ```bash
  pipx install ansible-lint
  ```

## 5. Terraform

- Download and install [Terraform CLI](https://www.terraform.io/downloads).

    ```bash
    cd /tmp
    export RELEASE=$(curl -s https://api.github.com/repos/  hashicorp/terraform/releases/latest | jq -r '.tag_name')
    RELEASE="${RELEASE:1}" # Remove the 'v'
    wget "https://releases.hashicorp.com/terraform/${RELEASE}/  terraform_${RELEASE}_linux_amd64.zip"
    unzip terraform_${RELEASE}_linux_amd64.zip
    sudo mv terraform /usr/local/bin
    ```
- Download, install, and configure AWS CLI

    ```bash
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64. zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    aws configure
    ```
- Run

    ```bash
    terraform init       # Prepare workspace and download providers
    terraform validate   # Check configuration for validity
    terraform fmt        # Format source file
    terraform plan       # Show execution plan
    terraform apply
    ```
