# tap
My Dockerfiles

Show docker images
``` bash
sudo docker images
```

Show all Docker containers
``` bash
sudo docker ps -a
```
Build a image
``` bash
docker build -t <yourname>/<image-name> .
```
Execute a container
```bash
sudo docker exec -it container-name /bin/bash
```
##SQL container

Pull the mysql image
```bash
sudo docker pull mysql:latest
```

Run the MySQL Container
```bash
sudo docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql
```
