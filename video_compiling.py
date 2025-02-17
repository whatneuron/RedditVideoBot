import numpy as np
from frame_gen import new_frame
from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
from tts import *
from mutagen.mp3 import MP3
from thumbnail_engine.thumbnail import *
from reddit_post import *
from multiprocessing.dummy import Pool as ThreadPool
import shutil
# static clip -https://www.youtube.com/watch?v=Y62EgHvwa8k

class video_creator:
    def __init__(self,videosize: tuple,background: str,reddit_inst):
        self.screensize = videosize
        self.background = background
        self.clips = []
        self.fontsize_main = 30
        self.reddit_api = reddit_inst
        self.transition = VideoFileClip("static.mp4").subclip(0,0.5).resize(height=1080,width=1080)
        self.clip = []
        self.clips_saved = []
        self.end_clips = []
    def new_intro(self,thumbnail,post):
        text = self.reddit_api.get_post_title(post)
        produce_audio(str(text),"full_title_audio")
        audio = MP3(("audio/outputfull_title_audio.mp3"))
        clip_audio = AudioFileClip(("audio/outputfull_title_audio.mp3"))
        length = float(audio.info.length) - 0.4
        clip = ImageClip(("thumbnails/"+str(thumbnail)+".png"), duration=length).set_audio(clip_audio)
        #clip.set_audio(clip_audio)
        self.clips.append(clip)
        self.clips.append(self.transition)
    def new_scene_comment(self,comment):
        self.clip = []
        full_text = self.reddit_api.get_comment_body(comment)
        comment_id = self.reddit_api.get_comment_id(comment)
        comment_user =self.reddit_api.get_comment_user(comment)
        comment_score = self.reddit_api.get_comment_score(comment)
        text = ""
        formated =full_text.splitlines()
        for line in range(len(formated)):
            formated[line]=text_splitting(formated[line],90)
        formated_full="""
""".join(formated)
        formated= formated_full
        formated = formated.splitlines()
        print(formated)
        for x in range(len(formated)):
            #if formated[x]==" "or formated[x]=="" or formated[x]=="""
#""":
            #    pass
            # produce_audio(formated[x],("example"+str(x)))
            try:
                produce_audio(formated[x],str(x))
                audio = MP3(("audio/output"+str(x)+".mp3"))
                length = float(audio.info.length) -0.3
                if not x==0:
                    text += """
"""
                text+=formated[x]
                new_frame(str(comment_user),text,comment_score,x,(comment_id))
                clip = ImageClip(("frames/frame"+str(comment_id)+str(x)+".png"),duration=length)
                # total_clip=ImageClip("background.png",duration=length)
                # txtclip=TextClip(text, align = "west", fontsize=self.fontsize_main, color='black', font="Verdana.ttf")
                # txtclip=txtclip.set_position((80, 60)).set_duration(length)
                # total_clip = CompositeVideoClip([total_clip, txtclip])
                #
                # txtclip_user = TextClip(("u/"+str(comment_user)), align="west", fontsize=self.fontsize_main, color='rgb(79, 188, 255)', font="Verdana.ttf")
                # txtclip_user = txtclip_user.set_position((80, 20)).set_duration(length)
                # total_clip = CompositeVideoClip([total_clip, txtclip_user])

                # txtclip_user = TextClip((str(comment)), align="west", fontsize=self.fontsize, color='rgb(79, 188, 255)', font="Verdana.ttf")
                # txtclip_user = txtclip_user.set_position((80, 20)).set_duration(length)
                # total_clip = CompositeVideoClip([total_clip, txtclip_user])

                #audio = AudioFileClip(("audio/output"+str(x)+".mp3")).subclip(0,length)
                #audio = audio
                #total_clip = total_clip#.set_audio(audio)
                self.clip.append(clip)
            except AssertionError:
                pass
        produce_audio(formated_full,("full"+str(comment_id)))

        total_audio = AudioFileClip(("audio/outputfull"+str(comment_id)+".mp3"))
        finished_clip = concatenate_videoclips(self.clip)#.set_duration(total_audio.duration)
        finished_clip = finished_clip.set_audio(total_audio)
        self.clips.append(finished_clip)
        self.clips.append(self.transition)
    # def load_clips(self):
    #     for i in range(len(self.clips_saved)):
    #         self.clips.append()
    def compile_all(self,filename):
        print(self.clips)
        end = concatenate_videoclips(self.clips)
        self.clips = []
        self.end_clips.append(end)
        result=concatenate_videoclips(self.end_clips)
        audio_background = AudioFileClip('media/background_1_lower.mp3').subclip(0,result.duration)
        final_audio = CompositeAudioClip([result.audio, audio_background])
        result = result.set_audio(final_audio)

        end = None
        self.end_clips = []
        final_audio = None
        result.write_videofile(str((filename)),fps=10,bitrate='11000k',codec="libx264")#,ffmpeg_params="-threads 8")#,codec='h264_nvenc')#,ffmpeg_params="-hwaccel nvdec")
        result = None
        self.clear_folder("frames")
        self.clear_folder("audio")

        # os.system("rm -r frames/*")
        # os.system("rm -r audio/*")
    def clear_folder(self,folder):
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)
    def get_length_of_video(self):
        self.length = 0
        for i in self.clips:
            self.length += i.duration
        return self.length
    def clear_vars(self):
        pass
#    def new_scene_intro(self,):


