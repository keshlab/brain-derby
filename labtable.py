import random
import string
import cherrypy
import htmlTable

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
						%s
          </body>
        </html>""" % htmlTable.CountRaters('BSNIP2')

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
