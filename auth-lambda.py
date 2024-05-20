import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('<dynamodb table name>')

def lambda_handler(event, context):
    try:
        # Assuming the request body data is under 'body' key
        body_data = event.get('body')

        if body_data is not None:
            # Assuming the body data is JSON-encoded
            converted_data = json.loads(body_data)
            table.put_item(Item=converted_data)
        else:
            raise Exception("Missing data in request body")

    except json.JSONDecodeError:
        # Handle potential errors if the data is not valid JSON
        print("Error: Invalid JSON data in request body")
        return {
            'statusCode': 400,  # Bad Request
            'body': json.dumps('Invalid JSON data format')
        }
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Error adding data to DynamoDB: {e}")
        return {
            'statusCode': 500,  # Internal Server Error
            'body': json.dumps('An error occurred while processing your request.')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('Data added to DynamoDB successfully!')
    }