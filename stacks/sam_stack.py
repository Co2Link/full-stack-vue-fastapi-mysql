from aws_cdk import Stack
from aws_cdk import aws_apigateway as agt
from aws_cdk import aws_lambda as lambda_
from constructs import Construct


class SamStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        backend_lambda = lambda_.DockerImageFunction(
            self,
            "BackendLambda",
            memory_size=128,
            code=lambda_.DockerImageCode.from_image_asset(
                directory="backend", file="lambda_Dockerfile"
            ),
        )

        agt.LambdaRestApi(
            self,
            "BackendApi",
            handler=backend_lambda,
        )
