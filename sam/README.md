# Yaml to SAM converter

This python script will convert a lambda yaml description to an executable SAM file.

## Getting Started

These steps will allow you to:
- convert the lambda yaml file to a sam file
- install necessary hello world requirements
- deploy the application code
- start a local copy of sam to verify the Api execution locally

### Prerequisites

```
Requirements:
- aws-sam-cli
- python2.7
- docker
- python virtualenv
```

### Installing

```https://github.com/awslabs/aws-sam-cli```
```https://www.python.org/downloads/release/python-2714/```
```https://docs.docker.com/install/```
```https://virtualenv.pypa.io/en/stable/installation/```

## Run Instructions

### Parse yaml and create sam template

```python create_sam.py lambda_template.yaml```

### Install app dependencies

```pip install -r requirements.txt -t hello_world/build/```

### Deploy build

```cp hello_world/*.py hello_world/build/```

### Start sam locally to test endpoint

```sam local start-api```

### Curl against sam local to verify endpoint returns properly

```curl -v http://127.0.0.1:3000/hello```