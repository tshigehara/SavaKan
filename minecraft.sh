#!/bin/bash
STR=""
STR=$(netstat -a|grep 25565)
echo $STR
if [[ $STR = "" ]]; then
#echo $STR
LINE_ACCESS_TOKEN="QTHIRYGcoF805XY5M8C4ESNn6mpbUyhxqzeB97RS0Iq"
function line_notify() {
  MESSAGE=$1
  curl -X POST -H "Authorization: Bearer ${LINE_ACCESS_TOKEN}" -F "message=$MESSAGE" https://notify-api.line.me/api/notify
}
echo $STR
sudo java -jar /home/pi/minecraft2/server.jar nogui | while read -r line
do
  if [[ $line == *joined\ the\ game* ]]; then echo "${line:33}" | line_notify "$(cut -d ' ' -f 1) がログインしました。" ; fi
  if [[ $line == *left\ the\ game* ]]; then echo "${line:33}" | line_notify "$(cut -d ' ' -f 1) がログアウトしました。" ; fi
done;
else

echo $STR 
fi

