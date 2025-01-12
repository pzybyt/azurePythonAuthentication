from azure.identity import DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient

credential = DefaultAzureCredential()

#credential = DefaultAzureCredential(exclude_environment_credential=True, exclude_managed_identity_credential=True, exclude_visual_studio_code_credential=True, exclude_shared_token_cache_credential=True )

mySubscriptions = SubscriptionClient(credential)

for subscription in mySubscriptions.subscriptions.list():
    print(subscription.display_name, subscription.subscription_id, subscription.state)

