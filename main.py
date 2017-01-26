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

class SignupHandler(webapp2.RequestHandler):

    def build_form(self, user_error="", username="",
        pass_error="", em_error="", email=""):

        error_message = "Not a valid {}"

        username_label = "<label>Username: </label>"
        username_input = "<input type='text' name='username' value='%(username)s'/>"
        username_error = "<div style='color:red'>%(user_error)s</div>"
        username_error_message = error_message.format('username')
        username_field = username_label + username_input + username_error

        password_one_label = "<label>Password: </label>"
        password_input = "<input type='password' name='password'/>"
        password_error = "<div style='color:red'>%(pass_error)s</div>"
        password_error_message = error_message.format('password')
        password_one = password_one_label + password_input + password_error

        password_two_label = "<label> Re-enter Password: </label>"
        password_two = password_two_label + password_input

        email_label = "<label>Email Address (optional): </label>"
        email_input = "<input type ='text' name='email' value='%(email)s'/>"
        email_error = "<div style='color:red'>%(em_error)s</div>"
        email_error_message = error_message.format('email')
        email_field = email_label + email_input + email_error

        form = ("<form method='post'>" + username_field + "<br>" +
            password_one + "<br>" + password_two + "<br>" +
            email_field + "<br>" + "<input type='submit'/>" + "</form>")

        self.response.write(form %{"username":username, "user_error":user_error,
            "pass_error":pass_error, "email":email, "em_error":em_error})

    def get(self):
        self.build_form()

    def post(self):

        self.response.write("Hello")


app = webapp2.WSGIApplication([
    ('/', SignupHandler)
], debug=True)
