#!/bin/bash
while true
do 
 cd ~/Desktop/raspberry_sensors/data
 git add .
 git commit -m "raspberryname `date`"
 git push --set-upstream origin ubuntu
 echo "pushing"
 sleep 20
done
