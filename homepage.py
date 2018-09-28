'''renderers homepage'''

from utils import build_markdown

def home(pages, message=''):
    '''
    Returns the homepage as html
    '''

    css = """
    <style>
    .alert {
        padding: 10px;
        background-color: #222;
        color: white;
    }

    .closebtn {
        margin-left: 15px;
        color: white;
        font-weight: bold;
        float: right;
        font-size: 22px;
        line-height: 20px;
        cursor: pointer;
        transition: 0.3s;
    }

    .closebtn:hover {
        color: #ec6733;
    }
    input {
        width: 100%;
    }
    </style>
    """

    page_types = ['double', 'single', 'table']

    raw = '# eventy\n\n'
    top_menu = '> [refresh](/) - [save](/write) - [github](/)\n<br>\n>'
    raw = raw + '\n' + top_menu + '\n'
    if not pages:
        raw = raw + '\n\n' + '> No available pages!' + '\n\n'
    else:
        raw = raw + '## Pages\n'
        raw = raw + '| Page | Type | Style | Edit | Delete |\n| --- | --- | --- | --- | --- |\n'
        for entry in pages:
            raw = raw + '| [' + entry + '](/pages/' + entry + ') | ' + pages[entry]['type'] + ' '
            raw = raw + '| '+ pages[entry]['style'] + ' | ' +'[edit](/pages/' + entry + '/edit) '
            raw = raw + '| [delete](/pages/' + entry + '/delete) |\n'

    raw = raw + '\n\n## Add a page\n\n'

    html = build_markdown('eventy', raw, css=css)

    html = html + """
        <form method="POST">
            <select name="new-type">
    """
    for _type in page_types:
        html = html + '<option value="'+_type+'">'+_type+'</option>+\n'
    html = html + """
            </select>
            <input name="new-page">
            <br><br>
            <input type="submit">
        </form>
    """

    if message:
        html = html + '<div class="alert">\n'
        html = html + """<span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>\n"""
        html = html + '' + message + '\n'
        html = html + '</div>'

    return html
