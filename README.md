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


#### Step2: Testing 

```bash
apt install python3-pytest
cd app_py
pytest
```

#### Step3: Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step4: Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. Docker
![img](https://images.shiksha.com/mediadata/images/articles/1700649967php8v6tWG.jpeg)
- Docker installation

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

![img](https://www.jenkins.io/images/post-images/blueocean/pipeline-run.png)

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

![img](https://cdn.hashnode.com/res/hashnode/image/upload/v1689150053976/ab2d96c7-398a-42da-a6a6-bb0f7842d97a.webp?w=1600&h=840&fit=crop&crop=entropy&auto=compress,format&format=webp)

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
![img](https://developer.hashicorp.com/_next/image?url=https%3A%2F%2Fcontent.hashicorp.com%2Fapi%2Fassets%3Fproduct%3Dterraform%26version%3Drefs%252Fheads%252Fv1.9%26asset%3Dwebsite%252Fimg%252Fdocs%252Fintro-terraform-apis.png%26width%3D2048%26height%3D644&w=2048&q=75&dpl=dpl_AsSRcRKA9VSqCeGAyCyNSd63nA73)

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
- Run terraform

    ```bash
    terraform init       # Prepare workspace and download providers
    terraform validate   # Check configuration for validity
    terraform fmt        # Format source file
    terraform plan       # Show execution plan
    terraform apply
    ```
