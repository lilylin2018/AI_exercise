from huggingface_hub import snapshot_download

model_name = "BAAI/bge-large-zh-v1.5"
local_dir = "./ai_model"

snapshot_download(repo_id=model_name, local_dir=local_dir)