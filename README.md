reddpic
====

`reddpic` is an extension of the `praw` reddit Python framework that allows easily finding images that pertain to keyword searches. 

## Dependencies

* [`praw`](https://github.com/praw-dev/praw/) (pip install praw)

## Example

```bash
$ python reddpic.py \
	--terms tim,howard,GoT \
	--not brazil,columbia \
	--config ./settings.example.json
[
    {
        "title": "The one save I wish Tim Howard would have made. (GOT spoilers)", 
        "downs": 0, 
        "ups": 6, 
        "image": "http://i.imgur.com/OM1SPmH.jpg", 
        "ncomments": 2, 
        "subbreddit": "funny"
    }
]
```

## Documentation of Reddit Search for `praw`

Because it's hard to find elsewhere...

#### Search Terms

* `subreddit:subreddit` - find submissions in "subreddit"
* `author:username` - find submissions by "username"
* `site:example.com`- find submissions from "example.com"
* `url:text` - search for "text" in url
* `selftext:text` - search for "text" in self post contents
* `self:yes (or self:no)` - include (or exclude) self posts
* `nsfw:yes (or nsfw:no)` - include (or exclude) results marked as NSFW

Example: "subreddit:aww site:imgur.com dog"

==============
#### [Sort Types](https://github.com/praw-dev/praw/blob/dffa47294c4a3f02dd0c37473c7a0a5676a6b06a/praw/__init__.py#L721):
- controversial
- hot
- new
- rising
- top

==============
#### [Period Types](https://github.com/praw-dev/praw/blob/dffa47294c4a3f02dd0c37473c7a0a5676a6b06a/praw/__init__.py#L723) (only whem sort is 'controversial', or 'top'):
- all
- year
- day 
- hour
- month

Using `reddpic` you don't need to worry about these, but if you want to tinker with `praw` directly, these is helpful.
