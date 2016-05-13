#!/bin/bash
#top |grep "Cpu" 查看cpu占用情况
#每一分钟记录一次cpu信息
#每小时备份并删除一次
#每天删除一次备份

#crontab -l | grep -v '^#' > mycrontab

echo "1 * * * * echo -n $(date +%Y-%m-%d-%H-%M) >>/tmp/cpu.log && top |grep "Cpu" >>/tmp/cpu.log " >> mycrontab
echo "* */1 * * * cat /tmp/cpu.log >> /tmp/cpu_old.log && rm /tmp/cpu.log" >>mycrontab
echo "* * */1 * * rm /tmp/cpu_old.log" >>mycrontab

crontab mycrontab
