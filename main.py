from video_compiling import *
from thumbnail_engine.thumbnail import *
from reddit_post import *
import time

reddit_api_askreddit=reddit_api(reddit,"AskReddit")

video_engine = video_creator((1920,1080),"background.png",reddit_api_askreddit)
post = reddit_api_askreddit.get_hot_post()
x =time.time()
thumbnail("AskReddit",str(reddit_api_askreddit.get_comment_user(post)),str(reddit_api_askreddit.get_post_title(post)),"thumb")
end = time.time()
print(end-x)
video_engine.new_intro("thumb",post)
comments = []
Finished = False
x = 0
while not Finished:
    comments.append(reddit_api_askreddit.get_post_replies(post))
    video_engine.new_scene_comment(comments[x])
    x+=1
    if video_engine.get_length_of_video()>600.0:
        Finished = True

#video_engine.new_scene_comment(comment)
video_engine.compile_all("test.mp4")