import os
from huggingface_hub import HfApi

HF_TOKEN = os.environ["HF_TOKEN"]
api = HfApi(token=HF_TOKEN)
username = api.whoami()["name"]

backend_repo = f"{username}/superkart-sales-forecast-backend"
frontend_repo = f"{username}/superkart-sales-forecast-frontend"

for repo_id in [backend_repo, frontend_repo]:
    api.create_repo(
        repo_id=repo_id,
        repo_type="space",
        space_sdk="docker",
        private=False,
        exist_ok=True,
    )

api.upload_folder(
    folder_path="backend",
    repo_id=backend_repo,
    repo_type="space",
    commit_message="Deploy SuperKart Flask backend",
)

backend_url = f"https://{username}-superkart-sales-forecast-backend.hf.space"
api.add_space_variable(
    repo_id=frontend_repo,
    key="BACKEND_URL",
    value=backend_url,
    description="Public SuperKart backend API URL",
)

api.upload_folder(
    folder_path="frontend",
    repo_id=frontend_repo,
    repo_type="space",
    commit_message="Deploy SuperKart Streamlit frontend",
)

print(f"BACKEND_SPACE=https://huggingface.co/spaces/{backend_repo}")
print(f"FRONTEND_SPACE=https://huggingface.co/spaces/{frontend_repo}")
print(f"BACKEND_APP={backend_url}")
