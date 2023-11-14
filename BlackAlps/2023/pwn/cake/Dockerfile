FROM ubuntu:22.04
RUN apt-get update && apt-get install -y gcc make
RUN useradd player
WORKDIR /app
COPY cake.c Makefile flag.txt ./
RUN make
CMD ./cake
