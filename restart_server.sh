#! /bin/bash
for pid in $(ps aux|grep linaro |grep logserver.py | awk '{print $2}')
do
kill $pid
done
nohup python logserver.py &
