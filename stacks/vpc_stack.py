from aws_cdk import Stack, aws_ec2 as ec2, CfnOutput
from constructs import Construct


class VpcStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            "VPC",
            max_azs=2,
            ip_addresses=ec2.IpAddresses.cidr("10.0.0.0/16"),
            # configuration will create 2 groups in 2 AZs = 4 subnets.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC, name="Public", cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED, name="DB", cidr_mask=24
                ),
            ],
            nat_gateways=0,
        )
        CfnOutput(self, "Output", value=self.vpc.vpc_id)
