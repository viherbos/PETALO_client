# BATCH OF MEASUREMENTS

python socket_client.py -r

python socket_client.py -d ON
sleep 60
python socket_client.py -a 300 temp1
sleep 310
python socket_client.py -d OFF
sleep 3600

python socket_client.py -d ON
sleep 300
python socket_client.py -a 300 temp1        
sleep 310
python socket_client.py -d OFF
sleep 3600

python socket_client.py -d ON
sleep 900
python socket_client.py -a 300 temp1        
sleep 310
python socket_client.py -d OFF
sleep 3600

python socket_client.py -d ON
sleep 2700
python socket_client.py -a 300 temp1        
sleep 310
python socket_client.py -d OFF
sleep 3600

python socket_client.py -d ON
sleep 8100
python socket_client.py -a 300 temp1        
sleep 310
python socket_client.py -d OFF
sleep 3600


wait $!
python socket_client.py -f temp1 5

