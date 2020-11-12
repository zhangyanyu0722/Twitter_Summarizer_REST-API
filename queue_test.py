from tweepy_get import tweepy_get
from image2video import image_to_video
from queue_sys import queue_1
import os, sys

# keyNames = ['BU_Tweets', 'BU_ece', 'BostonDynamics', 'BBCWorld', 'WHO', 'TIME', 'celtics', 'nytimes', 'washingtonpost', 'BillGates']
number_thread = 4
queue_1(sys.argv[1:], number_thread)





