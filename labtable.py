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
            <table method="get" action="generate" border="2">
            <tr>
            	<th> Name</th>
            	<th> # of Brains Completed </th>
            </tr>
            <tr>
            	<td>Olivia</td>
            	<td align="center">25</td>
            </tr>
            <tr>
            	<td>Yunxiang</td>
            	<td align="center">35</td>
            </tr>
            <tr>
            	<td>Sid</td>
            	<td align="center">15</td>
            </tr>
            <tr>
            	<td>Anu</td>
            	<td align="center">20</td>
            </tr>
            </table>
          </body>
        </html>"""
        return htmlTable.CountRaters('BSNIP2')

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())