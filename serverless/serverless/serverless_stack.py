from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

from constructs import Construct

class ServerlessStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        rust_handler = _lambda.Function(self, "hello-rust",
                runtime=_lambda.Runtime.PROVIDED_AL2,
                handler="not.required",
                code=_lambda.Code.from_asset(
                    config["functions"]["rust"]["hello"]
                )
        )


        apigw.LambdaRestApi(
            self, "RustAPIEndpoint",
            handler=rust_handler
        )
