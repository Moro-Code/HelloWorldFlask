# Hello Supreme Leader and Welcome to Python web apps 101

We shall create a hello world app today using python-flask, gunicorn WSGI HTTP Server and Nginx HTTP proxy. Please note I look up setting up gunicorn and nginx everytime I have to do a manual deployment because honestly it's just not worth it to remember.

## A short primer on each item

### Flask

You already know this one obv. Our favorite little micro framework.

The reason why we use flask is that it is a micro framework. The process to get a flask application up and running is much less combersome than setting up django. Flask is geared towards making API's and considering thats what we mostly do anyways it's perfect for our applications.

The flask docs are fantastic. If there is anything that you don't know or are confused about. The answers are probably in [there](http://flask.pocoo.org/docs/1.0/) . In this tutorial we won't delve too much into using flask but rather how you can deploy a scalable flask app. 

### Green Unicorn (Gunicorn)

Flask has a built in WSGI server for development. I have made the mistake many times of forgetting of deploying a production app with this. This is a big no no. The Flask built in server should not be used in production. There are many different WSGI servers however gunicorn is the easiest to get a performant app with much less configuration. Again the [docs](https://gunicorn.org/) are excellent. The trouble here is that there are hundreds of ways you can configure gunicorn. However, for our purposes we don't need to concern ourselves with this 

### NGINX

The HTTP proxy to defeat all proxies. NGINX was originally developed as a load balancer. It is a fantastic and performant HTTP proxy. Again there is thousands of different ways you can configure NGINX so I won't even link to the docs for it. Usually if you chose a good WSGI server like gunicorn they will have the a suitable configuration already in their docs

### Our Setup

We will deploying a hello world app with all these components on an AWS EC2 instance with ubuntu 18.04.

I will have already installed NGINX but I will include the commands to do this for any new server below.

```sh
$ sudo apt-get update
$ sudo apt-get install nginx
# check if nginx installed successfully 
$ sudo nginx -v
```

Once you install nginx it should automatically start.
You can check this for yourself by the following command

```sh
$ sudo systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-06-26 15:14:25 UTC; 1min 46s ago
```
If in the odd case you find that nginx has not started you can always start it using the following command

```sh
$ sudo systemctl start nginx
```

Now we need to install python3 on the server. With the AWS AMI python 3.6.* already comes installed but if python3 is not installed on the server you can do the following

```sh
$ sudo apt install python3
```
check your python version 

```sh 
$ python3 -V
```
Okay now it's time to code our hello world application. We will be creating an HTML template from which we will be rendering from a view on a route as part of a blueprint.

Lot's of termonology however you'll quickly see how simple this is.

### Getting Python Environment set up

Before we can start coding we need to get our environment set up. It is important we isolate the dependancies of our projects for obvious reasons. To do this in python we use virtual environments. I like using venv because it is light weight and already comes with python

To create a virtual environment we use the following command

```sh
$ python3 -m venv [The name of your environment]
```

So we will do the following

```sh
$ python3 -m venv venv
```
This will create a folder called venv which you can think of an isolated python environment. Packages installed here won't be available to other environments. 

To use packages in an environment you must first activate it. This involves calling source on an activation script which will load the path of your environments packages into the system path

```sh
$ source activate ./venv/bin/activate
```
you should see a change to your command line 
```sh
(venv) user@ubuntu:~/$
```

Now install flask

```sh
$ pip install flask
```

You'll notice that the /venv is listed in the gitignore
Instead of uploading this large folder to github each time we instead have a requirements.txt which lists all the packages in our environment which we can then install in a virtual environment.

To generate a requirements.txt for your environment, activate your environment first then 

```sh
$ pip freeze > requirements.txt
```

You can now push your code to github

Once that is done log onto the server and pull your code. Or if you are doing this for the first time clone the repository.

Create the virtual environment and install from the requirements.txt

```sh
$ pip install -r requirements.txt
```
notice the flag -r which specifies recursion on the requirements file

### Setting up Gunicorn

First you need to install Gunicorn on the server

```sh 
$ pip install gunicorn
```

Then run the app with it

```sh
$ gunicorn -w 4 app:app --deamon
```
This will start a gunicorn deamon with 4 workers on port 8000

### configuring NGINX

We will do a very simple NGINX configuration

```nginx
server {
   listen 80;
   server_name _;
   access_log /var/log/nginx/example.log

   location / {
      proxy_pass http://127.0.0.1:8000;
      proxy_set_header Host $host;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
   }
}
```

You should now see the application when you navigate to the IP 




