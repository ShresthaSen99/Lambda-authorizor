# Lambda-authorizor

This project is mainly to configure a authorizer lambda with api. So to perform any action with the main lambda user needs to make sure that he/she is authorized for it. So they will be passing a token value, if that token value is correct it will aloow the user to perform the actions, incase it's a wrong value it will throw an error. In this case our main lambda's task is to put some data in our dynamodb table.

#How to configure it
* first will create a dynamodb table.
* Will create a rest api. Create a resource.
* Will create a lambda function. It will be our main lambda. We will write down code to get the data from our api and pass it to dynamodb table. We will attach our api tp our lambda.
* Also we need to have a IAM role which have permission for basic lambda execution, dynamodb permissions, also to write down logs in cloudwatch for our each execution.
* once done we can be able to put data through api to dynamodb.
* Then we will create a authorizer in our api. Create a token source.
* Create another lambda function for authorizer. Write down code for it. attach it with our api.
* Now while running it we have to put our token value in headers. Then it will verify the token and pass a IAM policy refer to which our main lambda function will run and do the main task of putting data in dynamodb.
* This way we can secure our lambda function and api.
