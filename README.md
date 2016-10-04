# Introduction
Import Chrome web browser history to elaticsearch for further analysis

- Step1 :  Navigate to "cd ~/Library/Application\ Support/Google/Chrome/Default/History"

- Step 2 : sqlite3 History
           sqlite> .headers on
           sqlite> .mode csv
           sqlite> .output my-hisotry1.csv
           sqllie> SELECT datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime'), url 
- Step 3 : Setup ElasticSearch on your localhost
- Step 4 : Create the template in ES as : ./create_elasticsearch_template.sh
- Step 5 : Import the history to ES as : python ./chrome.py
