# Lambda CI Demo

###### Automatically release a python lambda to AWS via BitBucket Pipelines
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

### Run the API locally
```bash
pip install -r requirements.txt -r requirements_local.txt

python -m uvicorn api.main:app --reload  
```

### Test the API locally
==THIS CURRENTLY DOES NOT WORK==

~~Install `newman` (via brew or npm), then (with the API running locally) do:~~
```bash
newman run postman_tests/lambda_ci_demo.postman_collection.json
```

### Run the API locally via Docker
```bash
docker-compose run api  
```

### Test the API locally via Docker

Install `newman` (via brew or npm), then (with the API running locally) do:
```bash
docker-compose run api_test
```


### Make changes to the API

#### Pre-requisites:
Make sure you have pre-commit installed:
```bash
pip install pre-commit
```


#### Debugging pipeline issues locally

Run the same image as BB locally:
```bash
docker run -v `pwd`:/api -it python:3.9.6-slim-buster /bin/sh
```

then just run the `bitbucket-piplines.yml` instructions in order