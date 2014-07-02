# -*- coding: utf-8 -*-
# openlibrary.py
# Copyright (C) 2014 Kali Kaneko
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Python Interface to the Open Library API.
"""
import requests

__author__ = "Kali Kaneko <kali@futeisha.org>"
__version__ = "0.0.1"


API_URI = "http://openlibrary.org/query.json?"
SEARCH_URI = "http://openlibrary.org/search.json?"


def maybe_single(thing):
    """
    Return a single object if it is the only item in a collection.
    """
    if isinstance(thing, list) and len(thing) == 1:
        return thing[0]
    return thing


class Search(object):
    """
    Generic search object.
    """
    uri = None

    def get(self, **kwargs):
        if not 'page' in kwargs:
            kwargs['page'] = 1
        resp = requests.get(self.uri, params=kwargs)
        return resp.json()


class Document(object):
    """
    A Document returned by a search result.
    """

    def __init__(self, doc):
        self._doc = doc

    def _get(self, key):
        return maybe_single(self._doc.get(key))

    @property
    def title(self):
        return self._get('title')

    @property
    def title_suggest(self):
        return self._get('title_suggest')

    @property
    def author(self):
        return self._get('author_name')

    @property
    def author_alt_name(self):
        return self._get('author_alternative_name')

    @property
    def publisher(self):
        return self._get('publisher')

    @property
    def cover_edition_key(self):
        return self._get('cover_edition_key')

    @property
    def first_publish_year(self):
        return self._get('first_publish_year')

    @property
    def lang(self):
        return self._get('language')

    @property
    def isbn(self):
        return self._get('isbn')

    @property
    def key(self):
        return self._get('key')

    @property
    def id_goodreads(self):
        return self._get('id_goodreads')

    @property
    def id_librarything(self):
        return self._get('id_librarything')

    @property
    def subject(self):
        return self._get('subject')

    def __repr__(self):
        return self.__unicode__().encode('ascii', 'replace')

    def __unicode__(self):
        return u"<Document: [{}] {}>".format(
            self.author, self.title)


class SearchResult(object):
    """
    Parse a search result.
    """

    def __init__(self, data):

        self._data = data

    @property
    def start(self):
        return self._data['start']

    @property
    def num_found(self):
        return self._data['num_found']

    @property
    def docs(self):
        return [Document(doc) for doc in self._data['docs']]

    def get_doc_by_index(self, index):
        return Document(self._data['docs'][index])

    def __getitem__(self, index):
        return self.get_doc_by_index(index)

    def __len__(self):
        return len(self.docs)

    def __repr__(self):
        return u"<SearchResult: %s-%s / %s>" % (
            self.start, self.start + len(self.docs) - 1, self.num_found)


class BookSearch(Search):
    """
    Implement book searches.
    """
    uri = SEARCH_URI

    def get_by_author(self, author):
        res = self.get(**{'author': author})
        return SearchResult(res)

    def get_by_title(self, title):
        res = self.get(**{'title': title})
        return SearchResult(res)
