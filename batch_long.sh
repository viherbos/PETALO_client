# BATCH OF MEASUREMENTS

python socket_client.py -r

python socket_client.py -d ON 12
sleep 60
python socket_client.py -a 2400 mu_LONG
sleep 2410
python socket_client.py -a 2400 mu_LONG
sleep 2410


wait $!
python socket_client.py -f mu_LONG 2

