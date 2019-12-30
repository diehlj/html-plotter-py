import datetime
import os

import inspect

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

TMP_FOLDER = '/tmp'


HTML_HULL = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<style type="text/css">
<!--STYLEPLACEHOLDER-->
</style>
</head>
<body>
<!--PLACEHOLDER-->
</body>"""

def show(plt, comment=None, folder=os.path.join(TMP_FOLDER, 'matplotlib'), html_filename='index.html', verbose=True, track_caller=True):
    """
    Plot to a png file and append <img> in a html file.
    """
    if not os.path.isdir( folder ):
        os.mkdir( folder )
    full_html_filename = os.path.join( folder, html_filename )
    if not os.path.isfile( full_html_filename ):
        with open( folder + '/' + html_filename, 'w' ) as html_file:
            html_file.write(HTML_HULL)
    full_img_filename = os.path.join( folder, str(datetime.datetime.now()).replace(' ','-').replace('','') + '.png' )
    plt.savefig( full_img_filename )
    plt.gcf().clear()

    if track_caller:
        code = inspect.currentframe().f_back.f_code
        caller_filename = code.co_filename
        if not os.path.isfile( caller_filename ):
            track_caller = False
        else:
            with open(caller_filename) as f:
                code_html = highlight(f.read(), PythonLexer(), HtmlFormatter(linespans='line'))
                code_css = HtmlFormatter(linespans='line').get_style_defs('.highlight')
            calling_code_html = os.path.join( folder, str(datetime.datetime.now()).replace(' ','-')+'.html' )
            with open( calling_code_html, 'w' ) as html_file:
                tmp = HTML_HULL.replace( '<!--PLACEHOLDER-->',
    """<p class='p_image'><img src='"""+full_img_filename+"""'/><br/>
                       <pre>"""+full_img_filename+( "-" + comment if comment else "" )+"</pre></p>"
                       +("caller: <a href='"+calling_code_html+"#line-"+str(code.co_firstlineno)+"'>"+caller_filename+"</a>" if track_caller else "")
                       +
                       "<br/>"
                       + code_html ).replace( '<!--STYLEPLACEHOLDER-->', code_css + "\n#line-"+str(code.co_firstlineno) + "{ background-color: #ddff36;} html, body {font-family: Verdana,sans-serif;} a {text-decoration: none; color: hotpink; } a:visited { color: grey; }" )
                html_file.write(tmp)

    with open( folder + '/' + html_filename, 'r' ) as html_file:
        html_old = html_file.read()
    with open( folder + '/' + html_filename, 'w' ) as html_file:
        html_file.write( html_old.replace( '<!--PLACEHOLDER-->',
"""<!--PLACEHOLDER-->
<p class='p_image'><img src='"""+full_img_filename+"""'/><br/>
                   <pre>"""+full_img_filename+( "-" + comment if comment else "" )+"</pre>"
                   +("caller: <a href='"+calling_code_html+"#line-"+str(code.co_firstlineno)+"'>"+caller_filename+"</a>" if track_caller else "")
                   +"</p>").replace( '<!--STYLEPLACEHOLDER-->', 'html, body {font-family: Verdana,sans-serif;} a {text-decoration: none; color: hotpink; } a:visited { color: grey; }' ) )
    if verbose:
        print('plot viewable in=', full_html_filename)

def caller():
    from matplotlib import pyplot as plt
    plt.plot(range(10),range(10))
    show( plt )
