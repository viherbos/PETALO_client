# BATCH OF MEASUREMENTS

./socket_client.py -a 5 /data/run1
sleep 7
./socket_client.py -a 5 /data/run2
sleep 7
./socket_client.py -a 5 /data/run3
sleep 7

./socket_client.py -f /data/run1 /data/run1_c
./socket_client.py -f /data/run1 /data/run2_c
./socket_client.py -f /data/run1 /data/run3_c
