""" simple example that copies contents at 
some web URL to a local file.  Things to note:
Resource we are fetching must exist. Check using browser
need permission to write to the destination filename, and the
file will be crated in the "current directory. Same folder
that the Python program is saved in.s
"""

import urllib.request

def retrieve_page(url):
    """ Retrieve contents of a web page """
    my_socket = urllib.request.urlopen(url)
    dta = my_socket.read()
    return dta

the_text = retrieve_page("https://google.com")
print(the_text)