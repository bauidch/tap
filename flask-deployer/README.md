# flask-deployer
[![Docker Hub](https://img.shields.io/badge/Docker Hub-Image-blue.svg?style=flat-square)](https://hub.docker.com/r/bauidch/flask-deployer/)

Flask on nginx with uwsgi 

Install the image
```bash
docker pull bauidch/flask-deployer
```

Run the Image with your files
```bash
sudo docker run --name flask-app -p 80:80 -d -v ~/your-app:/usr/share/nginx/html bauidch/flask-deployer
```

##### ! Your App must run in the app.py !

Link MongoDB to the Container
```bash
sudo docker run --name app -p 80:80 --link mongodb-server:mongo bauidch/flask-deployer
```

Execute the flask-app container
```bash
sudo docker exec -it flask-app /bin/bash
```


### Included Python Modules
- Uwsgi
- Flask
- Pymongo
 
## Via Docker Compose
Look at the ```docker-compose.yml``` file.
- Run App on port 80
- Include volume ~./MyApp to the app dir in the container
- Iclude MongoDB to a mongodb container
