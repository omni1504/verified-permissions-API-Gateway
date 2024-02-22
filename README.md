# Example for m2m and user authentication using API Gateway integration pattern and Verified Permissions as a policy store
Simple example of m2m and user auth flow with API GW, Cognito and Verified Permissions

Documentation is all WIP and will be updated as needed



Steps to install:
1. Create a Cognito client and Microsoft Entra ID Enterprise Application following Steps in https://aws.amazon.com/blogs/security/5. how-to-set-up-amazon-cognito-for-federated-authentication-using-azure-ad/
2. [TODO, to be expanded] Create 2 app clients, one for m2m, another - for user authentication. Assign scopes to both using the following naming convention: m2m-*, user-*. Add a custom attribute "adgroups" to Cognito user pool and assign read/write permissions within user app client. Adapt Sign-in behaviour - add Oauth2.0 scopes and authentication methods for user (code-based) and m2m2 (client credentials)
3. Add Lambda layer using lambda-layer.zip file (additional libraries used by Lambda)
4. Create an S3 bucket and upload LambdaAuthorizerCode.zip and LambdaSimpleHTTPResponseCode.zip
5. [TODO, currently still being adapted] Deploy a Cloudformation template SampleVerifiedPermissionsSetup-CFN-template.yaml using parameters from p1, p.3 and p.4.
6. Confirm correct deployment and Lambda codes.
7. Use test_send_to_APIGW.py for testing


Solution Topology (also refer to APIGW-Cognito-Verified-Permissions-0.2.drawio file in the Schemes directory)

User Flow




M2m Flow