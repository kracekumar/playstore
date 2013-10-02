# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup


class PlayStore(object):
    """
    Class to access details of app from Google Play Store.
    """
    def __init__(self, url=None):
        self.url = url
        self.description, self.name, self.category, self.author = u'', u'', u'', u''
        self.score, self.download_count, self.size = None, None, None
        self.updated_at, self.current_version = None, None
        self.minimum_requirement, self.content_rating = None, None
        self._url_pattern = u".*play.google.com.+"

    def is_valid_url(self):
        """
        Check if app url is valid play store url.
        """
        if re.match(self._url_pattern, self.url):
            return True
        return False

    def extract_details(self):
        """
        Extract app details from html.
        """
        try:
            self._soup = BeautifulSoup(self.html)
            # Extract Name
            self.name = self._soup.title.string.split('-')[0].strip()
            # Extract description
            self.description = self._soup.find('div', 'app-orig-desc').text.strip()
            # Extract Author & updated_at
            t = self._soup.find_all('div', itemprop='author')[0]
            t = t.text.split('-')
            self.author, self.updated_at = t[0].strip(), t[1].strip()
            # Extract category
            self.category = [i.text.strip() for i in self._soup.find_all('a', 'document-subtitle category')]
            # Extract score
            score = self._soup.find('div', 'score').text.strip()
            try:
                # Convert to int if possible
                self.score = int(score)
            except:
                self.score = score.strip()
            finally:
                # Just delete the variable
                del score
            # Extract Download Count
            # Download counts(5,858,841) are comma separated so replace
            dc = self._soup.find('span', 'reviews-num').text.strip().replace(',', "")
            try:
                self.download_count = int(dc)
            except:
                self.download_count = dc
            finally:
                del dc
            # Extract size
            self.size = self._soup.find('div', itemprop='fileSize').text.strip()
            # Extract current_version
            self.current_version = self._soup.find('div', itemprop='softwareVersion').text.strip()
            # Extract minimum_requirement
            self.minimum_requirement = self._soup.find('div', itemprop='operatingSystems').text.strip()
            # Extract content_rating
            self.content_rating = self._soup.find('div', itemprop='contentRating').text.strip()
        except AttributeError:
            raise AttributeError("Attribute is missing while parsing HTML. You should report this issue")

    def fetch_details(self, url=None):
        """
        Fetch html page from Google Play Store.
        """
        self.url = self.url or url
        if self.url:
            if not self.is_valid_url():
                raise Exception("Invalid Play Store Url %s " % self.url)
            try:
                r = requests.get(self.url)
                self._status_code = r.status_code
                self.html, self._request = r.content, r
                self.extract_details()
            except:
                pass
        else:
            raise Exception("url is missing")

    def short_description(self):
        """
        One line description of the app.
        """
        return self.description.split('.')[0]

    def star_counts(self):
        """
        Dictionary with count score from 1 to 5.
        """
        d = {}
        for key, val in [(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five")]:
            # Replace ','
            base = self._soup.find('div', 'rating-bar-container %s' % val).find('span', 'bar-number').text.strip('').replace(',', "")
            try:
                d[key] = int(base)
            except:
                d[key] = base
        return d

    def additional_information(self):
        """
        Dictionary containing dditional information of the app.
        """
        d = {}
        for i in self._soup.find_all('div', 'meta-info'):
            title, val = i.find('div', 'title').text, i.find('div', 'content')
            if title and val:
                # if the content is hyper link get the link name and url
                if val.a:
                    links = [{link.text.strip(): link.get('href')} for link in val.find_all('a')]
                    d[title] = links
                else:
                    d[title] = val.text.strip()
        return d

    def thumbnails_url(self):
        """
        List of all thumbnail urls
        """
        return [t.get('src') for i in self._soup.find_all('div', 'thumbnails') for t in i.find_all('img')]
        
    def coverimage_url(self):
        """
        Cover Image url
        """
        return self._soup.find('img', 'cover-image').get('src')

    def thumbnails(self):
        """
        list of dict containing thumbnails name, content, format etc...
        """
        l = []
        for i in self._soup.find_all('div', 'thumbnails'):
            for t in i.find_all('img'):
                src = t.get('src')
                r = requests.get(src)
                d = {u'src': src, u'name': t.get('data-expand-to'), 'content': r.content, 'content-type': r.headers['content-type'], u'content-length': r.headers['content-length']}
                l.append(d)
        return l

    def coverimage(self):
        """
        Dict contains coverimage name, content, format etc...
        """
        src = self._soup.find('img', 'cover-image').get('src')
        r = requests.get(src)
        return {u'content': r.content, u'name': 'cover-image', u'content': r.content, u'content-type': r.headers['content-type'], u'content-length': r.headers['content-length']}
