apt-get update
sudo apt install python3 python3-pip -y
pip3 install Flask==0.10.1
pip3 install google-cloud-logging
SERVER_ID=$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/my-server-id -H "Me
tadata-Flavor: Google")
apt-get install -y apache2
service apache2 restart &
curl -sSO https://dl.google.com/cloudagents/add-logging-agent-repo.sh
sudo bash add-logging-agent-repo.sh
sudo apt-get update
sudo apt-get install google-fluentd
service google-fluentd start &
mkdir /MKGames
cd /MKGames
python3 ./app.py
