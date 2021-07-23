From ubuntu:20.04

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# install python 3.6
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install zip 
RUN unzip psGAN_module.zip 
RUN apt-get install -y python3.6 
RUN apt-get install -y python3-pip
RUN pip3 install pip --upgrade
# install pytorch torchvision dlib
RUN pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN apt-get install -y git
RUN mkdir -p PSGAN-master/dlib
RUN git clone https://github.com/davisking/dlib.git PSGAN-master/dlib/
RUN cd PSGAN-master/dlib/ \
    python3 setup.py install
    # cd ../../


# Install production dependencies.
RUN pip3 install -r requirements.txt

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :$PORT --workers 4 --threads 8 --timeout 0 app:app