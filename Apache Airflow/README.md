#### Install Docker on Windows 10/11

Step 1: Install WSL2 (Windows Subsystem for Linux)

Run PowerShell as Administrator:

wsl --install

Then reboot.

Step 2: Install Docker Desktop

Download: Docker Desktop for Windows

Install with default settings (choose WSL2 backend).

After installation, restart and open Docker Desktop.

Step 4: Verify

Open PowerShell or CMD:

docker --version
docker run hello-world

#### Install Docker on Ubuntu / Linux

Step 1: Remove old Docker versions
sudo apt-get remove docker docker-engine docker.io containerd runc

Step 2: Update and install dependencies
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release -y

Step 3: Add Docker’s official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

Step 4: Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Step 5: Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

Step 6: Verify
docker --version
sudo docker run hello-world

To run without sudo:

sudo usermod -aG docker $USER
newgrp docker

###### Install Docker on macOS

Step 1: Download

Get Docker Desktop for Mac: Docker Mac Download

Step 2: Install

Open the .dmg → drag Docker to Applications.

Start Docker Desktop from Applications.

Step 3: Verify
docker --version
docker run hello-world

##### SETTING UP AIRFLOW WITH DOCKER

Step 1: Prerequisites

Make sure you have these installed:

Docker & Docker Compose
Check with:
docker --version
docker compose version

Step 2: Get Airflow’s Official Docker Setup

The Airflow team provides a ready-to-use Docker Compose setup.

mkdir airflow-docker
cd airflow-docker

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'

Create Folders for Airflow

Airflow needs some directories for logs, plugins, and dags:

mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
The .env file ensures proper permissions inside Docker.

Step 4: Initialize Airflow Database

Run once before starting Airflow:

docker compose up airflow-init

This sets up the metadata database and creates default connections.

 Step 5: Start Airflow

Now bring everything up:

docker compose up -d

This starts multiple services:

Airflow Webserver → UI at http://localhost:8080

Scheduler → triggers tasks

Postgres → Airflow metadata DB

Redis → message broker

Workers (CeleryExecutor)

Step 6: Login

Default credentials:

Username: airflow

Password: airflow
