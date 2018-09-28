'''renderers pages'''

from utils import build_markdown

def page_not_found(page_title):
    '''
    Returns 404 specific for /pages
    '''
    raw = '> [Home](/)\n'
    raw = raw + '# Page not found!\n'
    if len(page_title) > 20:
        page_title = page_title[:15] + '...'
    raw = raw + '##### Page `' + page_title + '` is nowhere to be found'
    return build_markdown('404', raw)

def single_page(page_title, event):
    '''
    Returns html for single message page
    '''

    if not event:
        raw = '> This page has yet to be configured!'
    else:
        raw = '# '+event

    return build_markdown(page_title, raw, _type='eventyxl')

def double_page(page_title, event):
    '''
    Returns html for double message page
    '''

    if not event:
        raw = '> This page has yet to be configured!'
    else:
        raw = '# '+event[0]
        if event[1]:
            raw = raw + '\n## ' + event[1]

    return build_markdown(page_title, raw, _type='eventyxl')

def table_page(page_title, event_list):
    '''
    Returns html for event table page
    '''

    top = []
    middle = []
    bottom = []

    for event in event_list:
        date = event['date']
        entry = event['entry']

        if not entry:
            continue
        if not date:
            date = '-'

        if date in ['!']:
            text = '| ' + '⚠️' + ' | ' + entry + ' | '
            top.append(text)
        elif date in ['0']:
            text = '| ' + '🤖' + ' | ' + entry + ' | '
            bottom.append(text)
        else:
            text = '| ' + date + ' | ' + entry + ' | '
            middle.append(text)

    raw = '## ' +page_title + '\n| Date | Event |\n'
    raw = raw + '| --- | --- |\n'
    if top:
        raw = raw + '\n'.join(top) + '\n'
    if middle:
        raw = raw + '\n'.join(middle) + '\n'
    if bottom:
        raw = raw + '\n'.join(bottom) + '\n'

    return build_markdown(page_title, raw, _type='eventy')
