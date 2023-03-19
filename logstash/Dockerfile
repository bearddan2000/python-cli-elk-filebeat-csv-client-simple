FROM logstash:7.12.0

USER logstash

COPY ./mystash.conf /usr/share/logstash/pipeline

EXPOSE 9600

ENV WAIT_VERSION 2.7.2

ADD --chown=logstash https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait

RUN chmod +x /wait

CMD ["logstash", "-f", "/usr/share/logstash/pipeline/mystash.conf"]