from youtube_transcript_api import YouTubeTranscriptApi
import pytube
from pytube.helpers import safe_filename
from tkinter.filedialog import *
import moviepy.editor
import speech_recognition as sr
from text_to_audio import *
from audiovideomerger import *
from subtitlestovideo import *
'from subtitlestovideo import *'
url = 'https://www.youtube.com/watch?v=0_EscfBn3rE&t=1s&ab_channel=CIPAMIndia'
sep = 'channel'
urlshrt = url.split(sep,1)[0]
urlshrt = urlshrt[32:-1]
my_video = pytube.YouTube(url)
my_video = my_video.streams.get_highest_resolution()
my_video.download('Downloads')
input_video="Downloads/" + safe_filename(my_video.title)+".mp4"
text_file = "subtitles/"+ urlshrt+".txt"
video = moviepy.editor.VideoFileClip(input_video)
try:
    srt = YouTubeTranscriptApi.get_transcript(urlshrt)
    text = ""
    with open(text_file, "w") as file:
        for i in srt:
            text += i["text"] + "\n"    
        file.write(text)
        
except:
    audio = video.audio
    audio.write_audiofile("audio/"+my_video.title+".wav")
    sound = ("audio/" + my_video.title+".wav")
    rec = sr.Recognizer()
    with sr.AudioFile(sound) as source:
        audio=rec.listen(source)
        try:
            text = rec.recognize_google(audio)
            with open("subtitles/" + urlshrt+".txt" , "w") as  file:
                file.write(text)
        except:
            print("Sorry couldn't hear that")
convert_text_to_target_language(text_file, "hi", text_file[:-4]+"hi.txt")
convert_text_file_to_audio(text_file[:-4]+"hi.txt" , "hi","audio/" + my_video.title+"hi"+".mp3")
merge_audio_and_video(input_video,"audio/" + my_video.title+"hi"+".mp3","final/"+my_video.title+"final.mp4")
    