import pandas as pd

class Beast:

    df = pd.read_csv('data/mr_beast_youtube_stats.csv')

    def __init__(self, title):
        self.title = title
        self.row = self.df[self.df['title'] == self.title]
        self.desc = self.row['description'][0]
        self.viewcount = self.row['viewCount'][0]
        self.likecount = self.row['likeCount'][0]
        self.commentcount = self.row['commentCount'][0]
