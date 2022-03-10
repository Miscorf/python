#我们这里安装第一个
docker pull portainer/portainer
docker run -d -p 9000:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --name prtainer-test portainer/portainer



docker volume create portainer_data
docker run --name portainer321 -d -p 9186:9186 -p 9186:9186 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer

docker stop $(docker ps -q)
docker rm $(docker ps -aq)
git://github.com/big-data-europe/docker-hadoop.git


git clone git://github.com/kiwenlau/hadoop-cluster-docker

sudo docker network create --driver=bridge hadoop



