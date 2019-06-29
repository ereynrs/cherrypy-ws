import os
import cherrypy

import os
from pathlib import Path
ACPATH = Path(os.path.dirname(__file__))

class mySaaS:

    @cherrypy.expose
    def index(self):
        return '''
        <?xml version="1.0"?>
        <p>Hi buddy!</p>
        <p> Welcome to our incredible SaaS platform...</p>
        <p>You can obtain contact details details about our employees <a href="contact_details">here</a></p>
        <p>You can obtain professional details details about our employees <a href="professional_details">here</a></p>
        </xml>'''


    @cherrypy.expose
    def contact_details(self):

        import json
        with open(str(ACPATH / 'contact_details.json'), 'r') as fp:
            data = json.load(fp)

        from jinja2 import Template
        template = Template('''
        <?xml version="1.0"?>
        {% for person in data %}
        <person href={{data[person]['uri']}}>
        <uri>{{data[person]['uri']}}</uri>
        <fullname>{{ data[person]['fullname'] }}</fullname>
        <phone>{{ data[person]['phone'] }}</phone>
        </person>
        {% endfor %}
        </xml>
        ''')
        return template.render(data=data)


    @cherrypy.expose
    def professional_details(self):

        import json
        with open(str(ACPATH / 'professional_details.json'), 'r') as fp:
            data = json.load(fp)

        from jinja2 import Template
        template = Template('''
        <?xml version="1.0"?>
        {% for person in data %}
        <person href={{data[person]['uri']}}>
        <uri>{{data[person]['uri']}}</uri>
        <fullname>{{ data[person]['fullname'] }}</fullname>
        <profession>{{ data[person]['profession'] }}</profession>
        <department>{{data[person]['department']}}</department>
        <salary>{{data[person]['salary']}}</salary>
        </person>
        {% endfor %}
        </xml>
        ''')
        return template.render(data=data)


    @cherrypy.expose
    def describe_john(self):

        import utils
        opener = utils.get_opener()
        return opener.open('http://localhost:5820/mySaaS#')


    @cherrypy.expose
    def describe_mary(self):

        import utils
        opener = utils.get_opener()
        return opener.open('http://localhost:5820/mySaaS#!/query/')

#server_conf = os.path.join(os.path.dirname(__file__), 'cherry-ws.conf')

if __name__ == '__main__':
    #cherrypy.quickstart(HelloWorld(), server_conf)
    cherrypy.quickstart(mySaaS())
