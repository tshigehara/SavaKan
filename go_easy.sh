#!/bin/sh
sed s/difficulty=hard/difficulty=easy/ /home/pi/minecraft2/server.properties|sudo tee /home/pi/minecraft2/server.properties > /dev/null

