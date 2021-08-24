#!/bin/sh
sed s/difficulty=easy/difficulty=hard/ /home/pi/minecraft2/server.properties|sudo tee /home/pi/minecraft2/server.properties > /dev/null
#sed s/difficulty=easy/difficulty=hard/ /home/pi/minecraft2/server.properties > temp.log

