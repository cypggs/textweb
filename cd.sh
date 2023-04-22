git pull
docker build -t textweb .
docker stop textweb
docker rename textweb textweb.bak`date +%m-%d`
docker run -dit --name=textweb -p 88:88 textweb
