#!/usr/bin/python

import boto3
from pprint import pprint
ec2 = boto3.resource('ec2', aws_access_key_id = 'PUTYOURACCESSKEY', aws_secret_access_key = 'PUTYOURSECRETKEY')

instances_list = []

for instance in ec2.instances.all():
    # print (type(instance.id))
    pprint(instance)
    instances_list.append(instance.id)
    if instance.id == 'i-INSTANCEID':
        for method in dir(instance):
            print(method)
        pprint(type(instance.tags))
        instance.create_tags(Tags=[
        {
            'Key': ' Name',
            'Value': 'test code',
        },
    ])
        
