#!/usr/bin/env bash
# Author : Lyhour Chhen
# Script : Alias for KOOMPI USER :D

USER=whoami
location=~/.bashrc
echo "--------------------------------------------------------"
echo "Welcome to automat Alias Script"
echo "Decription : "
echo "This script let u to create shortcut on KOOMPI OS"
echo "--------------------------------------------------------"
#Ask for Softcut
echo "Enter the Commend u want to change:" && read commend

#Ask For Commend
echo "Enter the shortcut u want to define :"
read softcut

#Ask for Decription for the commend
echo "Enter any Decription"
read Decription

echo "----------------------"
echo "Your new commends"
echo "$commend ===> $softcut"
echo "----------------------"
echo "Decription ==> $Decription"

echo "=========================="
echo "alias $softcut='$commend'">>$location


echo "Execute the alias has been successfully :P"
source ~/.bashrc
echo "Exit the program"
