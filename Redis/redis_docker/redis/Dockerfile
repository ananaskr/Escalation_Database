FROM redis:5.0

RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN sed -i 's/security.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list

RUN apt-get -y update && \
    apt-get -y install wget curl && \
    apt-get -y install netcat && \
    apt-get -y install net-tools && \
    apt-get -y install nano && \
    apt-get -y install openssh-server && \
    apt-get -y autoremove  && \
    rm -rf /var/lib/apt/lists/*

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./redis.conf /etc/redis/redis.conf

COPY ./sshd_config /etc/ssh/sshd_config

CMD ["/start.sh"]
