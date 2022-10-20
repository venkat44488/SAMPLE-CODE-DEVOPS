file=$1
exit_status=0
servers=(`cat $file`)

for ip in ${servers[@]}
do
        if ping -c 1 -W 3 $ip 1> /dev/null 2> /dev/null; then
                echo $?
                echo "$ip ✓"
        else
                echo $?
                exit_status=1
                echo "$ip ✗"
        fi
done
exit $exit_status

## run this file as ./uptime.sh /path/to/servers.txt
## keep all the server ip in servers.txt
