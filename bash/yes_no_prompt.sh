#!/bin/bash
echo "Do you want to continue ?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) echo "Do something"; break;;
        No ) exit;;
    esac
done
