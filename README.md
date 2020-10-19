# DJANGO_CARDREADER
Classification model to recognize cards and pytesseract for text extraction from the card are implemented using Django  

### Install requierments.txt  

## Before starting the server, unzip LIVE/Model/classifier2.zip in the same dir  

# How it works:

from cmd start the server by running `python manage.py runserver`  
In the browser goto route `localhost:8000/live/detect`  

**This is how the page looks like:**  

![page](https://github.com/luckyCasualGuy/DJANGO_CARDREADER/blob/main/imgs/page.png)

## Install IP webcam app on your phone to use mobile camera as your feed  

[Download Link](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US&gl=US)

![ipwebcam](https://github.com/luckyCasualGuy/DJANGO_CARDREADER/blob/main/imgs/ipwebcam.png)

setup and start the server from your mobile device.  
Put the ip link provided to you (After starting the server) in the set box.  

**If your Ip is incorrect/ you are not connected to same newtwork / Server is not running you will get this error**  

![error](https://github.com/luckyCasualGuy/DJANGO_CARDREADER/blob/main/imgs/error.png)

This is where you will see the confidence of your card. The classifier is not perfect, prototype was used inorder to reduce file size.  
wait for 5 green confidence ticks for results.  

green ticks:  

![page](https://github.com/luckyCasualGuy/DJANGO_CARDREADER/blob/main/imgs/greentick.png)

red ticks:  

![page](https://github.com/luckyCasualGuy/DJANGO_CARDREADER/blob/main/imgs/redtick.png)

This is how you get results after successful predictions:  

![page](https://github.com/luckyCasualGuy/DJANGO_CARDREADER/blob/main/imgs/detection.png)


You may not get perfect predictions due to various reasons, but the results are good enough. This project is just a showcase of DL models on Django !!
Filtering will be added later when I have more free time.
