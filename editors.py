'''renderers pages'''

from utils import build_markdown

def single_edit(page_title, event):
    '''
    Returns html for single config page
    '''
    css = """<style> input { width: 100%;} </style>"""
    raw_md = '# Edit: '+page_title
    raw_md = raw_md + '\n> [cancel](/) - [view file](/pages/'+page_title+')\n\n'
    raw_md = raw_md + '## Old:\n\n'
    raw_md = raw_md + '```' + event + '```\n'
    raw_md = raw_md + '## New:\n\n'
    htm = build_markdown(page_title, raw_md, css=css)
    htm = htm + """<form method='POST'><input name="message"><br>"""
    htm = htm + """<br><input type="submit"></form>"""
    return htm

def double_edit(page_title, event):
    '''
    Returns html for double config page
    '''

    css = """<style> input { width: 100%;} </style>"""
    raw_md = '# Edit: '+page_title
    raw_md = raw_md + '\n> [cancel](/) - [view file](/pages/'+page_title+')\n\n'
    raw_md = raw_md + '## Old:\n\n'
    raw_md = raw_md + '### message:\n\n'
    raw_md = raw_md + '```' + event[0] + '```\n'
    raw_md = raw_md + '### sub:\n\n'
    raw_md = raw_md + '```' + event[1] + '```\n'
    raw_md = raw_md + '## New:\n\n'
    htm = build_markdown(page_title, raw_md, css=css)
    htm = htm + """<form method='POST'>message:<input name="message"> """
    htm = htm + """Sub:<input name="message-sub"><br>"""
    htm = htm + """<br><input type="submit">\n</form>"""
    return htm

def table_edit(page_title, event_list):
    '''
    Returns html for table config page
    '''

    css = """<style> input { width: 50%;} </style>"""
    raw_md = '# Edit: '+page_title
    raw_md = raw_md + '\n> [cancel](/) - [view file](/pages/'+page_title+')\n\n'
    raw_md = raw_md + '# Table:\n\n'
    raw_md = raw_md + '> Use `!` as date to show on top, `0` as date to show at bottom of table.\n\n'
    htm = build_markdown(page_title, raw_md, css=css)
    for i in range(8):
        htm = htm + '''<form method='POST'><input name="date-'''
        htm = htm+str(i)+'''", value="'''+event_list[i]['date']+'''">'''
        htm = htm + '''<input name="entry-'''+str(i)
        htm = htm +'''", value="'''+event_list[i]['entry']+'''">'''
        htm = htm + '<br>'
    htm = htm + '''<br><input type="submit"></form>'''
    return htm
