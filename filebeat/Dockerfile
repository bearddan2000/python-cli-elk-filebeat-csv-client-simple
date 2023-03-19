FROM elastic/filebeat:7.12.0

COPY ./dog-demo.csv /usr/share/filebeat/logs

COPY ./filebeat.yml /usr/share/filebeat

EXPOSE 5044

ENV WAIT_VERSION 2.7.2

USER filebeat

ADD --chown=filebeat https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

USER root

CMD ["filebeat", "-e", "--strict.perms=false"]