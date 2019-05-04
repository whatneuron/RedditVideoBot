from PIL import Image,ImageDraw,ImageOps,ImageFont
from thumbnail_engine.thumbnail import text_splitting


def new_frame(user,text,score,line,comment_id):
    colour=(120, 124, 126)
    #title_formated = text_splitting(title,39)
    #img = Image.open('media/ask_reddit_logo.png', 'r')
    #comments_icon=Image.open("media/comments_icon.PNG")
    #img_w, img_h = img.size
    background = Image.new('RGBA', (1920, 1080), (255,255,255,255))#26, 26, 27, 255))
    #background.paste(img, (20,110))
    font_title = ImageFont.truetype("Verdana.ttf", 20)
    font_comments = ImageFont.truetype("Verdana.ttf",30)
    ImageDraw.Draw(background).text((80,20),("posted by u/"+user),(79, 188, 255),font=font_title)
    #ImageDraw.Draw(background).text((286, 220), (str(text)), colour, font=font_title)
    ImageDraw.Draw(background).text((80, 60), text , (0,0,0), font=font_title)
    #number_lines=title_formated.count("\n")+1
    #background.paste(comments_icon,(20,490+(70*number_lines)))
    #ImageDraw.Draw(background).text((110, 500+(70*number_lines)), "4.1k comments", (120, 124, 126), font=font_comments)
    background.save(('frames/frame'+str(comment_id)+str(line)+'.png'))