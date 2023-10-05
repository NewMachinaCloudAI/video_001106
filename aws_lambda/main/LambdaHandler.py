import json
import boto3

def lambda_handler(event, context):
    
    # Log to console
    print("File Uploaded - invoked by Trigger")
    
    # Document
    s3BucketName = "video-000110-bucket"
    documentName = "video-001106/Input-Text-In-Image.png"

    # Amazon Textract client
    textract = boto3.client('textract')

    # Call Amazon Textract
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': documentName
                }
    })

    print(response)

    # Print detected text
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print ('\033[94m' +  item["Text"] + '\033[0m')
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
