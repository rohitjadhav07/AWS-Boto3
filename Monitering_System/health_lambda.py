import datetime

def lambda_handler(event, context):
    current_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - System health check OK")
    return "OK"