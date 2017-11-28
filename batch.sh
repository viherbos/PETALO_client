# BATCH OF MEASUREMENTS

./socket_client.py -r
./socket_client.py -a 5 timing
./socket_client.py -a 5 timing
./socket_client.py -a 5 timing
wait $!

./socket_client.py -f timing 3
