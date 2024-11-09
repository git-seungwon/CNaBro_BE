import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

docker_username = os.getenv("DOCKER_USERNAME")
docker_filename = os.getenv("DOCKER_FILENAME")

build_command = f"docker build -t {docker_username}/{docker_filename} ."
print(f"명령어 실행 중: {build_command}")
subprocess.run(build_command, shell=True, check=True)

pull_command = f"docker push {docker_username}/{docker_filename}"
print(f"명령어 실행 중: {pull_command}")
subprocess.run(pull_command, shell=True, check=True)

print("Docker 명령어가 완료되었습니다.")