# django books test task

## Description
This project was made as a test task

## Installation

First, [install Docker](https://docs.docker.com/installation/). If you're new to Docker, you might also want to check out the [Hello, world! tutorial](https://docs.docker.com/userguide/dockerizing/).

Next, open a terminal and clone this repo:

    $ git clone https://github.com/saltitc/books_test_task.git
    $ cd books_test_task 

Create a file with environment variables:
    
    $ touch .env

Copy the content below and paste into your .env file
```
DEBUG=True
DOMAIN_NAME=http://127.0.0.1:8000

REDIS_HOST=redis
REDIS_PORT=6379
REDIS_URL=redis://redis:6379/0

MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_DATABASE=library_db
MYSQL_PASSWORD=password
MYSQL_USER=library_user
MYSQL_ROOT_PASSWORD=password

EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=youremail@yandex.ru(instructions below)
EMAIL_HOST_PASSWORD=your_password(instructions below)
EMAIL_USE_SSL=True
```
> Emails (you can use yandex, gmail and others, the instruction will be on setting up the Yandex server):
>>   1. Create a yandex account.
>>   2. Go to settings > mail programs and tick all the boxes
>>   3. <img width="400" alt="image" src="https://github.com/saltitc/booking/assets/114296895/6e1723e5-8afc-48ae-a7ce-afc9bbae50f5">
>>   4. Up-to-date information about the email host, port and the use of ssl(specify True if ssl connection security) is available [here](https://yandex.ru/support/mail/mail-clients/others.html#smtpsetting__smtp-config-prog)
>>   5. Email host user is your email address
>>   6. Create an application password using this [link](https://id.yandex.ru/security/app-passwords)
>>   7. Click on the highlighted block and create a password name:
>>   8. <img width="400" alt="Снимок экрана 2023-11-25 в 13 02 16" src="https://github.com/saltitc/books_test_task/assets/114296895/2b782f58-28fa-4b68-a5ca-b1e1952ecf40"> <img width="405" alt="image" src="https://github.com/saltitc/books_test_task/assets/114296895/16de9a4e-f3ab-40c2-9a27-35d49cba6662">
>>   8. Copy the password and assign it to the EMAIL_HOST_PASSWORD variable in the .env file <img width="400" alt="Снимок экрана 2023-11-25 в 13 07 44" src="https://github.com/saltitc/books_test_task/assets/114296895/5dfeae0e-f0b1-400f-a127-0d5f903abb9a">

Finally, enter the following command in the terminal in the folder from the cloned repository

    $ docker-compose up --build 

> Errors
>> If you have any errors during installation, write to me in [telegram](https://t.me/saltitc)
>> 
>> If u get
>> ``` Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:3306 -> 0.0.0.0:0: listen tcp 0.0.0.0:3306: bind: address already in use ``` then you need to disable your MySQL server

