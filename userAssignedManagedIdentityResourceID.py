# Authenticate with a user-assigned managed identity
# https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python
# user assigned managed identity: userIssignedIanagedIdentityReader

# pythonvmidentity 
resourceID = "/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourceGroups/pythonInAzure/providers/Microsoft.ManagedIdentity/userAssignedIdentities/pythonvmidentity"
subscriptionID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

from azure.identity import ManagedIdentityCredential
from azure.mgmt.resource import ResourceManagementClient

credential = ManagedIdentityCredential(identity_config={"resource_id": resourceID })

resource_client = ResourceManagementClient(credential, subscriptionID)
for resource_group in resource_client.resource_groups.list():
    print(resource_group.name)