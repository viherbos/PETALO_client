# BATCH OF MEASUREMENTS

python socket_client.py -r
for i in {1..50}
do
python socket_client.py -d ON
sleep 30
var=$[$RANDOM % 10]
sleep $var
python socket_client.py -a 900 timing_ONOFF2
sleep 910
python socket_client.py -d OFF
sleep 30
var=$[$RANDOM % 10]
sleep $var
done

wait $!

python socket_client.py -f timing_ONOFF2 50
