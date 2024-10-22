FROM gcc:14.2.0

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY fakeit .
COPY fake_flag.txt .
COPY flag.txt .
COPY ynetd .

RUN chown -R root:root /home/ctf
USER ctf
EXPOSE 6969
CMD ./ynetd -p 6969 ./fakeit