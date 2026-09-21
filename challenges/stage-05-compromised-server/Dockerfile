FROM debian:bookworm-slim

RUN useradd -m analyst

COPY src/ /

RUN chown -R root:root /var/log/auth.log /opt/novatech/recovery-note.txt && \
    chmod 644 /var/log/auth.log /opt/novatech/recovery-note.txt && \
    chown analyst:analyst /home/analyst/.bash_history

USER analyst
WORKDIR /home/analyst

CMD ["sleep", "infinity"]
