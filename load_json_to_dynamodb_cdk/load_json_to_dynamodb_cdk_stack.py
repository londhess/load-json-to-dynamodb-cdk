from aws_cdk import (
    aws_s3 as s3,
    aws_s3_notifications as notification,
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
    core
) 


class LoadJsonToDynamodbCdkStack(core.Stack):

    @property
    def table(self):
        return self._table 

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the S3 bucket
        my_bucket = s3.Bucket(self,"my_s3_bucket_raw")

        #create dynamo db table
        self._table = ddb.Table(
            self, 'Employee',
            partition_key={'name': 'Emp_Id', 'type': ddb.AttributeType.NUMBER}
        )
        
        #Create lambda function
        my_lambda = _lambda.Function(
                            self,
                            id="EventFunction",
                            runtime=_lambda.Runtime.PYTHON_3_7,
                            code=_lambda.Code.asset("lambda"),
                            handler="event.handler" ,
                            environment={
                                "Table_Name":self._table.table_name
                            }                           
        )

        #Add Filters
        filter1=s3.NotificationKeyFilter(prefix="home/",suffix=".json")
        
        #Create Notification
        s3_lambda_notification = notification.LambdaDestination(my_lambda)

        #link s3 and lambda
        my_bucket.add_event_notification(s3.EventType.OBJECT_CREATED,s3_lambda_notification,filter1)
        
        #grant lambda read/write access to lambda function
        self._table.grant_read_write_data(my_lambda)
        _lambda.IFunction.grant_invoke(self,my_lambda)

        #Grant s3 read access to lambda function
        my_bucket.grant_read(my_lambda)
        