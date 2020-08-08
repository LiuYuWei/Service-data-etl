# Base image - ubuntu
FROM ubuntu:18.04

#Setting timezone
ENV TZ Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#Construct the home directory and work directory
RUN addgroup --gid 1001 app 
RUN useradd -u 1001 \
            -G app \
            -d /home/app/workdir \
            -s /sbin/nologin \
            -g app \
            app

#Install python, Set timezone and relation 
RUN apt-get update \
    && apt-get install tzdata \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && apt-get install -y \
    linux-libc-dev \
    python3.6 \
    python3.6-dev \
    python3-pip \
    libyaml-cpp-dev \
    libyaml-dev \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

#Create an app user for the application usage
ENV APP_HOME=/home/app/workdir/

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME
RUN chown -R app:app $APP_HOME

#Install python packages
COPY ./docker/fastapi/requirements.txt $APP_HOME/requirements.txt
RUN pip3 --no-cache-dir install -r $APP_HOME/requirements.txt

#Project data and code
COPY . $APP_HOME
RUN chmod a+w -R $APP_HOME/data/

EXPOSE 5000
ENV PROJECT_PATH=$APP_HOME

#Change User - app
# USER app

#Run api code
ENTRYPOINT [ "/bin/bash" , "-c" , "python3 main.py --framework fastapi"]
