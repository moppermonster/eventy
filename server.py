'''
server
'''

from flask import Flask, request, jsonify, make_response, send_from_directory, redirect

import pages
import homepage
import editors
import utils

CONFIG = utils.config_load()
PAGES = CONFIG['pages']
APP = Flask(__name__)

@APP.route('/favicon.ico')
def favicon():
    '''Return favicon.ico'''
    return send_from_directory('/static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@APP.route('/logo.png')
def logo():
    '''Return logo.png'''
    return send_from_directory('/static/logo', 'logo.png')

@APP.route('/', methods=['GET', 'POST'])
def index():
    '''home/config'''
    message = ''
    if request.method == 'GET':
        return homepage.home(PAGES, message)
    elif request.method == 'POST':
        new = request.form['new-page']
        new_type = request.form['new-type']
        if new in PAGES:
            message = 'A page with that name already exists. Name: ' + new
        elif new == '':
            message = 'Pages require a title'
        else:
            if new_type == 'table':
                empty_events = [{'date': '', 'entry': ''}]*8
                PAGES.update({new:{'type': new_type, 'style': 'default', 'events': empty_events}})
            else:
                PAGES.update({new:{'type': new_type, 'style': 'default', 'entry': ''}})
            message = 'Added new page: '+new
        return homepage.home(PAGES, message)

@APP.route('/pages/<page_name>')
def event(page_name):
    '''event'''
    if not page_name in PAGES:
        return pages.page_not_found(page_name)
    page = PAGES[page_name]
    if page['type'] == 'single':
        return pages.single_page(page_name, PAGES[page_name]['entry'])
    elif page['type'] == 'double':
        return pages.double_page(page_name, PAGES[page_name]['entry'])
    elif page['type'] == 'table':
        return pages.table_page(page_name, PAGES[page_name]['events'])


@APP.route('/pages/<page_name>/edit', methods=['GET', 'POST'])
def editor(page_name):
    '''editor'''
    if not page_name in PAGES:
        return pages.page_not_found(page_name)
    page = PAGES[page_name]
    if page['type'] == 'single':
        if request.method == 'POST':
            new = request.form['message']
            PAGES[page_name]['entry'] = new
            return redirect('/')
        return editors.single_edit(page_name, PAGES[page_name]['entry'])
    elif page['type'] == 'double':
        if request.method == 'POST':
            new = request.form['message']
            sub = request.form['message-sub']
            PAGES[page_name]['entry'][0] = new
            PAGES[page_name]['entry'][1] = sub
            return redirect('/')
        return editors.double_edit(page_name, PAGES[page_name]['entry'])
    elif page['type'] == 'table':
        if request.method == 'POST':
            d_0 = request.form['date-0']
            e_0 = request.form['entry-0']
            d_1 = request.form['date-1']
            e_1 = request.form['entry-1']
            d_2 = request.form['date-2']
            e_2 = request.form['entry-2']
            d_3 = request.form['date-3']
            e_3 = request.form['entry-3']
            d_4 = request.form['date-4']
            e_4 = request.form['entry-4']
            d_5 = request.form['date-5']
            e_5 = request.form['entry-5']
            d_6 = request.form['date-6']
            e_6 = request.form['entry-6']
            d_7 = request.form['date-7']
            e_7 = request.form['entry-7']
            new_list = [
                {'date': d_0, 'entry': e_0},
                {'date': d_1, 'entry': e_1},
                {'date': d_2, 'entry': e_2},
                {'date': d_3, 'entry': e_3},
                {'date': d_4, 'entry': e_4},
                {'date': d_5, 'entry': e_5},
                {'date': d_6, 'entry': e_6},
                {'date': d_7, 'entry': e_7},
            ]
            PAGES[page_name]['events'] = new_list
            return redirect('/')
        return editors.table_edit(page_name, PAGES[page_name]['events'])

@APP.route('/pages/<page_name>/delete', methods=['GET', 'POST'])
def delete(page_name):
    '''editor'''
    raw_md = "[BACK](/)\n"
    raw_md = raw_md + '# Delete '+page_name
    htm = utils.build_markdown('delete: '+page_name, raw_md)
    if not page_name in PAGES:
        return pages.page_not_found(page_name)
    if request.method == 'GET':
        htm = htm + """Confirm deletion of """+page_name
        htm = htm + """<form method='POST'><input type="submit"></form>"""
        return htm
    if request.method == 'POST':
        del PAGES[page_name]
        return redirect('/')

@APP.route('/write')
def write():
    '''save'''
    # utils.config_write(PAGES)
    return make_response(jsonify(PAGES))

@APP.errorhandler(404)
def not_found(error):
    '''Return a generic 404 message'''
    _path = request.full_path
    _ip = request.remote_addr
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    APP.run(debug=True)
