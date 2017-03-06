import os
import sys
import dockermap.api

docker_url = "unix://var/run/docker.sock"
tag_name = sys.argv[1]

docker_conn = dockermap.api.DockerClientWrapper(docker_url)
docker_file = dockermap.api.DockerFile('centos7/hw', maintainer='Hrunyk Yurii')

docker_conn.build_from_file(docker_file, tag_name)
