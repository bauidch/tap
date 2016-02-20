# flask-deployer
Flask on nginx with uwsgi 

Run the Image with your files
```bash
sudo docker run --name flask-app -p 80:80 -d -v ~/your-app:/usr/share/nginx/html bauidch/flask-deployer
```

Execute the flask-app container
```bash
sudo docker exec -it flask-app /bin/bash
```
