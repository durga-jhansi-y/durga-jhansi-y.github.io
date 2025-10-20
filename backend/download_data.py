import kagglehub

# Download latest version of NSL-KDD
path = kagglehub.dataset_download("hassan06/nslkdd")

print("Path to dataset files:", path)
