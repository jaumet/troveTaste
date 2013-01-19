from django.http import HttpResponse
from django.shortcuts import render_to_response
from urllib import pathname2url
from trove_txt.models import Queries

class configs:
    ###########################
    ## CONFIGS
    ## trove totals per zone:
    troveTotals = {
	"total": 247732527,
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
	"total": "grey",
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

    ##  troveTotalRecords
    troveTotalRecords = 247732527 #sum(troveTotals.values())

    ## Stop words list from http://jmlr.csail.mit.edu/papers/volume5/lewis04a/a11-smart-stop-list/english.stop
    stopWords = ["a", "a's", "able", "about", "above", "according", "accordingly", "across", "actually", "after", "afterwards", "again", "against", "ain't", "all", "allow", "allows", "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "an", "and", "another", "any", "anybody", "anyhow", "anyone", "anything", "anyway", "anyways", "anywhere", "apart", "appear", "appreciate", "appropriate", "are", "aren't", "around", "as", "aside", "ask", "asking", "associated", "at", "available", "away", "awfully", "b", "be", "became", "because", "become", "becomes", "becoming", "been", "before", "beforehand", "behind", "being", "believe", "below", "beside", "besides", "best", "better", "between", "beyond", "both", "brief", "but", "by", "c", "c'mon", "c's", "came", "can", "can't", "cannot", "cant", "cause", "causes", "certain", "certainly", "changes", "clearly", "co", "com", "come", "comes", "concerning", "consequently", "consider", "considering", "contain", "containing", "contains", "corresponding", "could", "couldn't", "course", "currently", "d", "definitely", "described", "despite", "did", "didn't", "different", "do", "does", "doesn't", "doing", "don't", "done", "down", "downwards", "during", "e", "each", "edu", "eg", "eight", "either", "else", "elsewhere", "enough", "entirely", "especially", "et", "etc", "even", "ever", "every", "everybody", "everyone", "everything", "everywhere", "ex", "exactly", "example", "except", "f", "far", "few", "fifth", "first", "five", "followed", "following", "follows", "for", "former", "formerly", "forth", "four", "from", "further", "furthermore", "g", "get", "gets", "getting", "given", "gives", "go", "goes", "going", "gone", "got", "gotten", "greetings", "h", "had", "hadn't", "happens", "hardly", "has", "hasn't", "have", "haven't", "having", "he", "he's", "hello", "help", "hence", "her", "here", "here's", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "hi", "him", "himself", "his", "hither", "hopefully", "how", "howbeit", "however", "i", "i'd", "i'll", "i'm", "i've", "ie", "if", "ignored", "immediate", "in", "inasmuch", "inc", "indeed", "indicate", "indicated", "indicates", "inner", "insofar", "instead", "into", "inward", "is", "isn't", "it", "it'd", "it'll", "it's", "its", "itself", "j", "just", "k", "keep", "keeps", "kept", "know", "knows", "known", "l", "last", "lately", "later", "latter", "latterly", "least", "less", "lest", "let", "let's", "like", "liked", "likely", "little", "look", "looking", "looks", "ltd", "m", "mainly", "many", "may", "maybe", "me", "mean", "meanwhile", "merely", "might", "more", "moreover", "most", "mostly", "much", "must", "my", "myself", "n", "name", "namely", "nd", "near", "nearly", "necessary", "need", "needs", "neither", "never", "nevertheless", "new", "next", "nine", "no", "nobody", "non", "none", "noone", "nor", "normally", "not", "nothing", "novel", "now", "nowhere", "o", "obviously", "of", "off", "often", "oh", "ok", "okay", "old", "on", "once", "one", "ones", "only", "onto", "or", "other", "others", "otherwise", "ought", "our", "ours", "ourselves", "out", "outside", "over", "overall", "own", "p", "particular", "particularly", "per", "perhaps", "placed", "please", "plus", "possible", "presumably", "probably", "provides", "q", "que", "quite", "qv", "r", "rather", "rd", "re", "really", "reasonably", "regarding", "regardless", "regards", "relatively", "respectively", "right", "s", "said", "same", "saw", "say", "saying", "says", "second", "secondly", "see", "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves", "sensible", "sent", "serious", "seriously", "seven", "several", "shall", "she", "should", "shouldn't", "since", "six", "so", "some", "somebody", "somehow", "someone", "something", "sometime", "sometimes", "somewhat", "somewhere", "soon", "sorry", "specified", "specify", "specifying", "still", "sub", "such", "sup", "sure", "t", "t's", "take", "taken", "tell", "tends", "th", "than", "thank", "thanks", "thanx", "that", "that's", "thats", "the", "their", "theirs", "them", "themselves", "then", "thence", "there", "there's", "thereafter", "thereby", "therefore", "therein", "theres", "thereupon", "these", "they", "they'd", "they'll", "they're", "they've", "think", "third", "this", "thorough", "thoroughly", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "took", "toward", "towards", "tried", "tries", "truly", "try", "trying", "twice", "two", "u", "un", "under", "unfortunately", "unless", "unlikely", "until", "unto", "up", "upon", "us", "use", "used", "useful", "uses", "using", "usually", "uucp", "v", "value", "various", "very", "via", "viz", "vs", "w", "want", "wants", "was", "wasn't", "way", "we", "we'd", "we'll", "we're", "we've", "welcome", "well", "went", "were", "weren't", "what", "what's", "whatever", "when", "whence", "whenever", "where", "where's", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "who's", "whoever", "whole", "whom", "whose", "why", "will", "willing", "wish", "with", "within", "without", "won't", "wonder", "would", "would", "wouldn't", "x", "y", "yes", "yet", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "z", "zero"]

###########################


def index(request):
    troveTotalRecords = configs.troveTotalRecords
    troveTotals = configs.troveTotals
    return render_to_response('index.html', {'troveTotalRecords': troveTotalRecords, 'troveTotals': troveTotals})

def cercle(request):
    return render_to_response('testcercles.html')

def about(request):
    return render_to_response('about.html')

def test(request):
    myvar = "this is my silly var."
    return render_to_response('test.html', {'myvar': myvar})


def comparing(request, query):
    if request.is_ajax():
        import json
        comparingList = []
        query = pathname2url(query)
        myrow = ''
        # List of zones:
	from operator import itemgetter
	myDictZones = sorted(configs.troveTotals.items(), key=itemgetter(1), reverse=True)
        for zone, v in myDictZones:
            # Getting the zone value for the this query
            myzone = "int(Queries.objects.filter(query='"+query+"')[0]."+zone+")"
            myzone = eval(myzone)
            # Getting 3 queries under
            my3under = "Queries.objects.values('query','"+zone+"').order_by('-"+zone+"').filter("+zone+"__lt="+str(myzone)+")[:5]"
            my3under = eval(my3under)
            # Getting the 2 queries over
            my3over = "Queries.objects.values('query','"+zone+"').order_by('"+zone+"').filter("+zone+"__gt="+str(myzone)+")[:5]"
            my3over = eval(my3over)

            def do_tr(myvalues, zone, which):
                # Building the HTML table output
                mystr = ''
                # A trick for the order of the compared items:
                if which == "over":
                    myrange = range(4, -1,-1)
                else:
                    myrange = range(0,5)

                for f in myrange:
                    try:
                        mystr += '<td>'+str(myvalues[f]["query"])+'<br />'+str(myvalues[f][zone])+'</td>'
                    except:
                        if which == "over":
                            mystr = '<td>&nbsp;</td>'+mystr
                        else:
                            mystr += '<td>&nbsp;</td>'
                return mystr

            myrow += '<tr>'+do_tr(my3over, zone, "over")+'<td><h3 style="color:'+configs.troveColors[zone]+';"><a href="http://trove.nla.gov.au/result?&q-type0=all&q-term0='+query+'&q-field1=title%3A&q-type1=all&q-field2=creator%3A&q-type2=all&q-field3=subject%3A&q-type3=all&l-advformat='+configs.troveColors[zone]+'" class="ext" style="color:'+configs.troveColors[zone]+';">'+zone+'</a><br />('+str(myzone)+')</h3></td>'+do_tr(my3under, zone, "under")+'</tr>'
        myTable = '<table><tr><td></td><td></td><td><h2>More tasty</h2></td><td></td><td></td><td><h1>'+query.replace('%20', ' ')+'</h1></td><td></td><td><h2>less tasty</h2></td><td></td><td></td><td></td></tr>'+myrow+'</table>'
    else:
        myTable = "Sorry, this query is not allowed"
    return HttpResponse(myTable, mimetype='application/html')

def trove_query(request, query):
    if query not in configs.stopWords:
        # Encoding query:
        query = pathname2url(query);
        if request.is_ajax():
            import json
            import urllib2
            import math
            from operator import itemgetter

            # Building API url:
            base = 'http://api.trove.nla.gov.au/result?' # fixed value!
            mykey = "key=mljedjjo4e7om4l7" # fixed value!
            amp = '&'
            zone = 'zone=all'
            #zone = 'zone=book%2Call'
            #zone = 'zone=book%2Cpicture%2Carticle%2Cmusic%2Cmap%2Ccollection%2Cnewspaper%2Clist%2Cpeople'
            encoding = 'encoding=json' # fixed value!
            q = 'q='+query

            url = base+mykey+amp+zone+amp+encoding+amp+q

            # getting the JSON file
            s = urllib2.urlopen(url)
            data = json.load(s)
            # Transforming troveJSON to myJSON
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
            # looks like JSON needs double quotes, not simple ones!
            myjson = myjson.replace("\'", "\"")
            # Saving query + results to the ddbb. ONLY if the query is not already there
            m = Queries.objects.filter(query=query)
            if len(m) == 0:
                mydict = dict(map(lambda x: (x["name"], x["number"]), myjson2save))
                mydict["total"]=sum(mydict.values())
                mydict["query"]=query
                m = Queries(**mydict)
                m.save()
        else:
            myjson = '{"message": "Sorry this page is not directly accessible!"}'
    else:
        myjson = '{"message": "Sorry, this query is not allowed"}'
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
