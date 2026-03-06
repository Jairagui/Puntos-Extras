import json
import boto3

dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('KanbanCards')


def lambda_handler(event, context):
    # Sacar el ID de la URL
    id_tarea = event['pathParameters']['id']

    # Borrarlo directo de la base de datos
    tabla.delete_item(Key={'id': id_tarea})

    return {'statusCode': 200, 'body': '"Card eliminada"'}