#
# This is a comment block and is ignored by the interpreter.
#
# This program will build a webpage using a template that references the
# variables defined below.
#
# TODO:
#
#     - Add a "author" key in the "template_vars" dictionary below that
#       references the "USER" environment variable
#
#     - Add a "domain" key in the "template_vars" dictionary below that
#       reads the reads the domain name of the website from a program
#       argument specified when executing the program
#

import sys

#
# If there aren't enough arguments supplied, print a help message
#
if len(sys.argv) < 3:
    help = """usage: {name} <outfile> <domain>

    Creates a webpage based on a template.

    <outfile> is the filename of the resulting webpage
    <domain> is the domain name where the webpage will be hosted"""
    print(help.format(name=sys.argv[0]))
    exit(1)


#
# Define the template variables
#
template_vars = {
    "title": "Example Org Inc.",
    "motto": "A positive example for all"
}

#
# Set the outfile
#
outfile = sys.argv[1]


#
# Process the template
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

with open(outfile, 'w') as f:
    f.write(template.format(**template_vars))
