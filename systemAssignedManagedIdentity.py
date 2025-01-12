#!/usr/bin/env python3
# Authenticate with a system-assigned managed identity
# Download modules https://pypi.org/

subscriptionID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

from azure.identity import ManagedIdentityCredential
from azure.mgmt.resource import ResourceManagementClient

credential = ManagedIdentityCredential()

resource_client = ResourceManagementClient(credential, subscriptionID)
for resource_group in resource_client.resource_groups.list():
    print(resource_group.name)