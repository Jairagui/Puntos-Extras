import json
import boto3

tabla = boto3.resource('dynamodb').Table('KanbanCards')

def lambda_handler(event, context):
    respuesta = tabla.scan()
    return {
        'statusCode': 200,
        'body': json.dumps(respuesta.get('Items', []))
    }