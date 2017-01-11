import feedparser
import time
import math
import json
import os
from collections import OrderedDict

# add below line to crontab:
# 0 0,6,12,18 * * * /path/to/mycommand
stackoverflow_json_file = 'stackoverflow_jobs.json'

de_states = {'DE': 'Germany', 'REMOTE': 'Remote', 'BW': 'Baden-Wuerttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
             'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
             'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz', 'SL': 'Saarland',
             'SN': 'Sachsen', 'ST': 'Sachen-Anhalt', 'SH': 'Schleswig-Holstein', 'TH': 'Thuringia'}

de_states_sorted = OrderedDict(
        [('DE', 'Germany'), ('REMOTE', 'Remote'), ('BW', 'Baden-Württemberg'), ('BY', 'Bayern'), ('BE', 'Berlin'),
         ('BB', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hessen'), ('MV', 'Mecklenburg-Vorpommern'),
         ('NI', 'Niedersachsen'), ('NW', 'Nordrhein-Westfalen'), ('RP', 'Rheinland-Pfalz'), ('SL', 'Saarland'),
         ('SN', 'Sachsen'), ('ST', 'Sachen-Anhalt'), ('SH', 'Schleswig-Holstein'), ('TH', 'Thüringen')])

DE_STATE_CHOICES = (('Germany', 'Germany'), ('BW', 'Baden-Württemberg'), ('BY', 'Bayern'), ('BE', 'Berlin'),
                    ('BB', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hessen'),
                    ('MV', 'Mecklenburg-Vorpommern'), ('NI', 'Niedersachsen'), ('NW', 'Nordrhein-Westfalen'),
                    ('RP', 'Rheinland-Pfalz'), ('SL', 'Saarland'), ('SN', 'Sachsen'), ('ST', 'Sachen-Anhalt'),
                    ('SH', 'Schleswig-Holstein'), ('TH', 'Thüringen'))


eu_countries = {'EU': 'Europe', 'AT': 'Austria', 'BE': 'Belgium', 'CH': 'Switzerland', 'DE': 'Germany', 'DK': 'Denmark',
                'FR': 'France', 'IT': 'Italy', 'LU': 'Luxembourg', 'NL': 'Netherlands', 'PL': 'Poland', 'SE': 'Sweden',
                'SP': 'Spain', 'UK': 'United Kingdom', 'REMOTE': 'Remote'}

eu_countries_sorted = OrderedDict(
    [('EU', 'Europe'), ('AT', 'Austria'), ('BE', 'Belgium'), ('CH', 'Switzerland'), ('DE', 'Germany'),
     ('DK', 'Denmark'), ('FR', 'France'), ('IT', 'Italy'), ('LU', 'Luxembourg'), ('NL', 'Netherlands'),
     ('PL', 'Poland'), ('SE', 'Sweden'), ('SP', 'Spain'), ('UK', 'United Kingdom'), ('REMOTE', 'Remote')]
)

EU_COUNTRIES_CHOICES = (
    ('AT', 'Austria'), ('BE', 'Belgium'), ('CH', 'Switzerland'), ('DE', 'Germany'), ('DK', 'Denmark'), ('FR', 'France'),
    ('IT', 'Italy'), ('LU', 'Luxembourg'), ('NL', 'Netherlands'), ('PL', 'Poland'), ('SE', 'Sweden'), ('SP', 'Spain'),
    ('UK', 'United Kingdom')
)


def _get_title(job_item):
    """
    Given a JobItem class returns a string with the title of a job offer

    :param job_item: JobItem class
    :return: a string representing the title of the job offer
    """
    main = job_item.title + ' at ' + job_item.name
    location = ' ()'
    remote = ''
    if job_item.city and job_item.state:
        location = ' (%s , %s)' % (job_item.city, eu_countries[job_item.state])
    elif job_item.city:
        location = ' ( %s)' % job_item.city
    elif job_item.state:
        location = ' ( %s)' % eu_countries[job_item.state]
    if job_item.remote:
        remote = ' (allows remote)'

    return main + location + remote


def _get_updated_parsed(job_item):
    """

    :param job_item:
    :return:
    """
    return job_item.published.timetuple()


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
        return cls(_get_title(job), '', job.name, '',
                   _get_updated_parsed(job), job.description, job.url, job.instructions)

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
    """
    Feeder of StackOverFlow to help fetching the remote jobs
    """
    def __init__(self):
        self._url = "https://stackoverflow.com/jobs/feed"
        self._question_mark_added = False

    def _pre_add_parameter(self):
        if not self._question_mark_added:
            self._question_mar_added = True
            self._url += "?"

    def _add_remote(self):
        self.reset()
        self._pre_add_parameter()
        self._url += 'r=true'

    def add_state(self, state):
        if state == 'Remote':
            return self._add_remote()
        self.reset()
        self._pre_add_parameter()
        self._url += 'sort=i&' + 'l=' + state + ',Germany' + '&d=20&u=Km'

    def add_country(self, country):
        if country == 'Remote':
            return self._add_remote()
        self.reset()
        self._pre_add_parameter()
        self._url += 'sort=i&' + 'l=' + country + '&d=20&u=Km'

    def reset(self):
        self._url = "https://stackoverflow.com/jobs/feed"

    def parse(self):
        return feedparser.parse(self._url)


def get_stackoverflow_jobs():
    result = dict()
    for k, v in eu_countries_sorted.items():
        result[k] = get_stackoverflow_by_state(v)
    return result


def get_stackoverflow_by_state(country):
    """
    Fetch stackoverflow jobs for a given state and sort them

    :param state: the state where to fetch the jobs
    :return: sorted dictionary of jobs
    """
    sofeed = StackOverflowFeed()
    sofeed.add_country(country)
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
    """
    Auxiliar function
    """
    if isinstance(t, time.struct_time):
        return list(t)
    else:
        return t


def merge_dict_jobs(dictA, dictB):
    """
    Merge two dictionary of jobs into a single dictionary sorting the values.

    :param dictA: dictionary with states as keys
    :param dictB: dictionary with states as keys
    :return: a dictionary with sorted content of dictA and dictB
    """
    result = {}
    for k, v in dictA.items():
        list = dictA[k] + dictB[k]
        sorted_list = sorted(list, key=lambda t: _sort_job_help(t['updated_parsed']), reverse=True)
        result[k] = sorted_list
    return result


def load_stackoverflow_jobs():
    """
    Load the local file with stackoverflow jobs into a python dictionary.

    :return: dictionary with stackoverflow jobs
    """
    with open(stackoverflow_json_file) as json_data:
        result = json.load(json_data)
        return result


def write_stackoverflow_jobs(data):
    """
    Write stackoverflow jobs into a local file.
    """
    with open(stackoverflow_json_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def download_stackoverflow_jobs():
    """
    Get all stackoverflow jobs and write them in a local file
    """
    try:
        os.remove(stackoverflow_json_file)
    except FileNotFoundError:
        pass
    data = get_stackoverflow_jobs()
    write_stackoverflow_jobs(data)


def get_raw():
    sofeed = StackOverflowFeed()
    sofeed.add_state('DE')
    jobs = sofeed.parse()
    data = jobs["items"]
    with open('raw.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)


def test_bundesland():
    jobs = get_stackoverflow_by_state(de_states['BY'])
    for job in jobs:
        # print(job['title'] + ' -- ' + job['location'] + ' -- ' + job['published'])
        print(job['published'])


def test_urls():
    sofeed = StackOverflowFeed()
    for k, v in de_states.items():
        sofeed.add_state(v)
        print(sofeed._url)


def test_load():
    a = load_stackoverflow_jobs()
    print(a)

#test_bundesland()
download_stackoverflow_jobs()
#test_urls()
#test_load()

