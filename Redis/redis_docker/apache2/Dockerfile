FROM centos:7

ENV DEBIAN_FRONTEND noninteractive

RUN yum -y update && \
	yum -y install nc && \
	yum -y install httpd php && \
	yum -y install curl && \
	yum -y install nano && \
	yum -y install php-curl && \
	yum -y install crontabs

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80

ENTRYPOINT ["/usr/sbin/init"]