from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.views.decorators.csrf import csrf_protect
#from django.template import RequestContext
from django.utils import simplejson
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
        "list": 19429}

    ##  troveTotalRecords
    troveTotalRecords = sum(troveTotals.values())

    ## Stop words list
    stopWords = ['a', 'be']
    ###########################


def index(request):
    troveTotalRecords = configs.troveTotalRecords
    troveTotals = configs.troveTotals
    return render_to_response('index.html', {'troveTotalRecords': troveTotalRecords, 'troveTotals': troveTotals})

def test(request):
    myvar = "this is my silly var."

    return render_to_response('test.html', {'myvar': myvar})

def trove_query(request, query):
    if request.is_ajax():
        import json
        #import xmltodict
        import urllib2
        #from pprint import pprint

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
        # Transforming JSON to JSON
        #>>> json["response"]["zone"][0]["name"]
        #'people'
        #>>> json["response"]["zone"][0]["records"]["total"]
        myjson = []
        for zone in data["response"]["zone"]:
            myjson.append({"name":str(zone["name"]), "total":int(zone["records"]["total"])})
        myjson = str(myjson)
        myjson = myjson.replace("\'", "\"")

    else:
        myjson = "Sorry this ,ethod is not allowed!"
    #json = simplejson.dumps(message)
    #return HttpResponse(json, mimetype='application/json')
    return HttpResponse(myjson, mimetype='application/json')

def get(request):

    # method vars
    query = ''
    html_out = ''

    # getting POSted form:
    if request.GET['query'] and request.GET['query'] not in configs.stopWords:
        query = request.GET['query']

        import json
        import xmltodict
        import urllib2
        #from pprint import pprint

        # Building API url:
        base = 'http://api.trove.nla.gov.au/result?' # fix value!
        mykey = "key=mljedjjo4e7om4l7" # fix value!
        amp = '&'
        zone = 'zone=all'
        encoding = 'encoding=xml' # fix value!
        q = 'q='+query

        url = base+mykey+amp+zone+amp+encoding+amp+q

        # getting the XML file
        s = urllib2.urlopen(url)
        # XML to dictionary
        values = xmltodict.parse(s)

        #pprint(values['response']['zone'])
        mytrovetotal = 0
        html_out = "<table>\n"
        for o in values['response']['zone']:
            zonetotal = configs.troveTotals[o['@name']]
            myzone = int(o['records']['@total'])
            percent = (myzone*1000.0)/zonetotal
            html_out +=  "<tr><td>"+o['@name']+"</td><td>"+str(myzone)+"</td><td>"+str(percent)+"  &permil; </tg></tr>\n"
            mytrovetotal += myzone
        percent = (mytrovetotal*1000.0)/configs.troveTotalRecords
        html_out +=  "<tr><td>Total</td><td>"+str(mytrovetotal)+"</td><td>"+str(percent)+"  &permil; </tg></tr>\n"
        html_out +=  "</table>\n"
    else:
        html_out = "<h1>Sorry, no acceptable query<br /> Please try again if you like so</h1>"
    return render_to_response('test.html', {'query': query, 'troveTotalRecords': configs.troveTotalRecords, 'html_out': html_out})