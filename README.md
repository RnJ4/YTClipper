# YTClipper
+ yt-dlp now officially supports downloading a section of the video, please see https://github.com/yt-dlp/yt-dlp#download-options
+ You can still use this repo if you don't want run the download process on your machine


1. Fork this
2. Go to the Actions tab in your forked repo
3. In the left sidebar, click the Clip workflow.
4. Above the list of workflow runs, select Run workflow
5. Input the url,start and end time, then click Run workflow
6. Wait for the action to complete and download the artifact
+ note:The beginning of the video might be silent, set your start time a few seconds earlier and trim these part locally.
+ Or use Clip and re-encode workflow in Actions. (very slow!)
