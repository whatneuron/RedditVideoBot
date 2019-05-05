from video_compiling import *
from thumbnail_engine.thumbnail import *
from reddit_post import *
import time
from youtube_upload_wrapper.youtube_uploader import *
import resource


def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (get_memory() * 1024, hard))

def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory
print(resource.getrlimit(resource.RLIMIT_AS))
memory_limit()
print(resource.getrlimit(resource.RLIMIT_AS))


def round_string(string:str, length:int):
    length_endstring = length - 3
    endstring = string
    if len(endstring) > length_endstring:
        endstring = string[0:length_endstring]
        endstring+="..."
        return endstring
    return endstring

reddit_api_askreddit=reddit_api(reddit,"AskReddit")
while 1:
    video_engine = video_creator((1920,1080),"background.png",reddit_api_askreddit)
    post = reddit_api_askreddit.get_hot_post()
    x =time.time()
    thumbnail("AskReddit",str(reddit_api_askreddit.get_comment_user(post)),str(reddit_api_askreddit.get_post_title(post)),"thumb")
    end = time.time()
    #print(end-x)

    video_engine.new_intro("thumb",post)
    comments = []
    Finished = False
    x = 0
    while not Finished:
        comments.append(reddit_api_askreddit.get_post_replies(post))
        video_engine.new_scene_comment(comments[x])
        x+=1
        if video_engine.get_length_of_video()>600.0:
            print("done")
            Finished = True

    #video_engine.new_scene_comment(comment)
    video_engine.compile_all("test.mp4")
    title = ("Askreddit - "+str(reddit_api_askreddit.get_post_title(post)))
    title = round_string(title,70)
    print(title)
    upload_video(title,os.path.abspath("thumbnails/thumb.png"),os.path.abspath("test.mp4"))
    end = time.time()
    print(end-x)
    print(time.time())