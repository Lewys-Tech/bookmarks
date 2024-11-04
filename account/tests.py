from django.test import TestCase

# Create your tests here.
# {% extends "base.html" %}

# {% block title %}
#   Log-in
# {% endblock %}

# {% block content %}
#   <h1>Log-in</h1>
#   <p>Please, use the following form to log-in:</p>
#   <form method="post">
#     {{ form.as_p }}
#     {% csrf_token %}
#     <p><input type="submit" value="Log in"></p>
#   </form>
# {% endblock %}

# {% load static %}
# <!DOCTYPE html>
# <html>
#   <head>
#     <title>{% block title %}{% endblock %}</title>
#     <link href="{% static "css/base.css" %}" rel="stylesheet">
#   </head>
#   <body>
#     <div id="header">
#       <span class="logo">Bookmarks</span>
#     </div>
#     <div id="content">
#       {% block content %}{% endblock %}
#     </div>
#   </body>
# </html>