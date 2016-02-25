# flask-dokku
Simply Flask Demo app for Dokku(Mini PaaS on Docker) 

Clone the Git
```
git clone 
```

Crate the ap on your Dokku Server
```
dokku apps:create flask-dokku
```

Deploy our app to your Dokku server
```
git remote add dokku dokku@<hostname>:flask-dokku
git push dokku master
```
