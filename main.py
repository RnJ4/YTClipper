from ast import arg
import os,argparse,subprocess
import string

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="video url",type=str)
parser.add_argument("--start", help="start time",type=str)
parser.add_argument("--end", help="end time",type=str)
args = parser.parse_args()
cmd="yt-dlp -g -S \"ext\" "+args.url

time=" -ss "+args.start+" -to "+args.end+" "

r = os.popen(cmd)  
urlOutput = r.read()  
r.close()

urls=urlOutput.split('\n',1)
# print("first: "+urls[0])
# print("second: "+urls[1])
trimCmd="./ffmpeg"+time+"-i \""+urls[0]+"\""+time+"-i "+"\""+urls[1]+"\" -c copy output.mp4"
print(trimCmd)
subprocess.run(trimCmd,shell=True)
