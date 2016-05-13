#!/bin/bash

while true;do

    ps aux | grep  ssh1.exp | grep -v grep

    if [ $? -ne 0 ];then
        /usr/bin/expect /root/shell/ssh1.exp
    fi

done

#  ssh1.exp 

#!/usr/bin/expect 

echo "set port:" 
read port
echo "set user:"
read user
echo "set host:" 
read host
echo "set password:"
read password
set timeout -1  

spawn ssh -4 -D $port $user@$host
expect {
    "yes/no" { send "yes\r";exp_continue}
    "*password:*" {send "${password}\r";exp_continue}
    }
expect eof
                                 


spawn ssh -4 -D $port $user@$host
expect {
    "yes/no" { send "yes\r";exp_continue}
    "*password:*" {send "${password}\r";exp_continue}
    }
expect eof
