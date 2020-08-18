import os

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
                              # The absolute URL must match the redirect URI you set
                              # in the app's registration in the Azure portal.

# ENDPOINT = 'https://graph.microsoft.com/v1.0/users/7f328e4a-2819-4383-b1e3-b363e2205627/drives'


# CLIENT_ID = "8b896b8d-a6e6-4f51-85fb-6ec80be7ba3f"
# CLIENT_SECRET = "-k8.HQolPDnTE-3SD8u07pd-nCCGZoHIZu"
# AUTHORITY = "https://login.microsoftonline.com/common"
# # ENDPOINT = 'https://graph.microsoft.com/v1.0/me'
# ENDPOINT = 'https://graph.microsoft.com/v1.0/users/7f328e4a-2819-4383-b1e3-b363e2205627/drives'
# # ENDPOINT = 'https://graph.microsoft.com/v1.0/users/7f328e4a-2819-4383-b1e3-b363e2205627/drives/da70f5a3d869b697/root/children'


# ENDPOINT = 'https://graph.microsoft.com/v1.0/drives/da70f5a3d869b697/root/children'


CLIENT_ID = "87f23b6a-506e-44c7-9ff6-b855fcde3ae9"
CLIENT_SECRET = "a-KhwL4.1l~9s8qDjqt-8CLey5~_~3s9ri"
AUTHORITY = "https://login.microsoftonline.com/f01e930a-b52e-42b1-b70f-a8882b5d043b"
# ENDPOINT = 'https://graph.microsoft.com/v1.0/me'
ENDPOINT = 'https://graph.microsoft.com/v1.0/users/7f328e4a-2819-4383-b1e3-b363e2205627'
# ENDPOINT = 'https://graph.microsoft.com/v1.0/users/7f328e4a-2819-4383-b1e3-b363e2205627/drives'


# CLIENT_ID = "b7b65ec6-502f-4b43-bd11-b7aa1f6b42dd"
# CLIENT_SECRET = "-CuO.eEa-388z11WChGxxSK9J1~0diN~35"
# AUTHORITY = "https://login.microsoftonline.com/f01e930a-b52e-42b1-b70f-a8882b5d043b"
# # ENDPOINT = 'https://graph.microsoft.com/v1.0/me'
# # ENDPOINT = 'https://graph.microsoft.com/v1.0/users/ca18d8a6-b5da-403b-a1ec-c65028cdc316'
# ENDPOINT = 'https://graph.microsoft.com/v1.0/users/ca18d8a6-b5da-403b-a1ec-c65028cdc316/drives'


# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["Files.ReadWrite.All"]

SESSION_TYPE = "filesystem"  # Specifies the token cache should be stored in server-side session
