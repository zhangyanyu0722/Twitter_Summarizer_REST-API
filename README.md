# Twitter Summarizer Based on Flask and Restful
## Step 1: Learn Flask and RESTful as WEB service platform
### Flask
- Reference 1: [Flask] ([Github])
- Reference 2: [Flask-RESTFUL] ([Github.])
## Step 2: Integrate module to become a RESTFUL system
### *** My API is setting on AWS EC2 Services with 1GB memory. For more detail, visit: [AWS] ***
### *** To save money, I temporarily terminated the service ***
- First, visit ec2-3-85-121-108.compute-1.amazonaws.com with port 80
```
ec2-3-85-121-108.compute-1.amazonaws.com:80
```
- Second, write 1~4 keyword in the block and click submit.
******************************************************
The name you input must be the exist twitter name
******************************************************
<p align="center">
  <img src= "https://github.com/BUEC500C1/twitter-summarizer-rest-service-zhangyanyu0722/blob/master/img/8.png" width=600>
</p>

- Third, wait a few seconds, the files will be downloaded.
<p align="center">
  <img src= "https://github.com/BUEC500C1/twitter-summarizer-rest-service-zhangyanyu0722/blob/master/img/9.png" width=400>
</p>

[AWS]: https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin&region=us-east-1
[Flask]: https://palletsprojects.com/p/flask/
[Github]: https://github.com/pallets/flask
[Flask-RESTFUL]: https://flask-restful.readthedocs.io/en/latest/
[Github.]: https://github.com/flask-restful/flask-restful
[AWS Services]: https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc
