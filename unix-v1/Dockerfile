FROM ubuntu:latest
MAINTAINER littlebutt
WORKDIR /app
RUN apt update && \
    apt install -y --no-install-recommends ca-certificates build-essential \
        git cmake libjson-c-dev libwebsockets-dev sudo python3
RUN git clone https://github.com/jserv/unix-v1.git
RUN git clone --branch 1.6.3 https://github.com/tsl0922/ttyd.git
RUN mkdir ttyd/build
RUN cd ttyd/build && cmake ..
RUN make -C ttyd/build && sudo make -C ttyd/build install
RUN make -C unix-v1
COPY start.sh /app
EXPOSE 8089/tcp
CMD ttyd -p 8089 bash

