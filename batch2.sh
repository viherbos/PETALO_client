# BATCH OF MEASUREMENTS

python socket_client.py -r
for i in {1..150}
do
python socket_client.py -d ON
sleep 30
var=$[$RANDOM % 10]
sleep $var
python socket_client.py -a 450 timing_ONOFF3
sleep 460
python socket_client.py -d OFF
sleep 30
var=$[$RANDOM % 10]
sleep $var
done

wait $!
python socket_client.py -f timing_ONOFF3 150
