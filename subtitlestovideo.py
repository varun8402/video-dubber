from moviepy.editor import *
def subtitles_to_video(subtitles,input_video,transcript):
    with open(subtitles,"r" ,encoding='utf-8') as sub:
        s = sub.read();
    x=[]
    for i in transcript:
        for j in s:
            t = TextClip(j,fontsize=40,color="white").set_position(("bottom")).set_duration(i["duration"]).set_start(i["start"])
    x.append(t)
    global f 
    f = CompositeVideoClip([VideoFileClip(input_video),x])