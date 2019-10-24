import webapp2
import json
import os
import urllib2
import random
import jinja2
from database import defaultdatas
from Images import ImageInfo, fetchNearByImages
from test import test
from database import loadlayer3

the_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],autoescape=True)


def getData():
      return ImageInfo.query(ImageInfo.level==1).order().fetch()

class Home(webapp2.RequestHandler):
    def get(self):
        test()
        homepage = the_jinja_env.get_template('/template/mosaic.html')
        self.response.write(homepage.render( {"data":getData()}))

class AddImage(webapp2.RequestHandler):
    def get(self):
        homepage = the_jinja_env.get_template('/template/addImages.html')
        self.response.write(homepage.render())
class loadImages(webapp2.RequestHandler):
    def get(self):  
        defaultdatas()
        # loadlayer3()
        homepage = the_jinja_env.get_template('/template/mosaic.html')
        self.response.write(homepage.render({"data":getData()}))
class update(webapp2.RequestHandler):
    def get(self):
        location=int(self.request.GET.get('location'))
        layer=int(self.request.GET.get('layer'))
        datasentback=fetchNearByImages(location,layer)
        self.response.write(json.dumps(datasentback))

      
        

       


        


app = webapp2.WSGIApplication([
('/',Home),
('/addImage',AddImage),
 ('/load', loadImages),
 ('/update', update)
# ('/contact',Contact),
# ('/login',LoginPage)
], debug=True)

