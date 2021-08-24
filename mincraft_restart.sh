#!/bin/bash
systemctl stop minecraft
systemctl start minecraft
LINE_ACCESS_TOKEN="QTHIRYGcoF805XY5M8C4ESNn6mpbUyhxqzeB97RS0Iq"
function line_notify() {
  MESSAGE=$1
  curl -X POST -H "Authorization: Bearer ${LINE_ACCESS_TOKEN}" -F "message=$MESSAGE" https://notify-api.line.me/api/notify
}

 line_notify "Pipper:サーバーをRebootしました"

