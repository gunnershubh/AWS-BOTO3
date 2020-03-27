import boto3
import botocore
from pprint import pprint


session = boto3.Session(profile_name='lmit')
ec2_client = session.client('ec2')
response = ec2_client.describe_instances()


stopped = ec2_client.stop_instances(InstanceIds = ['i-084c4bc55f6479927'])
