import praw
import json

class Reddpic(object):

    IMG_EXTENSIONS = [".jpg", ".png", ".gif", ".tiff"]
    VALID_PERIODS = ["day", "week", "month", "year", "all"]
    VALID_SORT_TYPES = ["hot", "controversial", "new", "rising", "top"]

    def __init__(self, username, password, appname=None, 
                sort=None, subreddits=None, period=None, 
                safe=True, limit=25, extensions=None):

        # log into reddit
        # https://praw.readthedocs.org/en/v2.1.16/pages/configuration_files.html
        self.appname = appname or "Reddpic"
        self.username = username
        self.reddit = praw.Reddit(self.appname)
        self.reddit.login(username=username, password=password)

        # set settings
        self.sort = sort or 'hot'
        self.period = period or 'month'
        self.subreddits = subreddits or ["funny"]
        self.safe = True if safe else False
        self.limit = limit 
        self.extensions = extensions or Reddpic.IMG_EXTENSIONS

    def set_sort(self, sort):
        if sort in Reddpic.VALID_SORT_TYPES:
            self.sort = sort 

    def set_period(self, period):
        if period in Reddpic.VALID_PERIODS:
            self.period = period

    def set_safe(self, safe):
        if safe == True:
            self.safe = safe
        else:
            # if invalid, assume safe
            self.safe = True

    def set_limit(self, limit):
        if limit > 0:
            self.limit = int(limit)

    def set_subreddits(self, subreddits):
        self.subreddits = subreddits

    def set_extensions(self, extensions):
        self.extensions = extensions

    def query(self, terms, nots=None, output=False):
        if nots:
            terms += ["-" + n for n in nots]
        if self.safe:
            terms += ["nsfw:no"]
        terms += ["self:no"]

        results = []
        for sub in self.subreddits:
            temp_terms = list(terms)
            temp_terms += ["subreddit:%s" % sub]
            search = " ".join(temp_terms)
            submissions = self.reddit.search(search,
                limit=self.limit, sort=self.sort, period=self.period)
            processed = self.process_query(submissions, subbreddit=sub)
            results.extend(processed)

        if output:
            # output to stdout
            print self.output_json(results)
            return None
        else:
            # just return for further processing
            return results

    def process_query(self, submissions, subbreddit=None, verbose=False):
        results = []
        for submission in submissions:
            if verbose:
                print "Title: %s" % submission.title
                print "Upvotes: %d, downvotes: %d, total comments: %d" % (
                    submission.ups, submission.downs, submission.num_comments)
                print "Link: %s" % submission.url
                print

            if self.is_image(submission.url):
                result = {}
                result["title"] = submission.title
                result["ups"] = submission.ups
                result["downs"] = submission.downs
                result["image"] = submission.url
                result["ncomments"] = submission.num_comments
                if subbreddit:
                    result["subbreddit"] = subbreddit
                results.append(result)

        return results

    def output_json(self, dictionary):
        return json.dumps(dictionary)

    def is_image(self, url):
        isimage = 0
        for imgext in self.extensions:
            if url.endswith(imgext):
                isimage += 1
        return True if isimage > 0 else False

