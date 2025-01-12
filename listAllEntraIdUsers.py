from azure.identity import DefaultAzureCredential
import requests

tenantID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
scopeMicrosoftGraph = "https://graph.microsoft.com/.default"

credential = DefaultAzureCredential()
result = credential.get_token(scopeMicrosoftGraph, tenant_id=tenantID)

if result.token:
    print("Access Token.")
else:
    print("Error")

headers = {"Authorization": f"Bearer {result.token}"}
roles_url = "https://graph.microsoft.com/v1.0/roleManagement/directory/roleDefinitions"
response = requests.get(roles_url, headers=headers)

response.raise_for_status()
roles_data = response.json().get('value', [])

for role in roles_data:
    print(role.get('id'), role.get('displayName'))


