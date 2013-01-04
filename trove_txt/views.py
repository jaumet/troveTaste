from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.views.decorators.csrf import csrf_protect
#from django.template import RequestContext
#from django.utils import simplejson
from trove_txt.models import Queries

class configs:
    ###########################
    ## CONFIGS
    ## trove totals per zone:
    troveTotals = {
        "article": 142458865,
        "newspaper": 78533033,
        "book": 17428770,
        "picture": 4903410,
        "music": 2553743,
        "people": 913785,
        "collection": 532151,
        "map": 389341,
        "list": 19429
    }
    troveColors = {
        "article": "#ff7f0e",
        "newspaper": "#2ca02c",
        "book": "#d62728",
        "picture": "#bcbd22",
        "music": "#9467bd",
        "people": "#8c564b",
        "collection": "#17becf",
        "map": "#1f77b4",
        "list": "#e377c2"
    }

    #num-map {background-color:;}
    #num-book {background-color:;}
    #num-music {background-color:;}
    #num-people {background-color:;}
    #num-newspaper {background-color:;}
    #num-article {background-color:;}
    #num-list {background-color:;}
    #num-collection {background-color:;}
    #num-picture {background-color:;}
    #total-records {background-color:#7f7f7f;}

    ##  troveTotalRecords
    troveTotalRecords = sum(troveTotals.values())

    ## Stop words list
    stopWords = ['a', 'be']
    ###########################


def index(request):
    troveTotalRecords = configs.troveTotalRecords
    troveTotals = configs.troveTotals
    return render_to_response('index.html', {'troveTotalRecords': troveTotalRecords, 'troveTotals': troveTotals})

def cercle(request):
    return render_to_response('testcercles.html')

def test(request):
    myvar = "this is my silly var."

    return render_to_response('test.html', {'myvar': myvar})

def trove_query(request, query):
    # Encoding query:
    from urllib import pathname2url
    query = pathname2url(query);

    if request.is_ajax():
        import json
        import urllib2
        import math
        from operator import itemgetter

        # Building API url:
        base = 'http://api.trove.nla.gov.au/result?' # fix value!
        mykey = "key=mljedjjo4e7om4l7" # fix value!
        amp = '&'
        zone = 'zone=all'
        encoding = 'encoding=json' # fix value!
        q = 'q='+query

        url = base+mykey+amp+zone+amp+encoding+amp+q

        # getting the JSON file
        s = urllib2.urlopen(url)
        data = json.load(s)
        # Transforming troveJSON to myJSON
        #>>> json["response"]["zone"][0]["name"]
        #'people'
        #>>> json["response"]["zone"][0]["records"]["total"]
        myjson = []
        myjson2save = []
        mydict = {}
        for zone in data["response"]["zone"]:
            myzone = int(zone["records"]["total"])
            zonetotal = configs.troveTotals[zone["name"]]
            permil = int((myzone*1000.0/zonetotal))
            if myzone>0:
                logzone = int(round(10*math.log10(myzone)))
            else:
                logzone = 0
            myjson.append({"name":str(zone["name"]), "color":str(configs.troveColors[zone["name"]]),  "r":logzone, "x":permil})
            myjson2save.append({"name":str(zone["name"]), "number": myzone})
        myjson = sorted(myjson,key=itemgetter('r'), reverse=True)
        myjson = str(myjson)
        # JSON needs double quotes, not simple ones!
        myjson = myjson.replace("\'", "\"")
        # Saving query + results to the ddbb:
        mydict = dict(map(lambda x: (x["name"], x["number"]), myjson2save))
        mydict["total"]=sum(mydict.values())
        mydict["query"]=query
        m = Queries(**mydict)
        m.save()
    else:
        myjson = "Sorry this page is not directly accessible!"
    return HttpResponse(myjson, mimetype='application/json')

def get(request):

    # method vars
    query = ''
    html_out = ''

    # getting POSted form:
    if request.GET['query'] and request.GET['query'] not in configs.stopWords:
        query = request.GET['query']

        # Encoding query string
        from urllib import pathname2url
        query = pathname2url(query);

        import json
        import xmltodict
        import urllib2
        import math
        #from pprint import pprint

        # Building API url:
        base = 'http://api.trove.nla.gov.au/result?' # fix value!
        mykey = "key=mljedjjo4e7om4l7" # fix value!
        amp = '&'
        s = 's=0'
        n = 'n=0'
        zone = 'zone=book%2Cmap'
        encoding = 'encoding=xml' # fix value!
        q = 'q='+query

        url = base+mykey+amp+zone+amp+s+amp+n+amp+encoding+amp+q

        # getting the XML file
        s = urllib2.urlopen(url)
        # XML to dictionary
        values = xmltodict.parse(s)

        #pprint(values['response']['zone'])
        mytrovetotal = 0
        html_out = "<table>\n"
        html_out +=  "<tr><td>name</td><td>zonelog</td><td>myzone</td><td> %</td><td> &permil; </td><td>log(&permil)</td></tr>\n"
        for o in values['response']['zone']:
            zonetotal = configs.troveTotals[o['@name']]
            myzone = int(o['records']['@total'])
            percent = (myzone*100.0)/zonetotal
            permil = (myzone*1000.0)/zonetotal
            if percent>0:
                log = math.log10(permil)
                zonelog = math.log10(myzone)
            else:
                log = "-"
                zonelog = "-"
            html_out +=  "<tr><td>"+o['@name']+"</td><td>"+str(zonelog)+"</td><td>"+str(myzone)+"</td><td>"+str(percent)+" %</td><td>"+str(permil)+"  &permil; </td><td>"+str(log)+"</td></tr>\n"
            mytrovetotal += myzone
        percent = (mytrovetotal*1000.0)/configs.troveTotalRecords
        html_out +=  "<tr><td>Total</td><td>"+str(mytrovetotal)+"</td><td>"+str(percent)+"  &permil; </tg></tr>\n"
        html_out +=  "</table>\n"
    else:
        html_out = "<h1>Sorry, no acceptable query<br /> Please try again if you like so</h1>"
    return render_to_response('test.html', {'query': query, 'troveTotalRecords': configs.troveTotalRecords, 'html_out': html_out})