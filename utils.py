'''utils'''

import json
from markdown import markdown

import requests
from flask import make_response, jsonify

def build_markdown(title, content, _type='default', style='default', css=''):
    '''
    Return the content as markdown formatted html with title title
    '''
    content = markdown(content, extensions=['markdown.extensions.extra'])
    if _type == 'default':
        fonts = '<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />'
        head_a = '<html><head><title>'+title+'</title> '+fonts
        head_b = '<link rel="stylesheet" href="/static/css/dfmd_light.css">'
        head = head_a + ' ' + head_b + css + '</head>'
    elif _type == 'eventy':
        fonts = '<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />'
        head_a = '<html><head><title>'+title+'</title> '+fonts
        head_b = '<link rel="stylesheet" href="/static/css/eventy.css">'
        head = head_a + ' ' + head_b + css + '</head>'
    elif _type == 'eventyxl':
        fonts = '<link rel="stylesheet" type="text/css" href="//fonts.googleapis.com/css?family=Open+Sans" />'
        head_a = '<html><head><title>'+title+'</title> '+fonts
        head_b = '<link rel="stylesheet" href="/static/css/eventyxl.css">'
        head = head_a + ' ' + head_b + css + '</head>'
    page = head + '\n\n<body>\n' + content + '\n</body>\n</html>'
    return page

def config_error(message='Things went wrong'):
    '''raise exception message'''
    raise Exception(message)

def config_test():
    '''standard config.txt test'''
    print('Going through standard config.txt test')
    from os.path import isfile
    if not isfile('config/config.txt'):
        config_error('Missing config.txt')
    with open('config/config.txt') as f:
        lines = f.read()
    return lines

def config_load(skip=False):
    '''load and parse config file and return settings'''
    print('Eventy is loading...')
    raw_json = config_test()
    print('Eventy finished loading')
    if raw_json in ['', '{}']:
        print('Empty config.txt, loading demo content')
        pages = config_demo()
    else:
        pages = json.loads(raw_json)
    return {'pages': pages}

def config_write(pages, skip=False):
    '''write config file and return settings'''
    print('Eventy is saving...')
    lines = config_test()
    raw_json = json.dumps(pages)
    with open('config/config.txt', 'w') as f:
        f.write(raw_json)
    print('Eventy finished saving')
    return raw_json

def config_demo():
    '''return demo settings'''
    pages = {
        'hello-world': {
            'type': 'table',
            'style': 'default',
            'events': [
                {'date': 'every Friday', 'entry': 'Hello world!'},
                {'date': '!', 'entry': 'Eventy can be configured from the home page.'},
                {'date': '0', 'entry': 'Using `0` in the date field makes events show at the bottom, `!` at the top.'},
                {'date': '', 'entry': ''},
                {'date': '', 'entry': ''},
                {'date': '', 'entry': ''},
                {'date': '', 'entry': ''},
                {'date': '', 'entry': ''},
            ],
        },
        'single-example': {
            'type': 'single',
            'style': 'default',
            'entry': 'Single message example'
        },
        'double-example': {
            'type': 'double',
            'style': 'default',
            'entry': ['Double message example', 'Sub message']
        },
    }
    return pages
