#!/usr/bin/env python3
import praw
import re
from comment import get_reply

reddit = praw.Reddit("fabia_bot")


#for submission in reddit.subreddit("czech").hot(limit=1000):
#    #submission.comment_sort = "new"
#    submission.comments.replace_more()
#    for comment in submission.comments.list():
#        print(comment.body)
#        comment.reply(body="testreply")


def should_reply_to(comment):
    if type(comment) is not praw.models.reddit.comment.Comment: 
        # end of recursion - parent is None or Submission
        return True
    if comment.author == reddit.user.me(): 
        # do not reply to myself or when I already replied in this chain of replies
        return False
    return should_reply_to(comment.parent())

def run(sub):
    for comment in reddit.subreddit(sub).stream.comments(skip_existing=True):
        print(f'comment: {comment.id}\n{comment.body}') # debug
        reply = get_reply(comment.body)
        if reply:
            comment.refresh()
            if should_reply_to(comment):
                print(f'Comment: {comment.id}')
                print(comment.body)
                print("Reply:")
                print(reply)
                print("------")
                # comment.reply(body=reply) # not ready yet


def delete_my_comments():
    for comment in reddit.user.me().comments.new(limit=None):
        comment.delete()

#delete_my_comments()

run("czech") # !!! change to "premektest" for premek's tests

