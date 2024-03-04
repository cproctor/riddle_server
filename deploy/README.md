# Deploy instructions

These instructions are for a very basic deployment, really only 
suitable for a teaching demo. First, create the cheapest possible
Ubuntu droplet in Digital Ocean. SSH in as root.

```
apt update
apt upgrade
apt install python3-venv
cd /opt
git clone https://github.com/cproctor/riddle_server.git
cd riddle_server
env/bin/pip install -r requirements.txt
ln -s /opt/riddle_server/deploy/riddles.service /etc/systemd/system/riddles.service
```
