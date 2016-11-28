import feedparser
import time
import math
import json

# from geekjobs.constants import bundeslander2
# from . import constants


# add below line to crontab:
# 0 0,6,12,18 * * * /path/to/mycommand
stackoverflow_json_file = 'stackoverflow_jobs.json'

bundeslander2 = {'DE': 'Germany', 'REMOTE': 'Remote', 'BW': 'Baden-Wuerttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                 'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                 'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz', 'SL': 'Saarland',
                 'SN': 'Sachsen', 'ST': 'Sachen-Anhalt', 'SH': 'Schleswig-Holstein', 'TH': 'Thuringia'}


def _generate_title(cls):
    main = cls.title + ' at ' + cls.name
    location = ' (Germany)'
    remote = ''
    if cls.city:
        location = ' (' + cls.city + ', Germany)'
    if cls.remote:
        remote = ' (allows remote)'

    return main + location + remote


def _generate_updated_parsed(cls):
    return cls.published.timetuple()


def _generate_published(cls):
    return cls.published.strftime('%a, %d %b %Y %X')


def _generate_days(timestruct):
    return math.modf((time.mktime(time.localtime()) - time.mktime(timestruct)) / (60*60*24))[1]


class JobItem:
    def __init__(self, title, location, author, published, updated_parsed, summary, link, instructions):
        self.title = title
        self.location = location
        self.author = author
        self.published = published
        self.updated_parsed = updated_parsed
        self.summary = summary
        self.link = link
        self.days = _generate_days(updated_parsed)
        self.instructions = instructions

    @classmethod
    def from_model_job(cls, job):
        return cls(_generate_title(job), '', job.name, '',
                   _generate_updated_parsed(job), job.description, job.url, job.instructions)

    def to_dict(self):
        result = dict()
        result['title'] = self.title
        result['location'] = self.location
        result['author'] = self.author
        result['published'] = self.published
        result['updated_parsed'] = self.updated_parsed
        result['summary'] = self.summary
        result['link'] = self.link
        result['days'] = self.days
        result['instructions'] = self.instructions
        return result


class StackOverflowFeed:
    def __init__(self):
        self._url = "https://stackoverflow.com/jobs/feed"
        self._question_mark_added = False

    def _pre_add_parameter(self):
        if not self._question_mark_added:
            self._question_mar_added = True
            self._url += "?"

    def add_bundesland(self, bundesland):
        if bundesland == 'Remote':
            return self.add_remote()
        self.reset()
        self._pre_add_parameter()
        self._url += 'sort=i&' + 'l=' + bundesland + ',Germany' + '&d=20&u=Km'

    def add_remote(self):
        self.reset()
        self._pre_add_parameter()
        self._url += 'r=true'

    def reset(self):
        self._url = "https://stackoverflow.com/jobs/feed"

    def parse(self):
        return feedparser.parse(self._url)


def get_stackoverflow_jobs():
    result = dict()
    for k, v in bundeslander2.items():
        result[k] = get_stackoverflow_bundesland(v)
    return result


def get_stackoverflow_bundesland(value):
    sofeed = StackOverflowFeed()
    sofeed.add_bundesland(value)
    jobs = sofeed.parse()
    result = []
    for item in jobs["items"]:
        try:
            location = item.location
        except AttributeError:
            location = None
        new_item = JobItem(item.title, location, item.author, item.published, item.updated_parsed, item.summary,
                           item.link, None)
        result.append(new_item.to_dict())
    sorted_result = sorted(result, key=lambda t: t['updated_parsed'], reverse=True)
    return sorted_result


def _sort_job_help(t):
    if isinstance(t, time.struct_time):
        return list(t)
    else:
        return t


def merge_json_jobs(dictA, dictB):
    result = {}
    for k, v in dictA.items():
        list = dictA[k] + dictB[k]
        sorted_list = sorted(list, key=lambda t: _sort_job_help(t['updated_parsed']), reverse=True)
        result[k] = sorted_list
    return result


def get_raw():
    sofeed = StackOverflowFeed()
    sofeed.add_bundesland('DE')
    jobs = sofeed.parse()
    data = jobs["items"]
    with open('raw.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def write_json(data):
    with open(stackoverflow_json_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def load_json_file():
    with open(stackoverflow_json_file) as json_data:
        result = json.load(json_data)
        return result


def test_bundesland():
    jobs = get_stackoverflow_bundesland(bundeslander2['BY'])
    for job in jobs:
        # print(job['title'] + ' -- ' + job['location'] + ' -- ' + job['published'])
        print(job['published'])


def test_write():
    # data = get_stackoverflow_bundesland(bundeslander['BY'])
    data = get_stackoverflow_jobs()
    write_json(data)


def test_urls():
    sofeed = StackOverflowFeed()
    for k, v in bundeslander2.items():
        sofeed.add_bundesland(v)
        print(sofeed._url)


def test_load():
    a = load_json_file()
    print(a)

#test_bundesland()
test_write()
#test_urls()
#test_load()

