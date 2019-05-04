from PIL import Image,ImageDraw,ImageOps,ImageFont

def text_splitting(string,inlength):
    length = 0
    out_string = ""
    out_string_testing = ""
    words = string.split(" ")
    for x in range(len(words)):
        if x == 0:
            out_string_testing +=(""+words[x])
            length+=len(words[x])+1
            if length > inlength:
                out_string_testing = out_string
                out_string_testing += "\n"+words[x]
                out_string = out_string_testing
                length=len(words[x])
            else:
                out_string = out_string_testing
        else:
            out_string_testing += (" " + words[x])
            length += len(words[x]) + 1
            if length > inlength:
                out_string_testing = out_string
                out_string_testing += "\n" + words[x]
                out_string = out_string_testing
                length = len(words[x])
            else:
                out_string = out_string_testing

    return out_string

def thumbnail(subreddit,user,title,file):
    colour=(120, 124, 126)
    title_formated = text_splitting(title,39)
    img = Image.open('media/ask_reddit_logo.png', 'r')
    comments_icon=Image.open("media/comments_icon.PNG")
    img_w, img_h = img.size
    background = Image.new('RGBA', (1920, 1080), (255,255,255,255))#26, 26, 27, 255))
    background.paste(img, (20,110))
    font_title = ImageFont.truetype("Verdana.ttf", 90)
    font_comments = ImageFont.truetype("Verdana.ttf",60)
    ImageDraw.Draw(background).text((286,110),("r/"+subreddit),(28,28,28),font=font_title)
    ImageDraw.Draw(background).text((286, 220), ("posted by u/"+user), colour, font=font_title)
    ImageDraw.Draw(background).text((30, 360), title_formated , (0,0,0), font=font_title)
    number_lines=title_formated.count("\n")+1
    background.paste(comments_icon,(20,490+(70*number_lines)))
    ImageDraw.Draw(background).text((110, 500+(70*number_lines)), "4.1k comments", (120, 124, 126), font=font_comments)
    background.save(('thumbnails/'+str(file)+'.png'))
# background = Image.new('RGBA', (1920, 1080), (255,255,255,255))#26, 26, 27, 255))
# background.save("background.png")