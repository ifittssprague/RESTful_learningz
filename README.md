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