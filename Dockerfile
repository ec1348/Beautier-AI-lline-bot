From ubuntu:20.04

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# install python 3.6
RUN sudo apt-get update
RUN sudo apt-get -y upgrade
RUN unzip psGAN_module.zip
RUN sudo apt-get install -y python3.6 
RUN sudo apt-get install -y python3-pip
RUN pip3 install pip --upgrade
# install pytorch torchvision dlib
RUN pip3 install pip3 install torch==1.5.0+cpu torchvision==0.6.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN mkdir -p PSGAN-master/dlib
RUN git clone https://github.com/davisking/dlib.git PSGAN-master/dlib/
RUN cd PSGAN-master/dlib
RUN python3 setup.py install
RUN cd ../../


# Install production dependencies.
RUN pip3 install -r requirements.txt