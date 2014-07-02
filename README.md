pyopenlibrary
=============

Python Interface for the Open Library API

Documentation
-------------
See the [API documentation] (https://openlibrary.org/developers/api)

Install
-------

	pip install pyopenlibrary

Usage
-----

	import openlibrary
	api = openlibrary.BookSearch()
	res = api.get_by_author('greg egan')

	res.docs[:5]
	[<Document: [Greg Egan] Distress>,
	 <Document: [Greg Egan] Diaspora>,
	 <Document: [Greg Egan] Quarantine>,
	 <Document: [Greg Egan] Teranesia>,
	 <Document: [Greg Egan] Schild's ladder>]

	res.docs[0].lang
	u'eng'



