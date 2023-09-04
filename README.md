## Hollywood Actors Image Classification with deployment in AWS Cloud EC2 Instance
### The main aim of this project is to classify images of the Hollywood Actors scrapped from google using opencv library and Machine Learning Algorithms

- The model was built using opencv-python library and linear regression from images scrapped from google.
- The python flask server that uses the saved model to serve http requests. 
- The website built in html, css and javascript that allows user to drag or click to upload an image from the local system and calls python flask server to classify the actors images 
  and displaying the probability of match found.

#### In this data science and machine learning project, we classify Hollywood Actors. We restrict classification to only 5 people,
  - Brad Pitt
  - Chris Hemsworth
  - Dwayane Johnson
  - Leonardo Dicaprio
  - Will Smith

### Deploying in EC2 Instance of AWS Cloud
1> Createing an EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic.

2> Connecting with the EC2 Instance using the following commands in Git Bash
  - ssh -i "Hollywood_Actors_Classification.pem" ubuntu@ec2-16-171-137-199.eu-north-1.compute.amazonaws.com
   
3> Installing nginx server in EC2 Instance using
  - sudo apt-get update
  - sudo apt-get install nginx
   
4> Checking the status of nginx
  - sudo service nginx start
  - sudo service nginx status
   
5> Creating file /etc/nginx/sites-available/bhp.conf
  - server {
    listen 80;
        server_name hac;
        root /home/ubuntu/Classification/UI;
        index app.html;
        location /api/ {
             rewrite ^/api(.*) $1 break;
             proxy_pass http://127.0.0.1:5000;
        }

  }
  
6> Creating symlink for bhp.conf file in /etc/nginx/sites-enabled
  - sudo ln -v -s /etc/nginx/sites-available/hac.conf
   
7> Restaring nginx
  - sudo service nginx restart
   
8> Installing pip3 and requirements in EC2 Instance
  - sudo apt-get install python3-pip
  - sudo pip3 install -r /home/ubuntu/Classification/requirements.txt
   
9> Running the server.py
  - python3 /home/ubuntu/Classification/server/server.py

ec2-13-48-42-94.eu-north-1.compute.amazonaws.com is the url where we can predict the prices of home in Bangalore
![Result](https://github.com/guddushah/Banglore-Home-Price-Prediction/assets/40028193/36015fba-e7a8-44c2-b651-b63275d17f19)
