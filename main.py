from ast import arg
import os,argparse,subprocess
import string

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="video url",type=str)
parser.add_argument("--start", help="start time",type=str)
parser.add_argument("--end", help="end time",type=str)
args = parser.parse_args()
cmd="yt-dlp -g --youtube-skip-dash-manifest -S \"ext\" "+args.url

startTimes=args.start.split(",")
endTimes=args.end.split(",")

def clipTime(s,e):
    time = " -ss "+s+" -to "+e+" "
    return time

if(len(startTimes)!=len(endTimes)):
    print("could not match start and end time")
    exit()



r = os.popen(cmd)  
urlOutput = r.read()  
r.close()
urls=urlOutput.split('\n',1)

times=map(clipTime,startTimes,endTimes)
for idx,t in enumerate(times):
    trimCmd="ffmpeg"+t+"-i \""+urls[0].replace('\n', '').replace('\r', '')+"\""
    if(len(urls[1])>0):
        trimCmd+=t+"-i "+"\""+urls[1].replace('\n', '').replace('\r', '')+"\""
    trimCmd+=" -c copy output/output"+str(idx)+".mp4"
    print(trimCmd)
    subprocess.run(trimCmd,shell=True)

