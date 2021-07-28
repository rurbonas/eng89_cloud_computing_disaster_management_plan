import boto3

s3 = boto3.resource('s3')
s3.Object('eng89ron', 'test.txt').delete()

print("File deleted")
