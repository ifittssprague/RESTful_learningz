# RESTful_learningz
Learning some things about RESTful APIs and Flask in an attempt to become a more well rounded developer.

This repo is mostly musings to be fair


## Running the API
To run this application, you will need Python 3+ and Pipenv installed locally. If you have then, you can issue the following commands:
```
# from the flask-restful-apis directory
pipenv install
./bootstrap.sh 
```

Then you can issue requests to your API. For example, with curl, you can issue requests like that:

## Utilizing Docker

If you have Docker installed, the API can also be run on a Docker container. After running the `pipenv install` command listed above, you will also need to install docker on the virtual enviroment. 

After Docker has been installed, this API can be hosted on a Docker container by running the command.
```
docker build -t banking .
```

### inserting a new income
```
curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 300.0,
    "description": "loan payment"
}' http://localhost:5000/incomes
```

### listing all incomes
```
curl http://localhost:5000/incomes
```

#### A majority of the learnings in this repo are from the following super helpful guide:
https://auth0.com/blog/developing-restful-apis-with-python-and-flask/