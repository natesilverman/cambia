 1: Feature: Run serverless hello world docker app on ecs cluster as task
 2:   Task needs to be launched on locally mocked ecs cluster
 3:   Task is represented by task definition that utilizes existing hello world docker image
 4:   Script validates proper execution against ecs cluster and saves task arn to S3
 5: 
 6:   Scenario: Product team has signed off on hello world functionality 
 7:     Given JIRA tickets relative to the hello world image have been completed
 8:       And current sprint is in progress
 9:     When a developer has created a hello world Docker image to be deployed
10:       And Docker image has been successfully tested 
11:       And this script has been successfully run
12:     Then 
13:       Output of various AWS created objects should be generated to verify success
14:       - S3 taskArn should return properly from S3 query
15:       - Number of tasks should return 1
16:       - Task Arn should be listed successfully and be same as S3 taskArn
17:       - Cluster Arn should be listed successfully and should be named test_ecs_cluster
18:       - TaskDefinition Arn should be listed successfully and should be test_ecs_task:1
19:       - Container Instance Arn should be listed properly
20:       - Last Status should be listed as RUNNING
21:       - Desired Status should be listed as RUNNING
22:       - Started By should be listed as moto