# BATCH OF MEASUREMENTS

python socket_client.py -r
for i in {1..4}
do
python socket_client.py -a 5400 timingS
sleep 5410
done

wait $!

python socket_client.py -f timingS 4
