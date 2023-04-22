git pull
docker build -t textweb .
docker stop textweb
docker rename textweb textweb.bak
docker run -dit --name=textweb -p 88:88 textweb
