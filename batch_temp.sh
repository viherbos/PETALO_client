python socket_client.py -r

python socket_client.py -d V2 12
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 11
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 10
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 9
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 8
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 7
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 6
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 5
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -d V2 4
sleep 2400
python socket_client.py -a 900 temp_sweep
sleep 910

python socket_client.py -t
sleep 60

wait $!
python socket_client.py -f temp_sweep 10

