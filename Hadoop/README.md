#### Option 1: Use WSL (Windows Subsystem for Linux) → Recommended

Steps:

Enable WSL
Open PowerShell (Admin) and run:

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

Restart your system.

Install Ubuntu from Microsoft Store

Open Microsoft Store → Search Ubuntu 22.04 LTS → Install.

Open it once and create username + password.

Install Java in Ubuntu

sudo apt update
sudo apt install openjdk-11-jdk -y
java -version

Download & Setup Hadoop (inside Ubuntu)
Same Linux steps I gave earlier:

cd /usr/local
sudo wget https://downloads.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz
sudo tar -xvzf hadoop-3.4.0.tar.gz
sudo mv hadoop-3.4.0 hadoop

Set Environment Variables
Add to ~/.bashrc:

export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

source ~/.bashrc

Configure, Format, and Start Hadoop
(same as Linux guide).

Access Hadoop UI in Browser (on Windows)

Namenode: http://localhost:9870

YARN: http://localhost:8088
