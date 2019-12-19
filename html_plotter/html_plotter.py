import datetime
import os
TMP_FOLDER = '/tmp'

def show(plt, comment=None, folder=os.path.join(TMP_FOLDER, 'matplotlib'), html_filename='index.html', verbose=True):
    """
    Plot to a png file and append <img> in a html file.
    """
    if not os.path.isdir( folder ):
        os.mkdir( folder )
    full_html_filename = os.path.join( folder, html_filename )
    if not os.path.isfile( full_html_filename ):
        with open( folder + '/' + html_filename, 'w' ) as html_file:
            html_file.write("""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<style type="text/css">
</style>
</head>
<body>
<!--PLACEHOLDER-->
</body>""")
    full_img_filename = os.path.join( folder, str(datetime.datetime.now()).replace(' ','-').replace('.','').replace(':','') + '.png' )
    plt.savefig( full_img_filename )
    plt.gcf().clear()
    with open( folder + '/' + html_filename, 'r' ) as html_file:
        html_old = html_file.read()
    with open( folder + '/' + html_filename, 'w' ) as html_file:
        html_file.write( html_old.replace( '<!--PLACEHOLDER-->',
"""<!--PLACEHOLDER-->
<p class='p_image'><img src='"""+full_img_filename+"""'/><br/>
                   <pre>"""+full_img_filename+( "-" + comment if comment else "" )+"</pre></p>") )
    if verbose:
        print('plot viewable in=', full_html_filename)
