#List S3 buckets in InstanceCount

import boto3
from pprint import pprint
s3 = boto3.client('s3', aws_access_key_id = 'PUTYOURACCESSKEY', aws_secret_access_key = 'PUTYOURSECRETKEY')
response = s3.list_buckets()
#pprint(response)
my_list = []


my_list.append(response.copy())
#pprint(my_list)

for bucket in response['Buckets']:
    print(bucket['Name'])
