# ECS task runner example app

This python script run an ECS task and test it locally against moto mocks

## Getting Started

This script will allow you to:
- mock ec2, ecs & s3 locally via moto
- create an ecs cluster
- register an instance to the cluster
- register a task definition
- run the task on the cluster
- save the arn that results from the task to an object in s3
- retrieve the arn from s3
- output the results to the console

### Prerequisites

```
Requirements:
- moto
- python2.7
- docker
- python virtualenv
```

### Installing

```https://github.com/spulec/moto```
```https://www.python.org/downloads/release/python-2714/```
```https://docs.docker.com/install/```
```https://virtualenv.pypa.io/en/stable/installation/```

### Executing Script

```python execute_ecs_task.py```