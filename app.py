import boto3
from fastapi import FastAPI
import uvicorn

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CounterTable')

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck():
  try:
    table.get_item(Key={'CounterId': 'Counter1'})
    return {"status": "ok"}
  except Exception as e:
    return {"status": "error"}

@app.get("/")
async def root():
  response = table.update_item(
        Key={'CounterId': 'Counter1'},
        UpdateExpression='ADD #count :incr',
        ExpressionAttributeNames={'#count': 'Count'},
        ExpressionAttributeValues={':incr': 1},
        ReturnValues='UPDATED_NEW'
    )
  
  return {"counter": response['Attributes']['Count']}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)