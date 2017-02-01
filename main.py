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
import webapp2
import cgi
import re

class SignupHandler(webapp2.RequestHandler):

    def build_form(self, user_error="", username="",
        pass_error="", pass_two_error="", em_error="", email=""):

        username_label = "<label>Username: </label>"
        username_input = "<input type='text' name='username' value='%(username)s'/>"
        username_error = "<div style='color:red'>%(user_error)s</div>"
        username_field = username_label + username_input + username_error

        password_one_label = "<label>Password: </label>"
        password_one_input = "<input type='password' name='password_one'/>"
        password_one_error = "<div style='color:red'>%(pass_error)s</div>"
        password_one = password_one_label + password_one_input + password_one_error

        password_two_label = "<label> Re-enter Password: </label>"
        password_two_input = "<input type='password' name='password_two'/>"
        password_two_error = "<div style='color:red'>%(pass_two_error)s</div>"
        password_two = password_two_label + password_two_input + password_two_error

        email_label = "<label>Email Address (optional): </label>"
        email_input = "<input type ='text' name='email' value='%(email)s'/>"
        email_error = "<div style='color:red'>%(em_error)s</div>"
        email_field = email_label + email_input + email_error

        form = ("<form method='post'>" + username_field + "<br>" +
            password_one + "<br>" + password_two + "<br>" +
            email_field + "<br>" + "<input type='submit'/>" + "</form>")

        self.response.write(form %{"username":username, "user_error":user_error,
            "pass_error":pass_error, "pass_two_error":pass_two_error, "email":email, "em_error":em_error})

    def valid_username(self, username):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return USER_RE.match(username)

    def valid_password_one(self, password_one):
        USER_RE = re.compile(r"^.{3,20}$")
        return USER_RE.match(password_one)

    def valid_email(self, email):
        USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return USER_RE.match(email)

    def valid_password_two(self, password_one, password_two):
        return password_one == password_two

    def get(self):
        self.build_form()

    def post(self):
        username_test = self.valid_username(self.request.get('username'))
        password_one_test = self.valid_password_one(self.request.get('password_one'))
        password_two_test = self.valid_password_two(self.request.get('password_one'), self.request.get('password_two'))
        email_test = self.valid_email(self.request.get('email'))

        if username_test and password_one_test and password_two_test and email_test:
            return self.redirect("/thanks")

        if self.request.get('email') == "":
            if username_test and password_one_test and password_two_test:
                return self.redirect("/thanks")

        if not username_test:
            user_error = "Not a valid {}".format('username')
        else:
            user_error = ""

        if not password_one_test:
            pass_error = "Not a valid {}".format('password')
        else:
            pass_error = ""

        if not password_two_test:
            pass_two_error = "Passwords must be indentical"
        else:
            pass_two_error = ""

        if self.request.get('email') == "":
            em_error = ""
            return self.build_form(user_error, self.request.get('username'),
            pass_error, pass_two_error, em_error, self.request.get('email'))

        if not email_test:
            em_error = "Not a valid {}".format('email')
        else:
            em_error = ""

        return self.build_form(user_error, self.request.get('username'),
        pass_error, pass_two_error, em_error, self.request.get('email'))


class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thank you for signing up!")

app = webapp2.WSGIApplication([
    ('/', SignupHandler),
    ('/thanks', ThanksHandler)
], debug=True)
