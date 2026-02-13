from ast import arg
import os,argparse,subprocess
import string

parser = argparse.ArgumentParser()

parser.add_argument("--url", help="video url",type=str)
parser.add_argument("--start", help="start time",type=str)
parser.add_argument("--end", help="end time",type=str)
args = parser.parse_args()

cmd="yt-dlp -g --youtube-skip-dash-manifest --cookies-from-browser -S \"ext\" "+"\""+args.url+"\" "

startTimes=args.start.split(",")
endTimes=args.end.split(",")

def clipTime(s,e):
    time = " --download-sections *"+s+"-"+e
    return time

if(len(startTimes)!=len(endTimes)):
    print("could not match start and end time")
    exit()

if not os.path.exists('temp'):
    os.makedirs('temp')
if not os.path.exists('output'):
    os.makedirs('output')


times=map(clipTime,startTimes,endTimes)
for idx,t in enumerate(times):
    trimCmd="yt-dlp "
    trimCmd+=" --extractor-args \"youtube:getpot_bgutil_baseurl=https://yt-dlp-pot.44444444.xyz\" "
    trimCmd+=" -S quality,codec:avc:m4a "+"\""+args.url+"\""+t
    
    trimCmd+=" --cookies cookies.txt"
    trimCmd+=" -o temp/output"+str(idx)+".mp4"
    print(trimCmd)
    subprocess.run(trimCmd,shell=True)

print("Aligning a/v head")

for filename in os.listdir('temp'):
    input_file = os.path.join('temp', filename)
    output_file = os.path.join('output', filename)
    ffmpeg_command = f'ffmpeg -ss 0 -i "{input_file}" -c:v copy -c:a copy "{output_file}"'
    subprocess.run(ffmpeg_command, shell=True)
    os.remove(input_file)
