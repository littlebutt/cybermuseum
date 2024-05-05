FROM ubuntu:latest
MAINTAINER littlebutt
WORKDIR /app
RUN apt update && \
    apt install -y --no-install-recommends ca-certificates build-essential \
    git curl cmake libjson-c-dev libwebsockets-dev sudo
RUN curl https://www.python.org/ftp/python/src/Python-0.9.1.tar.gz -o python-0.9.1.tar.gz
RUN tar -xf python-0.9.1.tar.gz
RUN make -C python-0.9.1/src
RUN git clone --branch 1.6.3 https://github.com/tsl0922/ttyd.git
RUN mkdir ttyd/build
RUN cd ttyd/build && cmake ..
RUN make -C ttyd/build && sudo make -C ttyd/build install
COPY start.sh /app
EXPOSE 8090/tcp
CMD ttyd -p 8090 bash