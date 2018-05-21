from __future__ import unicode_literals

from copy import deepcopy

import boto3
import json
from moto.ec2 import utils as ec2_utils
from uuid import UUID

from moto import mock_cloudformation
from moto import mock_ecs
from moto import mock_ec2
from moto import mock_s3

from boto3 import client


@mock_ec2
@mock_ecs
@mock_s3

def run_task():
    client = boto3.client('ecs', region_name='us-east-1')
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    conn = boto3.resource('s3', region_name='us-east-1')
    s3 = boto3.client('s3', region_name='us-east-1')
    conn.create_bucket(Bucket='mybucket')


    test_cluster_name = 'test_ecs_cluster'

    _ = client.create_cluster(
        clusterName=test_cluster_name
    )

    test_instance = ec2.create_instances(
        ImageId="ami-1234abcd",
        MinCount=1,
        MaxCount=1,
    )[0]

    instance_id_document = json.dumps(
        ec2_utils.generate_instance_identity_document(test_instance)
    )

    response = client.register_container_instance(
        cluster=test_cluster_name,
        instanceIdentityDocument=instance_id_document
    )

    _ = client.register_task_definition(
        family='test_ecs_task',
        containerDefinitions=[
            {
                'name': 'hello_world',
                'image': 'docker/hello-world:latest',
                'cpu': 1024,
                'memory': 400,
                'essential': True,
                'environment': [{
                    'name': 'AWS_ACCESS_KEY_ID',
                    'value': 'SOME_ACCESS_KEY'
                }],
                'logConfiguration': {'logDriver': 'json-file'}
            }
        ]
    )

    response = client.run_task(
        cluster='test_ecs_cluster',
        overrides={},
        taskDefinition='test_ecs_task',
        count=1,
        startedBy='moto'
    )

    # Put Task Arn in S3 Bucket
    s3.put_object(Bucket='mybucket', Key='taskArn', Body=response['tasks'][0]['taskArn'])
    taskArn = conn.Object('mybucket', 'taskArn').get()['Body'].read().decode()
    print("The S3 taskArn was:     " + taskArn)
 
    # Print out response attributes of ECS Task
    print("Number of tasks:        " + str(len(response['tasks'])))
    print("Task ARN:               " + response['tasks'][0]['taskArn'])
    print("Cluster ARN:            " + response['tasks'][0]['clusterArn'])
    print("TaskDefinition ARN:     " + response['tasks'][0]['taskDefinitionArn'])
    print("Container Instance ARN: " + response['tasks'][0]['containerInstanceArn'])
    print("Last Status:            " + response['tasks'][0]['lastStatus'])
    print("Desired Status:         " + response['tasks'][0]['desiredStatus'])
    print("Started By:             " + response['tasks'][0]['startedBy'])
   
run_task()
