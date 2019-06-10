
cd `dirname $0`

while [ 1 -eq 1 ]
do

f=1
while [ "${f}" -eq 1 ]
do

f=`gpio -g read 5`
sleep 0.5

done
sudo ./src_led/led01

echo "start"
cd hark
harkmw ./localize.n >log.txt
cd ..
sudo ./src_led/led-clear

done

