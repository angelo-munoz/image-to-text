import json
import urllib.parse
import boto3
from decimal import Decimal

print('Loading function')

# s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

# --------------- Helper Functions to call Rekognition APIs ------------------
def detect_faces(bucket, key):
    response = rekognition.detect_faces(Image={"S3Object": {"Bucket": bucket, "Name": key}})
    return response

def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})    
    return response

def index_faces(bucket, key):
    # Note: Collection has to be created upfront. Use CreateCollection API to create a collecion.
    #rekognition.create_collection(CollectionId='BLUEPRINT_COLLECTION')
    response = rekognition.index_faces(Image={"S3Object": {"Bucket": bucket, "Name": key}}, CollectionId="BLUEPRINT_COLLECTION")
    return response


def handler(event, context):
    """S3 event handler function

    Parameters
    ----------
    event: dict, required
        S3 Lambda Input Format

        Event doc: https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    null. Asynchronous call        
    """
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    #key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        # print("getting object from s3")
        # response = s3.get_object(Bucket=bucket, Key=key)
        # print("CONTENT TYPE: " + response['ContentType'])
        
        print("sending object to rekognition")
        # Calls rekognition DetectFaces API to detect faces in S3 object
        response=rekognition.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':key}})
                        
        textDetections=response['TextDetections']
        print ('Detected text\n----------')
        detectedText = ""
        for text in textDetections:
            if text['Type']=="LINE":
                detectedText += text['DetectedText'] + " "
                #print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                #print ('Id: {}'.format(text['Id']))
                #if 'ParentId' in text:
                #    print ('Parent Id: {}'.format(text['ParentId']))
                #print ('Type:' + text['Type'])
                #print()
        print(detectedText)

        print("sending text to dynamodb")
        # Sample code to write response to DynamoDB table 'MyTable' with 'PK' as Primary Key.
        # Note: role used for executing this Lambda function should have write access to the table.
        #table = boto3.resource('dynamodb').Table('MyTable')
        #labels = [{'Confidence': Decimal(str(label_prediction['Confidence'])), 'Name': label_prediction['Name']} for label_prediction in response['Labels']]
        #table.put_item(Item={'PK': key, 'Labels': labels})
        #return response['ContentType']
        return len(textDetections)
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e