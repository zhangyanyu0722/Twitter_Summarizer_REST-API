import os
def image_to_video(keyword):
	args = "ffmpeg -r 1/3 -f image2 -s 1920x1080 -start_number 1 -i img/" + keyword + "%d.png -vframes 1000 -vcodec libx264 -crf 25  -pix_fmt yuv420p" + "videos/"+keyword + ".avi"
	os.system(args)
