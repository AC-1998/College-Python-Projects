###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: Objects and Classes
# Description: write a Python3 program that takes the URL of the National
#              Academy of Science and a list of topics.
#              For each topic of interest, your solution intelligence will
#              compute the number of instances of each topic on the NAS website
#              providing a simple yet complete report.
# Date: 04/18/2023
import datetime
import re
import urllib.request

# URL of the NAS website
url = "http://www.nasonline.org"

# Download the HTML document
response = urllib.request.urlopen(url)
html_content = response.read().decode('utf-8')

# List of topics under review
topics = ['research', 'climate', 'evolution', 'cultural', 'leadership',
          'technology']

# Count the number of occurrences of each topic
topic_count = {}
for topic in topics:
    count = len(re.findall(topic, html_content, re.IGNORECASE))
    topic_count[topic] = count

# Generate the date of the report run
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Print the report summary
print("Report Summary:")
print("Today's date of the report is: {}".format(date))
for topic in topic_count.keys():
    count = topic_count[topic]
    print("Topic: {} appears: {} times.".format(topic, count))

# Test Run
'''
Report Summary:
Today's date of the report is: 2023-04-18 15:29:10
Topic: research appears: 16 times.
Topic: climate appears: 5 times.
Topic: evolution appears: 4 times.
Topic: cultural appears: 8 times.
Topic: leadership appears: 4 times.
Topic: technology appears: 4 times.

'''