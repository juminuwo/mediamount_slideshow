system("sudo hdparm -W0 /dev/sda") # disable write-cache for first plugged in drive
videos <- grep('mp4$|avi$', list.files(path = '/media', full.names = T, recursive = TRUE), value = T)
for(i in videos) system(paste0("omxplayer -b ", '"', i, '"'))
system("/home/pi/python_mediamount_slideshow/slideshow.py /media/")
stop()
