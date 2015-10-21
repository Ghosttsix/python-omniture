import omniture
import sys
import os
from pprint import pprint

user = os.environ['OMNITURE_USERNAME']
secret = os.environ['OMNITURE_SECRET']
analytics = omniture.authenticate(user, secret)

# print analytics.suites
print(analytics.suites['gamestopprod'])
# print(analytics.suites['snestorescea-uat'])
network = analytics.suites['gamestopprod']
# pprint(network.segments)
print(network.metrics)
print(network.elements)
print(network.segments)
#
# segments = [
#     'UK (Locked)',
#     'US (Locked)',
#     ]
#
# queue = []
#
# for segment in segments:
#     report = network.report \
#         .range('2013-05-01', '2013-05-31', granularity='day') \
#         .over_time(metrics=['pageviews']) \
#         .filter(segment=segment)
#
#     queue.append(report)
#
#
# def heartbeat():
#     sys.stdout.write('.')
#     sys.stdout.flush()
#
# reports = omniture.sync(queue, heartbeat)
#
# for report in reports:
#     print(report.segment)
#     print(report.data['pageviews'])

