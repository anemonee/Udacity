import json
import codecs
import requests

API_KEY = {"popular": "06bda414847a45e79481695626e0584d", "article": "06bda414847a45e79481695626e0584d"}
params = {"api-key": API_KEY["popular"], "offset": 20}
path =  "https://api.nytimes.com/svc/mostpopular/v2/"


def query_nytimes_popular_articles(type,section,timeperiod):
    url = path + "most{0}/{1}/{2}.json".format(type,section,timeperiod)
    r = requests.get(url, params=params)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


data = query_nytimes_popular_articles("viewed","all-sections",1)
print data["num_results"]

with codecs.open("output.json", encoding='utf-8', mode='w') as v:
    v.write(json.dumps(data, indent=2))


with open("output.json", 'r') as f:
    data_py = json.loads(f.read())
    out_list = []
    urls = []
    for item in data_py["results"]:
        out_list.append({item["section"]: item["title"]})
        for item2 in item["media"]:
            for item3 in item2["media-metadata"]:
                if item3["format"] == "Standard Thumbnail":
                  urls.append(item3["url"])

  #  for i in range(0, (len(data_py["results"]))):
   #     out_list.append({data_py["results"][i]["section"]: data_py["results"][i]["title"]})
   #     for j in range(0, len(data_py["results"][i]["media"][0]["media-metadata"])):
     #       if data_py["results"][i]["media"][0]["media-metadata"][j]["format"] == "Standard Thumbnail":
      #          urls.append(data_py["results"][i]["media"][0]["media-metadata"][j]["url"])

print (out_list, urls)
