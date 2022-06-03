from ast import arg
import os,argparse,subprocess
from posixpath import split
import string

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="video url",type=str)
parser.add_argument("--start", help="start time",type=str)
parser.add_argument("--end", help="end time",type=str)
args = parser.parse_args()

startTimes=args.start.split(",")
endTimes=args.end.split(",")



def clipTime(s,e):
    time = " -ss "+s+" -to "+e+" "
    return time


cmd="yt-dlp -o temp.mp4 -S \"ext\" "+args.url
subprocess.run(cmd,shell=True)

if(len(startTimes)!=len(endTimes)):
    print("could not match start and end time")
    exit()

times=map(clipTime,startTimes,endTimes)
for idx,t in enumerate(times):
    trimCmd="ffmpeg " + t +"-i temp.mp4 output/output"+str(idx)+".mp4"
    print(trimCmd)
    subprocess.run(trimCmd,shell=True)

# time=" -ss "+args.start+" -to "+args.end+" "

# subprocess.run(cmd,shell=True)


# trimCmd="./ffmpeg " + time +"-i temp.mp4 output.mp4"
# print(trimCmd)
# subprocess.run(trimCmd,shell=True)
