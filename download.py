import boto3

s3 = boto3.client('s3')
s3.download_file('eng89ron', 'test.txt', 'test2.txt')

print("File downloaded")
