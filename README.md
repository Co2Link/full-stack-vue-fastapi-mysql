# full-stack-vue-fastapi-mysql
CDK App


## Develop
### Run local api server for backend
```
cdk synth
```
Build SamStack
```
sam build -t cdk.out\SamStack.template.json
```
Start local api server
```
sam local start-api -t cdk.out\SamStack.template.json
```
