import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('KanbanCards')


def lambda_handler(event, context):
    body = json.loads(event['body'])
    id_tarea = event['pathParameters']['id']

    # Validar estado
    if body['estado'] not in ['backlog', 'doing', 'done']:
        return {'statusCode': 400, 'body': '"Estado no valido"'}

    # Validar fecha
    try:
        datetime.fromisoformat(body['fecha_limite'])
    except:
        return {'statusCode': 400, 'body': '"Fecha no valida"'}

    # Actualizar la base de datos
    tabla.update_item(
        Key={'id': id_tarea},
        UpdateExpression="set estado=:e, fecha_limite=:f",
        ExpressionAttributeValues={
            ':e': body['estado'],
            ':f': body['fecha_limite']
        }
    )

    return {'statusCode': 200, 'body': '"Actualizado"'}