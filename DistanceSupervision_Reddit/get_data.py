from __future__ import print_function
import time
import datetime
import json
import gzip
import nltk
import requests

def isPotentialEnthymeme(sent):
    if ' and since ' in sent.lower():
        return True
    return False

QUERY_TEMPLATE = "http://api.pushshift.io/reddit/{}/search?subreddit={}&limit={}&sort=desc&before={}"
SUBREDDIT = 'changemyview' 
LIMIT = 100

class RedditIterator:
    def __init__(self, timestamp=None):
        self.timestamp = timestamp

    def __iter__(self):
        #time_limit = int(time.mktime(datetime.datetime(2017, 3, 22).timetuple())) #.now().timetuple()))
        if self.timestamp is not None:
            time_limit = int(time.mktime(datetime.datetime.utcfromtimestamp(self.timestamp).timetuple()))
        else:
            time_limit = int(time.mktime(datetime.datetime.now().timetuple()))
        while True:
            while True:
                try:
                    result = requests.get(QUERY_TEMPLATE.format(self.type, SUBREDDIT, LIMIT, time_limit))
                    data = json.loads(result.content)
                except Exception:
                    pass
                else:
                    break
                
            if not len(data['data']):
                break
            
            for datum in data['data']:
                yield datum            
            
            time_limit = int(data['data'][-1]['created_utc'])

class SubmissionIterator(RedditIterator):
    type = 'submission'
class CommentIterator(RedditIterator):
    type = 'comment'                

if __name__ == '__main__':
    for iterator in (SubmissionIterator,CommentIterator):
        s = iterator()
        previous_date = None
        outfile = None
        for submission in s:
            timestamp = int(submission['created_utc'])
            date = str(datetime.datetime.fromtimestamp(timestamp).date())
            if date != previous_date:
                
                if outfile is not None:
                    outfile.close()
                outfile = open('enthymemes.txt','w')
                previous_date = date
            if s.type=="submission":
                sentences = nltk.sent_tokenize(submission['title'])
                for sent in sentences:
                    sent = sent.replace('[WP] ','')
                    sent = sent.replace('[EU] ','')
                    sent = sent.replace('[CW] ','')
                    
                    if isPotentialEnthymeme(sent):
                        print(sent)
                        if sent.endswith('\n'):
                            outfile.write(sent)
                        else:
                            outfile.write(sent+'\n')
            elif s.type=="comment":
                sentences = nltk.sent_tokenize(submission['body'].replace('\n\n','\n'))
                for sent in sentences:
                    sent = sent.replace('[WP] ','')
                    sent = sent.replace('[EU] ','')
                    sent = sent.replace('[CW] ','')
                    
                    if isPotentialEnthymeme(sent):
                        if sent.endswith('\n'):
                            outfile.write(sent)
                        else:
                            outfile.write(sent+'\n')