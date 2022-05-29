# defines the base image
FROM python:3.8.10

# creates a working directory called project
WORKDIR /project

# adds all files to the working directory
ADD . /project

# upgrades pip and installs required modules/dependencies in my container
RUN \
    pip3 -q install pip --upgrade \
    && pip install -r requirements.txt

# forward the request from port 5000 on the host to port 5000 in the container
EXPOSE 5000

# lEt'S gOoOoOoO !!
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]