import os
import sys
import dockermap.api

docker_url = "unix://var/run/docker.sock"
tag_name = sys.argv[1]


docker_conn = dockermap.api.DockerClientWrapper(docker_url)
docker_file = dockermap.api.DockerFile('centos7/hw', maintainer='Hrunyk Yurii')
docker_file.run_all('yum -y update')
docker_file.run_all('yum -y install httpd')
docker_file.run_all('systemctl start httpd')
docker_file.run('echo "Homework6!" > /var/www/html/index.html')


docker_conn.build_from_file(docker_file, tag_name)

