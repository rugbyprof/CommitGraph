#!/bin/bash

case "$1" in 
start)
   /path/to/fakecommit.sh &
   echo $!>/var/run/fakecommit.pid
   ;;
stop)
   kill `cat /usr/local/bin/fakecommit.pid`
   rm /usr/local/bin/fakecommit.pid
   ;;
restart)
   $0 stop
   $0 start
   ;;
status)
   if [ -e /var/run/fakecommit.pid ]; then
      echo fakecommit.sh is running, pid=`cat /var/run/fakecommit.pid`
   else
      echo fakecommit.sh is NOT running
      exit 1
   fi
   ;;
*)
   echo "Usage: $0 {start|stop|status|restart}"
esac

exit 0 