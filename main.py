#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os #os library built into python. 

import webapp2
import jinja2 #jijna is a template library built into google app engine. There are many template libraries out there but we are gonna use jinja

#lets initialize jinja 

template_dir = os.path.join(os.path.dirname(__file__), 'templates') #os.path.join is used to concatinate two filenames. __file__ is the current directory you are in. 
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True) # we are instantiating jinja environment. 


form_html = """
<form>
<h2> Add a Food</h2>
<input type = "text" name = "food">
%s
<button>Add</button>
</form>
 """

hidden_html= """ <input type = "hidden" name = "food" value = "%s"> """

item_html = """ <li>%s</li>"""

shopping_list_html = """ 
<br>
<br>
<h2> Shopping List </h2>
<ul>
%s
</ul>
"""


class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainHandler(Handler):
    def get(self):
    	items = self.request.get_all('food')
    	self.render("shoppinglist.html", items = items)
    	# n = self.request.get("n")
    	# if n:
    	# 	n = int(n) #the get request always returns a string. so You will need to change it to integer to utilize the value of n. 
    	# 				#if you wanted to use n as a string then you could check if the input is all digits and then convert it to int otherwise process it as a string. 

    	# self.render("shoppinglist.html", n = n)


    	# self.render("shoppinglist.html", name = "Bhavesh")

    	# output = form_html
    	# output_hidden = ""
    	# items = self.request.get_all("food") # gets all items for food and stores it in a list 

    	# if items:
    	# 	output_items = ""
    	# 	for item in items:
    	# 		output_hidden += hidden_html %item
    	# 		output_items += item_html %item

    	# 	output_shopping = shopping_list_html % output_items
    	# 	output += output_shopping

    	# output = output % output_hidden


     #    self.write(output)
class FizzBuzz(Handler):
	def get(self):
		n = self.request.get('n', 0)
		if n:
			n= int(n)
		self.render("FizzBuzz.html", n = n)

app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/FizzBuzz', FizzBuzz)
], debug=True)
