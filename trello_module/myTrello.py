#!/usr/bin/env python
# -*- coding: utf-8 -*-


from trello import TrelloClient

__all__ = ['trelloConnection']

class trelloConnection:
	"""
    Implémentation d'une aide a la connection a trello
 
    Usage:
 
    >>> from trello_module import trelloConnection
    >>> trelloConnection(KEY,SECRET,TOKEN)

	"""
	def __init__(self,key,secret,token):
		client = TrelloClient(api_key=key,api_secret=secret,token=token)
		
		print "Connection ... to trello boards"
		
		all_boards = client.list_boards()
		
		print all_boards

