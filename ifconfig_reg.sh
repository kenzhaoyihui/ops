#!/bin/bash
#Author : 2993614148@qq.com

#获得网卡的数量
a=`ifconfig |sed -n "/^eth[0-9]/p"|wc -l`

#声明数组key为关联数组，也就是hash
declare -A key

#进入循环，每次循环找到该网卡的ip地址，并作为关联数组key的值
for((j=0;j<a;j++))
do
key[eth$j]=`ifconfig eth$j |grep 'inet addr' |awk '{print $2}'\ |awk  -F  ":"  '{print $2}'`
done 

#遍历哈希key，取关系数组的所有键，输出其网卡及对应的值
for value in ${!key[@]}
do
 echo $value=${key[$value]}
done
