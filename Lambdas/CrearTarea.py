import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('KanbanCards')


def lambda_handler(event, context):
    body = json.loads(event['body'])

    # Validar estados
    if body.get('estado') not in ['backlog', 'doing', 'done']:
        return {'statusCode': 400, 'body': '"Estado invalido"'}

    # Validar formato de fechas
    try:
        datetime.fromisoformat(body['fecha_limite'])
        datetime.fromisoformat(body['fecha_creado'])
    except:
        return {'statusCode': 400, 'body': '"Formato de fecha invalido"'}

    # Generar ID, meterlo al body y guardar todo directo
    body['id'] = str(uuid.uuid4())
    tabla.put_item(Item=body)

    return {
        'statusCode': 200,
        'body': json.dumps({'id': body['id']})
    }