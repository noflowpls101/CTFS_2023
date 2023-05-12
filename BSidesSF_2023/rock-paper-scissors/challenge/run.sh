sudo docker build -t $1 .
sudo docker run -p 8000:8000 -it $1