# Dockerfiles
Docker files for machine learning and robotics

## Compiling
```bash
cd ~/dockerfiles/{pkg}
docker build --tag {tag} -f {file_name} .
```

## Running
Command to get a bash (/bin/bash) from the container `rmiyagusuku/dlbox:base-9.0` \ 
Container also has GPU capabilities (--runtime=nvidia) \
and mounts the home directory to save data (-V /home:/home)

```bash
docker run --runtime=nvidia --rm -it \
    -v /home:/home \
    rmiyagusuku/dlbox:base-9.0 \
    /bin/bash
```

When running a hub version add the following options to allow the docker to use PAM authentication \
also, if no command is specified (as bash in the previous example), the container automatically launches a hub at port 8000

```bash
docker run --runtime=nvidia --rm -it \
    --user $(id -u):$(id -g) \
    -v /etc/sudoers:/etc/sudoers:ro \
    -v /etc/pam.d:/etc/pam.d:ro \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/shadow:/etc/shadow:ro \
    rmiyagusuku/dlbox:hub
```

For the ros versions it may be usefull to share the network with the host, 
so other ros processes can be launch from the host and still connect with the container 
(such as rviz for visualization)

```bash
docker run --runtime=nvidia --rm -it \
    --net=host \
    rmiyagusuku/ros:base
```

Most containers are not set up with users or allow running GUIs, yolo containers do \
To enable GUI add `DISPLAY` and share `/tmp/.X11-unix` - 
more details in this [post](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker)

```bash
docker run --runtime=nvidia --rm -it \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    rmiyagusuku/yolov2:gpu
```
