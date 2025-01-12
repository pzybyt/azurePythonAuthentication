# Authenticate with DefaultAzureCredential Class
# https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python
subscriptionID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

credential = DefaultAzureCredential()

resource_client = ResourceManagementClient(credential, subscriptionID)
for resource_group in resource_client.resource_groups.list():
    print(resource_group.name)

