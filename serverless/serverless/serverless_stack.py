from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
)
from constructs import Construct

class ServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        f = _lambda.Function(self, "hello-rust",
                runtime=_lambda.Runtime.PROVIDED_AL2,
                handler="not.required",
                code=_lambda.Code.from_asset(
                    "/artifacts/cdk-deploy/RustBinaries/serverless/lambda/hello/target/lambda/hello"
                )
        )