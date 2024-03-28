print("""
-----------------------------------------------------------------
✨ Get Tilted!
-----------------------------------------------------------------
""".strip())

docker_build('publisher', './services/publisher/')
docker_build('subscriber', './services/subscriber/')
k8s_yaml(['deploy_k8s.yml'])

