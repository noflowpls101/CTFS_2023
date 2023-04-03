#!/usr/bin/env python3

from flask import Flask, request, Response, redirect, render_template_string
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["50000 per hour"],
    storage_uri="memory://",
)

@app.route('/')
@limiter.limit("5/second")
def index():
    if 'num' not in request.args:
        return '''
<h1>Check if your number is even or odd!</h1>
<form action="/" method="get">
    Number: <input name="num" id='num' cols="15"></input>
    <input type="submit" value="Check"></input>
</form>
<a href='/source'>Source</a>
'''
    else:
        num = request.args['num']
        evenodd = even_or_odd(num)
        return render_template_string(
            f'The number {num} is {evenodd}.',
            num=num, evenodd=evenodd
        )

@app.route('/source')
@limiter.limit("5/second")
def source():
    return Response(open(__file__).read(), mimetype="text/plain")

def even_or_odd(num):
    if num == '1':
        return "odd"
    if num == '2':
        return "even"
    if num=='3':
        return 'odd'
    if num=='4':
        return 'even'
    if num=='5':
        return 'odd'
    if num=='6':
        return 'even'
    if num=='7':
        return 'odd'
    if num=='8':
        return 'even'
    if num=='9':
        return 'odd'
    if num=='10':
        return 'even'
    if num == '751089':
        return 'odd'
    if num == '994556':
        return 'even'
    if num == '880865':
        return 'odd'
    if num == '699472':
        return 'even'
    if num == '197278':
        return 'even'
    if num == '17743':
        return 'odd'
    if num == '691799':
        return 'odd'
    if num == '606588':
        return 'even'
    if num == '31409':
        return 'odd'
    if num == '240962':
        return 'even'
    if num == '443363':
        return 'odd'
    if num == '806388':
        return 'even'
    if num == '504346':
        return 'even'
    if num == '276072':
        return 'even'
    if num == '700999':
        return 'odd'
    if num == '285063':
        return 'odd'
    if num == '737738':
        return 'even'
    if num == '251207':
        return 'odd'
    if num == '531978':
        return 'even'
    if num == '858570':
        return 'even'
    if num == '955288':
        return 'even'
    if num == '66941':
        return 'odd'
    if num == '574008':
        return 'even'
    if num == '549675':
        return 'odd'
    if num == '271930':
        return 'even'
    if num == '203969':
        return 'odd'
    if num == '764824':
        return 'even'
    if num == '920663':
        return 'odd'
    if num == '20925':
        return 'odd'
    if num == '386875':
        return 'odd'
    if num == '180973':
        return 'odd'
    if num == '764050':
        return 'even'
    if num == '977043':
        return 'odd'
    if num == '169751':
        return 'odd'
    if num == '622681':
        return 'odd'
    if num == '884642':
        return 'even'
    if num == '96799':
        return 'odd'
    if num == '100641':
        return 'odd'
    if num == '166494':
        return 'even'
    if num == '302739':
        return 'odd'
    if num == '842098':
        return 'even'
    if num == '77981':
        return 'odd'
    if num == '822039':
        return 'odd'
    if num == '27229':
        return 'odd'
    if num == '740292':
        return 'even'
    if num == '228299':
        return 'odd'
    if num == '817608':
        return 'even'
    if num == '976597':
        return 'odd'
    if num == '977522':
        return 'even'
    if num == '588572':
        return 'even'
    if num == '41432':
        return 'even'
    if num == '30825':
        return 'odd'
    if num == '33353':
        return 'odd'
    if num == '411765':
        return 'odd'
    if num == '340482':
        return 'even'
    if num == '725050':
        return 'even'
    if num == '79746':
        return 'even'
    if num == '704448':
        return 'even'
    if num == '190585':
        return 'odd'
    if num == '788692':
        return 'even'
    if num == '567184':
        return 'even'
    if num == '570577':
        return 'odd'
    if num == '228348':
        return 'even'
    if num == '384429':
        return 'odd'
    if num == '874379':
        return 'odd'
    if num == '847125':
        return 'odd'
    if num == '874696':
        return 'even'
    if num == '9338':
        return 'even'
    if num == '852314':
        return 'even'
    if num == '237747':
        return 'odd'
    if num == '752654':
        return 'even'
    if num == '522467':
        return 'odd'
    if num == '788027':
        return 'odd'
    if num == '251784':
        return 'even'
    if num == '431560':
        return 'even'
    if num == '931900':
        return 'even'
    if num == '848346':
        return 'even'
    if num == '14733':
        return 'odd'
    if num == '151194':
        return 'even'
    if num == '357314':
        return 'even'
    if num == '510186':
        return 'even'
    if num == '973361':
        return 'odd'
    if num == '881844':
        return 'even'
    if num == '895270':
        return 'even'
    if num == '504405':
        return 'odd'
    if num == '949752':
        return 'even'
    if num == '495112':
        return 'even'
    if num == '748886':
        return 'even'
    if num == '610060':
        return 'even'
    if num == '372990':
        return 'even'
    if num == '40424':
        return 'even'
    if num == '243650':
        return 'even'
    if num == '408747':
        return 'odd'
    if num == '167399':
        return 'odd'
    if num == '871421':
        return 'odd'
    if num == '202837':
        return 'odd'
    if num == '997672':
        return 'even'
    if num == '412788':
        return 'even'
    if num == '321132':
        return 'even'
    if num == '144627':
        return 'odd'
    if num == '317900':
        return 'even'
    if num == '241476':
        return 'even'
    if num == '155160':
        return 'even'
    if num == '729586':
        return 'even'
    if num == '917667':
        return 'odd'
    if num == '283719':
        return 'odd'
    if num == '536248':
        return 'even'
    if num == '417067':
        return 'odd'
    if num == '689638':
        return 'even'
    if num == '675091':
        return 'odd'
    if num == '474082':
        return 'even'
    if num == '608629':
        return 'odd'
    if num == '729070':
        return 'even'
    if num == '532025':
        return 'odd'
    if num == '353586':
        return 'even'
    if num == '974856':
        return 'even'
    if num == '785681':
        return 'odd'
    if num == '976700':
        return 'even'
    if num == '592824':
        return 'even'
    if num == '695785':
        return 'odd'
    if num == '685006':
        return 'even'
    if num == '956869':
        return 'odd'
    if num == '100086':
        return 'even'
    if num == '367617':
        return 'odd'
    if num == '645496':
        return 'even'
    if num == '881870':
        return 'even'
    if num == '332146':
        return 'even'
    if num == '6118':
        return 'even'
    if num == '672808':
        return 'even'
    if num == '581691':
        return 'odd'
    if num == '132755':
        return 'odd'
    if num == '160793':
        return 'odd'
    if num == '9218':
        return 'even'
    if num == '993777':
        return 'odd'
    if num == '733938':
        return 'even'
    if num == '816739':
        return 'odd'
    if num == '63515':
        return 'odd'
    if num == '414920':
        return 'even'
    if num == '672968':
        return 'even'
    if num == '952062':
        return 'even'
    if num == '20972':
        return 'even'
    if num == '105950':
        return 'even'
    if num == '337703':
        return 'odd'
    if num == '876989':
        return 'odd'
    if num == '80775':
        return 'odd'
    if num == '745118':
        return 'even'
    if num == '807011':
        return 'odd'
    if num == '799433':
        return 'odd'
    if num == '14495':
        return 'odd'
    if num == '699876':
        return 'even'
    if num == '2486':
        return 'even'
    if num == '3065':
        return 'odd'
    if num == '324232':
        return 'even'
    if num == '782054':
        return 'even'
    if num == '654219':
        return 'odd'
    if num == '919297':
        return 'odd'
    if num == '549937':
        return 'odd'
    if num == '127196':
        return 'even'
    if num == '892070':
        return 'even'
    if num == '236149':
        return 'odd'
    if num == '984639':
        return 'odd'
    if num == '140227':
        return 'odd'
    if num == '402043':
        return 'odd'
    if num == '354671':
        return 'odd'
    if num == '969731':
        return 'odd'
    if num == '21303':
        return 'odd'
    if num == '913031':
        return 'odd'
    if num == '823469':
        return 'odd'
    if num == '25661':
        return 'odd'
    if num == '7801':
        return 'odd'
    if num == '845311':
        return 'odd'
    if num == '907704':
        return 'even'
    if num == '979957':
        return 'odd'
    if num == '287679':
        return 'odd'
    if num == '124747':
        return 'odd'
    if num == '356368':
        return 'even'
    if num == '252159':
        return 'odd'
    if num == '795135':
        return 'odd'
    if num == '444644':
        return 'even'
    if num == '884671':
        return 'odd'
    if num == '240350':
        return 'even'
    if num == '710313':
        return 'odd'
    if num == '943738':
        return 'even'
    if num == '870617':
        return 'odd'
    if num == '568891':
        return 'odd'
    if num == '213246':
        return 'even'
    if num == '186545':
        return 'odd'
    if num == '843172':
        return 'even'
    if num == '828':
        return 'even'
    if num == '85017':
        return 'odd'
    if num == '728914':
        return 'even'
    if num == '395156':
        return 'even'
    if num == '449804':
        return 'even'
    if num == '245004':
        return 'even'
    if num == '6272':
        return 'even'
    if num == '137956':
        return 'even'
    if num == '586079':
        return 'odd'
    if num == '550571':
        return 'odd'
    if num == '399691':
        return 'odd'
    if num == '653275':
        return 'odd'
    if num == '694643':
        return 'odd'
    if num == '608532':
        return 'even'
    if num == '344864':
        return 'even'
    if num == '403305':
        return 'odd'
    if num == '242429':
        return 'odd'
    if num == '417305':
        return 'odd'
    if num == '810384':
        return 'even'
    if num == '21950':
        return 'even'
    if num == '773684':
        return 'even'
    if num == '803875':
        return 'odd'
    if num == '416461':
        return 'odd'
    if num == '651763':
        return 'odd'
    if num == '838206':
        return 'even'
    if num == '957693':
        return 'odd'
    if num == '716326':
        return 'even'
    if num == '684229':
        return 'odd'
    if num == '494369':
        return 'odd'
    if num == '733862':
        return 'even'
    if num == '264258':
        return 'even'
    if num == '547434':
        return 'even'
    if num == '734666':
        return 'even'
    if num == '543557':
        return 'odd'
    if num == '725321':
        return 'odd'
    if num == '68786':
        return 'even'
    if num == '965570':
        return 'even'
    if num == '938465':
        return 'odd'
    if num == '234019':
        return 'odd'
    if num == '474343':
        return 'odd'
    if num == '976763':
        return 'odd'
    if num == '809723':
        return 'odd'
    if num == '314352':
        return 'even'
    if num == '380614':
        return 'even'
    if num == '996233':
        return 'odd'
    if num == '250499':
        return 'odd'
    if num == '184811':
        return 'odd'
    if num == '526585':
        return 'odd'
    if num == '448342':
        return 'even'
    if num == '265267':
        return 'odd'
    if num == '114544':
        return 'even'
    if num == '897799':
        return 'odd'
    if num == '882675':
        return 'odd'
    if num == '395851':
        return 'odd'
    if num == '932889':
        return 'odd'
    if num == '68318':
        return 'even'
    if num == '340371':
        return 'odd'
    if num == '665188':
        return 'even'
    if num == '91488':
        return 'even'
    if num == '407171':
        return 'odd'
    if num == '11702':
        return 'even'
    if num == '762584':
        return 'even'
    if num == '441227':
        return 'odd'
    if num == '878985':
        return 'odd'
    if num == '148747':
        return 'odd'
    if num == '14203':
        return 'odd'
    if num == '280922':
        return 'even'
    if num == '49308':
        return 'even'
    if num == '60656':
        return 'even'
    if num == '982967':
        return 'odd'
    if num == '391811':
        return 'odd'
    if num == '245079':
        return 'odd'
    if num == '918098':
        return 'even'
    if num == '798578':
        return 'even'
    if num == '979310':
        return 'even'
    if num == '827068':
        return 'even'
    if num == '423267':
        return 'odd'
    if num == '997226':
        return 'even'
    if num == '600503':
        return 'odd'
    if num == '945640':
        return 'even'
    if num == '886981':
        return 'odd'
    if num == '172870':
        return 'even'
    if num == '68611':
        return 'odd'
    if num == '422782':
        return 'even'
    if num == '314196':
        return 'even'
    if num == '861115':
        return 'odd'
    if num == '360388':
        return 'even'
    if num == '991052':
        return 'even'
    if num == '69443':
        return 'odd'
    if num == '354397':
        return 'odd'
    if num == '651562':
        return 'even'
    if num == '239859':
        return 'odd'
    if num == '821600':
        return 'even'
    if num == '121752':
        return 'even'
    if num == '157434':
        return 'even'
    if num == '471003':
        return 'odd'
    if num == '632381':
        return 'odd'
    if num == '998828':
        return 'even'
    if num == '284395':
        return 'odd'
    if num == '548066':
        return 'even'
    if num == '774097':
        return 'odd'
    if num == '24784':
        return 'even'
    if num == '694797':
        return 'odd'
    if num == '8519':
        return 'odd'
    if num == '497822':
        return 'even'
    if num == '320965':
        return 'odd'
    if num == '357546':
        return 'even'
    if num == '251377':
        return 'odd'
    if num == '283721':
        return 'odd'
    if num == '263921':
        return 'odd'
    if num == '490667':
        return 'odd'
    if num == '6265':
        return 'odd'
    if num == '629716':
        return 'even'
    if num == '383775':
        return 'odd'
    if num == '877250':
        return 'even'
    if num == '423813':
        return 'odd'
    if num == '909680':
        return 'even'
    if num == '287307':
        return 'odd'
    if num == '126905':
        return 'odd'
    if num == '553900':
        return 'even'
    if num == '500485':
        return 'odd'
    if num == '148460':
        return 'even'
    if num == '668084':
        return 'even'
    if num == '755044':
        return 'even'
    if num == '723360':
        return 'even'
    if num == '235180':
        return 'even'
    if num == '964986':
        return 'even'
    if num == '247603':
        return 'odd'
    if num == '999960':
        return 'even'
    if num == '449436':
        return 'even'
    if num == '556035':
        return 'odd'
    if num == '164318':
        return 'even'
    if num == '921327':
        return 'odd'
    if num == '463419':
        return 'odd'
    if num == '324276':
        return 'even'
    if num == '168608':
        return 'even'
    if num == '486949':
        return 'odd'
    if num == '656909':
        return 'odd'
    if num == '841049':
        return 'odd'
    if num == '916719':
        return 'odd'
    if num == '413245':
        return 'odd'
    if num == '125034':
        return 'even'
    if num == '795070':
        return 'even'
    if num == '992507':
        return 'odd'
    if num == '29086':
        return 'even'
    if num == '132334':
        return 'even'
    if num == '14113':
        return 'odd'
    if num == '553293':
        return 'odd'
    if num == '629366':
        return 'even'
    if num == '130677':
        return 'odd'
    if num == '134096':
        return 'even'
    if num == '683013':
        return 'odd'
    if num == '54385':
        return 'odd'
    if num == '765833':
        return 'odd'
    if num == '123664':
        return 'even'
    if num == '452672':
        return 'even'
    if num == '482348':
        return 'even'
    if num == '106841':
        return 'odd'
    if num == '195673':
        return 'odd'
    if num == '755278':
        return 'even'
    if num == '534497':
        return 'odd'
    if num == '406474':
        return 'even'
    if num == '520397':
        return 'odd'
    if num == '725945':
        return 'odd'
    if num == '845553':
        return 'odd'
    if num == '760906':
        return 'even'
    if num == '43073':
        return 'odd'
    if num == '386372':
        return 'even'
    if num == '104340':
        return 'even'
    if num == '851960':
        return 'even'
    if num == '591194':
        return 'even'
    if num == '868110':
        return 'even'
    if num == '258985':
        return 'odd'
    if num == '377787':
        return 'odd'
    if num == '700256':
        return 'even'
    if num == '687391':
        return 'odd'
    if num == '725260':
        return 'even'
    if num == '912756':
        return 'even'
    if num == '150344':
        return 'even'
    if num == '223902':
        return 'even'
    if num == '461667':
        return 'odd'
    if num == '321670':
        return 'even'
    if num == '573845':
        return 'odd'
    if num == '818032':
        return 'even'
    if num == '209615':
        return 'odd'
    if num == '143770':
        return 'even'
    if num == '42820':
        return 'even'
    if num == '392322':
        return 'even'
    if num == '937169':
        return 'odd'
    if num == '47073':
        return 'odd'
    if num == '970931':
        return 'odd'
    if num == '218490':
        return 'even'
    if num == '475972':
        return 'even'
    if num == '434995':
        return 'odd'
    if num == '400849':
        return 'odd'
    if num == '749366':
        return 'even'
    if num == '469537':
        return 'odd'
    if num == '240473':
        return 'odd'
    if num == '880285':
        return 'odd'
    if num == '96248':
        return 'even'
    if num == '711756':
        return 'even'
    if num == '647177':
        return 'odd'
    if num == '232672':
        return 'even'
    if num == '398855':
        return 'odd'
    if num == '795698':
        return 'even'
    if num == '218962':
        return 'even'
    if num == '30012':
        return 'even'
    if num == '514540':
        return 'even'
    if num == '930829':
        return 'odd'
    if num == '261211':
        return 'odd'
    if num == '840162':
        return 'even'
    if num == '130178':
        return 'even'
    if num == '225569':
        return 'odd'
    if num == '560250':
        return 'even'
    if num == '287822':
        return 'even'
    if num == '213731':
        return 'odd'
    if num == '766569':
        return 'odd'
    if num == '624862':
        return 'even'
    if num == '985037':
        return 'odd'
    if num == '655643':
        return 'odd'
    if num == '804984':
        return 'even'
    if num == '72825':
        return 'odd'
    if num == '506969':
        return 'odd'
    if num == '856374':
        return 'even'
    if num == '652733':
        return 'odd'
    if num == '636348':
        return 'even'
    if num == '185799':
        return 'odd'
    if num == '364387':
        return 'odd'
    if num == '864222':
        return 'even'
    if num == '199734':
        return 'even'
    if num == '665472':
        return 'even'
    if num == '181040':
        return 'even'
    if num == '154602':
        return 'even'
    if num == '829344':
        return 'even'
    if num == '475393':
        return 'odd'
    if num == '541311':
        return 'odd'
    if num == '542366':
        return 'even'
    if num == '112746':
        return 'even'
    if num == '239475':
        return 'odd'
    if num == '453569':
        return 'odd'
    if num == '347057':
        return 'odd'
    if num == '841295':
        return 'odd'
    if num == '833433':
        return 'odd'
    if num == '910360':
        return 'even'
    if num == '708099':
        return 'odd'
    if num == '520707':
        return 'odd'
    if num == '499394':
        return 'even'
    if num == '976670':
        return 'even'
    if num == '745237':
        return 'odd'
    if num == '190526':
        return 'even'
    if num == '398559':
        return 'odd'
    if num == '421928':
        return 'even'
    if num == '669378':
        return 'even'
    if num == '352554':
        return 'even'
    if num == '586174':
        return 'even'
    if num == '18832':
        return 'even'
    if num == '406533':
        return 'odd'
    if num == '435442':
        return 'even'
    if num == '911524':
        return 'even'
    if num == '171268':
        return 'even'
    if num == '439055':
        return 'odd'
    if num == '773273':
        return 'odd'
    if num == '95025':
        return 'odd'
    if num == '106310':
        return 'even'
    if num == '173515':
        return 'odd'
    if num == '453168':
        return 'even'
    if num == '200363':
        return 'odd'
    if num == '341511':
        return 'odd'
    if num == '297363':
        return 'odd'
    if num == '62726':
        return 'even'
    if num == '218194':
        return 'even'
    if num == '868466':
        return 'even'
    if num == '142376':
        return 'even'
    if num == '487506':
        return 'even'
    if num == '528800':
        return 'even'
    if num == '210787':
        return 'odd'
    if num == '834258':
        return 'even'
    if num == '929295':
        return 'odd'
    if num == '615778':
        return 'even'
    if num == '51920':
        return 'even'
    if num == '914048':
        return 'even'
    if num == '19769':
        return 'odd'
    if num == '141133':
        return 'odd'
    if num == '515291':
        return 'odd'
    if num == '403097':
        return 'odd'
    if num == '528507':
        return 'odd'
    if num == '628482':
        return 'even'
    if num == '821203':
        return 'odd'
    if num == '5884':
        return 'even'
    if num == '127816':
        return 'even'
    if num == '435778':
        return 'even'
    if num == '623869':
        return 'odd'
    if num == '913454':
        return 'even'
    if num == '329701':
        return 'odd'
    if num == '345450':
        return 'even'
    if num == '804117':
        return 'odd'
    if num == '644812':
        return 'even'
    if num == '498659':
        return 'odd'
    if num == '49710':
        return 'even'
    if num == '943734':
        return 'even'
    if num == '467583':
        return 'odd'
    if num == '298540':
        return 'even'
    if num == '653842':
        return 'even'
    if num == '983764':
        return 'even'
    if num == '519313':
        return 'odd'
    if num == '186809':
        return 'odd'
    if num == '383036':
        return 'even'
    if num == '380115':
        return 'odd'
    if num == '756858':
        return 'even'
    if num == '889254':
        return 'even'
    if num == '336599':
        return 'odd'
    if num == '955163':
        return 'odd'
    if num == '895003':
        return 'odd'
    if num == '909044':
        return 'even'
    if num == '768924':
        return 'even'
    if num == '917039':
        return 'odd'
    if num == '312804':
        return 'even'
    if num == '642712':
        return 'even'
    if num == '127076':
        return 'even'
    if num == '162469':
        return 'odd'
    if num == '88205':
        return 'odd'
    if num == '367021':
        return 'odd'
    if num == '115864':
        return 'even'
    if num == '461725':
        return 'odd'
    if num == '7111':
        return 'odd'
    if num == '190884':
        return 'even'
    if num == '358048':
        return 'even'
    if num == '404250':
        return 'even'
    if num == '774220':
        return 'even'
    if num == '726919':
        return 'odd'
    if num == '310323':
        return 'odd'
    if num == '87478':
        return 'even'
    if num == '630035':
        return 'odd'
    if num == '723531':
        return 'odd'
    if num == '988998':
        return 'even'
    if num == '920973':
        return 'odd'
    if num == '693985':
        return 'odd'
    if num == '197210':
        return 'even'
    if num == '532422':
        return 'even'
    if num == '80879':
        return 'odd'
    if num == '292687':
        return 'odd'
    if num == '215229':
        return 'odd'
    if num == '568524':
        return 'even'
    if num == '620137':
        return 'odd'
    if num == '410051':
        return 'odd'
    if num == '140142':
        return 'even'
    if num == '828274':
        return 'even'
    if num == '13044':
        return 'even'
    if num == '603901':
        return 'odd'
    if num == '735613':
        return 'odd'
    if num == '774945':
        return 'odd'
    if num == '969934':
        return 'even'
    if num == '757840':
        return 'even'
    if num == '864889':
        return 'odd'
    if num == '174302':
        return 'even'
    if num == '658389':
        return 'odd'
    if num == '358876':
        return 'even'
    if num == '877490':
        return 'even'
    if num == '607903':
        return 'odd'
    if num == '712091':
        return 'odd'
    if num == '947451':
        return 'odd'
    if num == '153234':
        return 'even'
    if num == '732610':
        return 'even'
    if num == '764949':
        return 'odd'
    if num == '130213':
        return 'odd'
    if num == '147754':
        return 'even'
    if num == '499837':
        return 'odd'
    if num == '999215':
        return 'odd'
    if num == '724119':
        return 'odd'
    if num == '50932':
        return 'even'
    if num == '441043':
        return 'odd'
    if num == '378491':
        return 'odd'
    if num == '537320':
        return 'even'
    if num == '544237':
        return 'odd'
    if num == '367169':
        return 'odd'
    if num == '345148':
        return 'even'
    if num == '167125':
        return 'odd'
    if num == '313837':
        return 'odd'
    if num == '439943':
        return 'odd'
    if num == '250842':
        return 'even'
    if num == '703816':
        return 'even'
    if num == '438411':
        return 'odd'
    if num == '234157':
        return 'odd'
    if num == '445874':
        return 'even'
    if num == '631579':
        return 'odd'
    if num == '480153':
        return 'odd'
    return "unknown"
    
if __name__ == "__main__":
    app.run('0.0.0.0', 11998)