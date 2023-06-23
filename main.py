from ast import arg
import os,argparse,subprocess
import string

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="video url",type=str)
parser.add_argument("--start", help="start time",type=str)
parser.add_argument("--end", help="end time",type=str)
args = parser.parse_args()
cmd="yt-dlp -g -S \"ext\" "+"\""+args.url+"\""
"""
cmd="yt-dlp -g --youtube-skip-dash-manifest -S \"ext\" "+"\""+args.url+"\""
"""

startTimes=args.start.split(",")
endTimes=args.end.split(",")

def clipTime(s,e):
    time = " --download-sections *"+s+"-"+e
    return time

if(len(startTimes)!=len(endTimes)):
    print("could not match start and end time")
    exit()




times=map(clipTime,startTimes,endTimes)
for idx,t in enumerate(times):
    trimCmd="yt-dlp -S \"ext\" "+"\""+args.url+"\""+t
    trimCmd+=" -o output/output"+str(idx)+".mp4"
    print(trimCmd)
    subprocess.run(trimCmd,shell=True)

