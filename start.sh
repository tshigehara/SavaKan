#!/bin/sh

#screenの名前
SCREEN_NAME='minecraft'

#screen -UAmdS $SCREEN_NAME java -server -Dfile.encoding=UTF-8 -Xms8G -Xmx8G -jar /home/pi/minecraft2/server.jar

screen -UAmdS $SCREEN_NAME java -server -Dfile.encoding=UTF-8 -jar /home/pi/minecraft2/server.jar

