#!/bin/bash
while true; do 
    echo "Menu Options:"
    echo "1) Hello World (prints 'Hello World!' to the screen)"
    echo "2) Ping (pings your computer's loopback address)"
    echo "3) IP info (prints your computer's network adapter info)"
    echo "4) Exit"
    read -p "Please select an option number 1-4: " user_option
    case $user_option in
        1) 
            echo "Hello World!";;
        2) 
            ping -c 4 127.0.0.1;;
        3)
            ifconfig || ip a || ipconfig;;
        4) 
            echo "Goodbye."
            exit 0;;
        *)
            echo "Please select a number between 1 and 4.";;
    esac
done
