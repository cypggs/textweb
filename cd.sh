git pull
docker build -t textweb .
docker stop textweb
docker rename textweb textweb.bak`date +%m-%d`
#docker run -dit --name=textweb --network my_network -p 88:88 textweb
docker run -dit --name textweb --restart always -p 88:88 -v ./contents.db:/app/contents.db textweb

