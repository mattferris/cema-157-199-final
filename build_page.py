#
# This is a comment block and is ignored by the interpreter.
#
# This program will build a webpage using a template that references the
# variables defined below.
#
# TODO:
#
#     - Add a "author" key in the "config" dictionary below that
#       references the "USER" environment variable
#
#     - Add a "domain" key in the "config" dictionary below that
#       reads the reads the domain name of the website from a program
#       argument specified when executing the program
#

config = {
    "title": "Example Org Inc.",
    "motto": "A positive example for all"
}


#
# Do not make changes below this point
#

template = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <p>{motto}</p>
    <p>Hosted at {domain}, created by {author}</p>
  </body>
</html>"""

print(template.format(**config))
