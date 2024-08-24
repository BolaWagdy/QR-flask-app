# QR-Code Generator
![example workflow](https://github.com/BolaWagdy/QR-flask-app/actions/workflows/main.yml/badge.svg)

# Features

- Generate QR codes for any text or URL.
- Save QR codes in image formats.

# Project structure
```
└──.github
    └── 📁workflows
        └── main.yml
└── 📁ansible
    └── 📁roles
        └── 📁docker
            └── 📁tasks
                └── main.yml
    └── ansible-playbook.yml
    └── ansible.cfg
    └── hosts.ini
└── 📁app_py
    └── 📁db
        └── analyze.py
        └── users_visits.json
    └── 📁static
        └── 📁css
            └── bootstrap.min.css
    └── 📁templates
        └── home.html
    └── 📁tests
        └── __init__.py
        └── test_index.py
    └── 📁uploads
        └── qr-code.png
        └── share.png
    └── app.py
    └── Dockerfile
    └── requirements.txt
    └── wsgi.py
└── 📁k8s
    └── 📁minikube
        └── deployment.yaml
        └── ingress.yaml
        └── namespace.yaml
        └── service.yaml
└── 📁terraform
    └── .terraform.lock.hcl
    └── terraform-ec2.tf
└── .gitignore
└── index.html
└── Jenkinsfile               
```

# Installation

## 1. Python3
![img](https://ctf-cci-com.imgix.net/1vibQmk6bIzcqa7IOAhMcU/721c31daca3424f098689844146df25a/2024-05-30-testing-for-python.png?ixlib=rb-3.2.1&w=2000&auto=format&fit=max&q=60&ch=DPR%2CWidth%2CViewport-Width%2CSave-Data)
> Ensure you have Python installed. Download it from [python.org](https://www.python.org/downloads/).

### Documentation steps:

- Step1: Clone the repository

    ```bash
    git clone https://github.com/BolaWagdy/QR-Code.git
    cd QR-Code
    ```


- Step2: Testing 

    ```bash
    apt install python3-pytest
    cd app_py
    pytest
    ```

- Step3: Virtual Environment

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

- Step4: Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```

## 2. Docker
![img](https://media.licdn.com/dms/image/D5612AQGeEHapUptoxw/article-cover_image-shrink_600_2000/0/1684079864237?e=2147483647&v=beta&t=UUUAS5PPyisf3YVxC_VFidjxwFeTZwfpb1y4dH0G5xs)
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

### Push to Docker Hub steps:
> [!NOTE]  
> Repo link on Docker Hub: https://hub.docker.com/repository/docker/bola278/app_py/general            

- Step 1: Tag Your Docker Image

    ```bash
    docker tag app_py:latest bola278/app_py:latest
    ```

- Step 2: Login to Docker Hub

    ```bash
    docker login
    ```

- Step 3: Push to Docker Hub

    ```bash
    docker push bola278/app_py:latest
    ```

- Step4: Pull from Docker Hub

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

### Best practices:
- **Use an IDE plugin** for help with syntax highlighting and linting of `Jenkinsfile`.
- **When running Jenkins as a docker container**
  - Use the official and maintained image for Jenkins.
    - [Official Image](https://hub.docker.com/r/jenkins/jenkins) at the time of writing this.
  - Use `Dockerfile` and `docker-compose.yaml` for Jenkins deployment instead of running a long, undocumented command in the terminal.
  - Pay attention to the base OS and the user under which the container is running since:
    - Using `sh` in `Jenkinsfile` runs commands under that user and that base OS.
    - Running docker commands (e.g., `docker push`) from Jenkinsfile can be problematic when Jenkins itself is running as a docker container [[solution](http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/)].
- **Use maintained plugins instead of shell scripts for:**
  - Setting up tools, environment and dependencies (it makes build faster and more portable).
  - Working with credentials for Jenkins and 3rd party integrations (it’s more secure and organized).
- **In production environments:**
  - Create users and configure access controls for them, not everyone should have access to the admin credentials.
  - Set up distributed builds as building on the built-in node can be a security issue.


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
- Give permission to labsuser.pem
  ```bash
  cd Downloads
  sudo chmod 400 labsuser.pem
  ```

- Run ansible file
  ```bash
  cd ansible
  ansible-playbook.yml -i hosts.ini ansible-playbook.yml
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
- Before run

    ```bash
    nano ~/.aws/credentials # Update with your AWS lab credentials
    ```

- Run terraform
    ```bash
    terraform init       # Prepare workspace and download providers
    terraform validate   # Check configuration for validity
    terraform fmt        # Format source file
    terraform plan       # Show execution plan
    terraform apply      # Apply all
    ```
## 6. Kubernetes
![img](https://dt-cdn.net/wp-content/uploads/2023/01/BAE3222_RC_K8s2023_800x450_FINAL.png)

- kubernetes installation

    1. Install [kubectl](https://kubernetes.io/docs/tasks/tools/) and [minikube](https://minikube.sigs.k8s.io/docs/start/)

    2. Run minikube start to start a local k8s cluster and configure kubectl to interact with it.

## Apply the Kubernetes Configuration steps:
- Step 1: Start Minikube
    ```bash
    cd k8s
    cd minikube
    minikube start
    ```

- Step 2: Apply all
    ```bash
    kubectl apply -f namespace.yaml -f deployment.yaml -f service.yaml -f ingress.yaml
    ```
    

## Show running logs
```bash
kubectl get all -n app-ns
```
## URL link generator 
```bash
 minikube service -n app-ns qr-flask-app-service --url
```
