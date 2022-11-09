import aws_cdk as cdk

from stacks import SamStack, VpcStack

app = cdk.App()
VpcStack(app, "VpcStack")
SamStack(app, "SamStack")

app.synth()
