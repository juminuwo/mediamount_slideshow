#!/bin/bash
until R CMD BATCH /home/pi/python_mediamount_slideshow/video.R; do
    sleep 3
done
