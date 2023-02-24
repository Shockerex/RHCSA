useradd -m -p $(openssl passwd -1 "LaLiga-rules29") malvin

echo "Welcome to W Corp" > /home/malvin/welcome.txt

chmod 440 /home/malvin/welcome.txt