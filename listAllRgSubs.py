# https://github.com/MicrosoftDocs/azure-dev-docs/blob/main/articles/python/sdk/authentication/overview.md#use-defaultazurecredential-in-an-application

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

subscriptionID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
credential = DefaultAzureCredential(subscription_id=subscriptionID)

# list all resource groups in the current subscription

resource_client = ResourceManagementClient(credential, subscriptionID)
for resource_group in resource_client.resource_groups.list():
    print(resource_group.name)
    
