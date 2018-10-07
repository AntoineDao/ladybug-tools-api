#### FLASK RESTFUL API BOILER-PLATE WITH JWT

[![Build Status](https://travis-ci.com/AntoineDao/ladybug-tools-crud-API.svg?branch=master)](https://travis-ci.com/AntoineDao/ladybug-tools-crud-API)


### Terminal commands

    Initial installation: make install

    To run test: make tests

    To run application: make run

    To run all commands at once : make all


### Viewing the app ###

    Open the following url on your browser to view swagger documentation
    http://127.0.0.1:5000/


### Using Postman ####

    Authorization header is in the following format:

    Key: Authorization
    Value: "token_generated_during_login"

    For testing authorization, url for getting all user requires an admin token while url for getting a single
    user by public_id requires just a regular authentication.


### Contributing
If you want to contribute to this Ladybug Tools API server clone the repository and just start making pull requests.

### Shoulders of giants
I cannot thank [`cosmic-byte`](https://github.com/cosmic-byte) enough for their thorough article walking through how to build a
flask restplus api server. The repo forked for the basis of this project can be found below:
```
https://github.com/cosmic-byte/flask-restplus-boilerplate.git
```
And the article explaining how to build a similar restful api can be found [here](https://medium.freecodecamp.org/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563)
