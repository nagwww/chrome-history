#!/usr/bin/python

import csv
import time
import json
import requests
from urlparse import urlparse


def post_es(rs_json):
    es_url = "localhost"
    port = "7104"
    index = "nag_{}".format(time.strftime('%Y%m%d'))
    es_type = "default"
    es_url = "http://{}:{}/{}/{}".format(es_url, port, index, es_type)
    try:
        r = requests.post(es_url, data=json.dumps(rs_json))
        if str(r.status_code) in "200":
            return True
    except Exception as ex:
        print "Issues posting to ES", ex


if __name__ == "__main__":
    print "Starting"
    with open('my-history1.csv') as csvfile:
        line = csv.reader(csvfile, delimiter=',')
        for row in line:
            data = {}
            url = urlparse(row[1])
            data["url_date"] = row[0]
            data["site"] = url.netloc
            print post_es(data)
