# Puntos-Extras
¿Qué tecnología elegiste para el cómputo y por qué?
Usé AWS Lambda con API Gateway porque es serverless. Así me evité tener que levantar y configurar una instancia EC2 entera solo para unas funciones sencillas. Es mucho más rápido de armar y no hay que administrar ningún servidor.

¿Qué tecnología elegiste para almacenamiento y por qué?
Elegí DynamoDB porque, al ser NoSQL, es ideal para guardar los datos en formato JSON tal cual llegan en las peticiones. Aparte, se conecta directito con Lambda sin tener que meterme en configuraciones complicadas de red o credenciales.

¿Qué tecnologías utilizarías para notificar al usuario que una tarea con estado backlog o doing está próxima a vencer?
Armaría una combinación de tres servicios: usaría EventBridge para programar un cron que corra todos los días; ese evento dispararía una Lambda que busque en la base de datos las tareas a punto de vencer.
