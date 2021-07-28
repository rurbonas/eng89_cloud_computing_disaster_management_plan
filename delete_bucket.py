import boto3

s3 = boto3.client('s3')
bucket = 'eng89ron'
response = s3.delete_bucket(Bucket=bucket)

print("Bucket deleted")
