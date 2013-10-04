Lightroom
=========

A Facebook Hackathon project:  provide API access to an array of lights, and allow
user-submitted javascript to manipulate their state.

## Setup

This setup assumes you are using Ubuntu (and uses upstart).

You will need the following support packages installed:

```
apt-get install nginx python-virtualenv
```

### Python setup

Check this project out into `/srv/lightroom/lightroom`:

```
mkdir -p /srv/lightroom
git clone https://github.com/vhata/lightroom.git /srv/lightroom/lightroom
```

Create the virtualenv for lightroom:

```
virtualenv /srv/lightroom
/srv/lightroom/bin/pip install -r /srv/lightroom/lightroom/requirements.txt
```

### Docker setup

Install docker as per http://docs.docker.io/en/latest/installation/ubuntulinux/

Once this is done, you will need to create a docker image for the node.js sandbox.
These instructions were taken from http://kuhnza.com/2013/03/27/docker-makes-creating-secure-sandboxes-easier-than-ever/

Start a docker base image with:

```
sudo docker run -i -t ubuntu /bin/bash
```

Inside the image, run the following commands to install nodejs.  The first line is
a hack to make sure that the universe repository is in your source.list.

**Do not exit the shell after running these commands.**

```
sed -i -e 's/main/main universe/' /etc/apt/sources.list
apt-get update
apt-get install python-software-properties python g++ make
add-apt-repository ppa:chris-lea/node.js
apt-get update
apt-get install nodejs
```

Once this is complete, open **another shell** and run `sudo docker ps`.  This
will give you the ID of the running container.  You need to save this container
with the command `sudo docker commit [container ID] node`.

You can check that it was created with `sudo docker images`.

### Nginx setup

Copy `conf/lightroom-nginx.conf` from this repository to `/etc/nginx/sites-enabled/lightroom` and restart nginx.

In addition, you will need to copy `conf/lightroom-upstart.conf` to `/etc/init/lightroom.conf` and run `start lightroom`.

