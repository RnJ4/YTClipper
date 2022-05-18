from ast import arg
import os,argparse,subprocess
import string

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="video url",type=str)
parser.add_argument("--start", help="start time",type=str)
parser.add_argument("--end", help="end time",type=str)
args = parser.parse_args()
cmd="yt-dlp -o temp.mp4 -S \"ext\" "+args.url

time=" -ss "+args.start+" -to "+args.end+" "

subprocess.run(cmd,shell=True)


trimCmd="./ffmpeg " + time +"-i temp.mp4 -c copy output.mp4"
print(trimCmd)
subprocess.run(trimCmd,shell=True)
