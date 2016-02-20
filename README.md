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

##MongoDB container

Pull the mongo image
```bash
sudo docker pull mongo:latest
```

Run the MongoDB Container
```bash
sudo docker run --name mongodb-server -d mongo
```

Link MongoDB to Container(MongoDB port: 27017)
```bash
docker run --name server --link mongodb-server:mongo -d ubuntu
```

##MySQL container

Pull the mysql image
```bash
sudo docker pull mysql:latest
```

Run the MySQL Container
```bash
sudo docker run --name mysql-server -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql
```

Link MySQL to Container (MySql Port 3306)
```bash
docker run --name webserver --link mysql-server:mysql -d nginx
```

##Wordpress
Run wordpress container with linkt to MySQL container
```bash
docker run --name the-blog --link mysql-server:mysql -d wordpress
```
