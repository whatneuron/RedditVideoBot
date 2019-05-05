import praw
import save_engine
import os
reddit = praw.Reddit(client_id=str(os.environ.get("client_id")),
                     client_secret=str(os.environ.get("client_secret")),
                     user_agent=str(os.environ.get("user_agent")),
                     username=str(os.environ.get("user_agent")),
                     password=str(os.environ.get("password")))

class reddit_api:
    def __init__(self,client,sub):
        self.client=client
        self.subreddit = self.client.subreddit(sub)

    def get_hot(self,limit):
        hot_subreddit = self.subreddit.hot(limit=limit)
        return hot_subreddit

    def get_hot_post(self):
        lenposts=1
        used_posts=save_engine.load("used_posts")
        list_posts = self.get_hot(lenposts)
        loaded = False
        while not loaded:
            for post in list_posts:
                if not(post.id in used_posts):
                    used_posts.append(post.id)
                    save_engine.save(("comments/used_comments_" + str(post.id)), [])
                    save_engine.save("used_posts",used_posts)
                    loaded = True
                    return post

            lenposts+=1
            list_posts = self.get_hot(lenposts)

    def get_post_replies(self,post):
        used_comments = save_engine.load(("comments/used_comments_"+str(post.id)))
        submission = reddit.submission(post.id)
        for top_level_comment in submission.comments:
            if not(top_level_comment.id in used_comments) and not top_level_comment.stickied:
                used_comments.append(top_level_comment.id)
                save_engine.save(("comments/used_comments_"+str(post.id)),used_comments)
                return top_level_comment
        return "Nul"
    def get_comment_id(self,comment):
        return comment.id
    def get_comment_body(self,comment):
        return comment.body
    def get_comment_score(self,comment):
        return comment.score
    def get_post_score(self,post):
        return post.score
    def get_comment_user(self,comment):
        return(comment.author)
    def get_post_title(self,comment):
        return(comment.title)
    def comment_body_array(self,comment,line_distance):
        comment_content = comment.body
        comment_split_first = comment_content.splitlines()
        comment_array_final = []
        for it in range(len(comment_split_first)):
            if comment_split_first[it] == "" or comment_split_first[it] == " ":
                pass
            if len(comment_split_first[it]) >49:
                pass
            else:
                comment_array_final.append(comment_split_first[it])
# reddit_api_askreddit=reddit_api(reddit,"AskReddit")
# post = reddit_api_askreddit.get_hot_post()
# print(post.title)
# for x in range(0,10):
#     comment = reddit_api_askreddit.get_post_replies(post)
#     print(reddit_api_askreddit.get_comment_user(comment))
