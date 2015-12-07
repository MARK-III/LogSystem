#! /bin/bash
for pid in $(ps aux|grep linaro |grep server.py | awk '{print $2}')
do
kill $pid
done
nohup python server.py &
