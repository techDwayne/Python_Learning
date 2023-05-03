# write an amazon lambda function to output content type of a file uploaded to an S3 bucket
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    response = s3.get_object(Bucket=bucket, Key=key)
    content_type = response['ContentType']
    print(content_type)
    return content_type

#