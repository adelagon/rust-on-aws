from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
)
from constructs import Construct

class ServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        # The code that defines your stack goes here

        # example resource
        queue = sqs.Queue(
             self, "ServerlessQueue",
             visibility_timeout=Duration.seconds(300),
        )

        # f = _lambda.Function(self, "hello-rust",
        #         runtime=_lambda.Runtime.PROVIDED.AL2,
        #         handler="not.required",
        #         code=_lambda.Code.from_asset(
                    
        #         )