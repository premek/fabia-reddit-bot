#!/usr/bin/env python3
import time
import praw
from prawcore.exceptions import ServerError
from comment import get_reply

reddit = praw.Reddit("fabia_bot")


# for submission in reddit.subreddit("czech").hot(limit=1000):
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


def process_comment(comment):
    # print(f'comment: {comment.permalink} {comment.created_utc}\n{comment.body}') # debug
    reply = get_reply(comment.body)
    if reply:
        comment.refresh()
        if should_reply_to(comment):
            print(f"Comment: {comment.permalink} {comment.created_utc}")
            print(comment.body)
            print("Reply:")
            print(reply)
            print("------")
            comment.reply(body=reply)


def run(sub):
    while True:
        try:
            for comment in reddit.subreddit(sub).stream.comments(skip_existing=True):
                process_comment(comment)
        except ServerError as err:
            print(err)
            time.sleep(30)


def delete_my_comments():
    for comment in reddit.user.me().comments.new(limit=None):
        comment.delete()


# delete_my_comments()

run("czech")  # !!! change to "premektest" for premek's tests

print(f"Finished at {time.time()}")
