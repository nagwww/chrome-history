#curl -XDELETE http://localhost:7104/_template/nag
#curl -XDELETE http://localhost:7104/nag_*
curl -XPUT http://localhost:7104/_template/nag -d '
{
    "template" : "nag_*",
    "settings" : {
        "number_of_shards" : 1
    },
    "mappings": {
         "_default_": {
          "date_detection": false,
                  "properties": {
                      "url_date": {
                           "type": "date",
                            "format": "date_time" }

                   }
          }
    }
}'
