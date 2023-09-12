#!/bin/bash
cd ~/Desktop/data
python "sensors.py"
while true
do
 git add .
 git commit -m "raspberry3 `date`"
 git push origin
 echo "pushing"
 sleep 20
done
