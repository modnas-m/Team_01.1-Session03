"""
01 - Create a Speckle Model inside an existing Project and Folder

NOTE: Project workspace in this case is: 128262a20c
"""
from main import get_client
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_default_account

# Authenticate
client = SpeckleClient(host="https://app.speckle.systems")
account = get_default_account()
client.authenticate_with_account(account)

# Project ID (where the model will be created)
project_id = "128262a20c"

# Create the model with the folder path
# Use forward slashes to separate folder levels
model = client.model.create(
    project_id=project_id,
    name="team_01.1",
    description="Model created in session03 subfolder",  # optional
    folder_path="homework/session03"  # This targets the nested folder structure
)

print(f"Model created successfully!")
print(f"Model ID: {model.id}")
print(f"Model URL: https://app.speckle.systems/projects/{project_id}/models/{model.id}")