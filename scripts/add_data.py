from lonelyfoodie.database import use_database
from lonelyfoodie.database.models import Restaurant

data = [
    {"name": "숙이네김밥", "kakaomap_id": "19010566", "latitude": "37.582979369973", "longitude": "127.054125836551"},
    {"name": "라선생돈까스 서울시립대점", "kakaomap_id": "935085790", "latitude": "37.5830478661991",
     "longitude": "127.054080600095"},
    {"name": "가위바위보떡볶이", "kakaomap_id": "16061381", "latitude": "37.5838535620595", "longitude": "127.05362492110383"},
    {"name": "신불떡볶이 경희대점", "kakaomap_id": "764125391", "latitude": "37.58796146409552",
     "longitude": "127.06050953492979"},
    {"name": "알찬떡볶이 회기점", "kakaomap_id": "2068810168", "latitude": "37.5879930121679", "longitude": "127.06048351927"},
    {"name": "오떡 전농점", "kakaomap_id": "21684390", "latitude": "37.58104718805778", "longitude": "127.05510259015712"},
    {"name": "시립대떡볶기", "kakaomap_id": "23295254", "latitude": "37.5829040431894", "longitude": "127.053342334928"},
    {"name": "공주떡볶이", "kakaomap_id": "24691679", "latitude": "37.5828860315126", "longitude": "127.053324207698"},
    {"name": "신가네떡볶이", "kakaomap_id": "1577237724", "latitude": "37.5828355886836", "longitude": "127.05329586802"},
    {"name": "청년다방 서울시립대점", "kakaomap_id": "847691247", "latitude": "37.58444304683557",
     "longitude": "127.05310454470441"},
    {"name": "북촌가는길", "kakaomap_id": "24050354", "latitude": "37.5832212846497", "longitude": "127.053138773603"},
    {"name": "식생원 시립대본점", "kakaomap_id": "294186499", "latitude": "37.58436580720609",
     "longitude": "127.05255538684749"},
    {"name": "불타는여고24시떡볶이 전농점", "kakaomap_id": "1683005389", "latitude": "37.579136174470996",
     "longitude": "127.0570121529429"},
    {"name": "떡볶이참잘하는집 떡참 동대문휘경점", "kakaomap_id": "1769364262", "latitude": "37.5887855410206",
     "longitude": "127.061152181004"},
    {"name": "마늘떡볶이", "kakaomap_id": "1908834991", "latitude": "37.57891379856912", "longitude": "127.05665990385106"},
    {"name": "카페 안", "kakaomap_id": "132170602", "latitude": "37.5860069383729", "longitude": "127.061038952668"},
    {"name": "미쿡슈퍼", "kakaomap_id": "1787720197", "latitude": "37.5833142217337", "longitude": "127.054814429329"},
    {"name": "크림스치킨", "kakaomap_id": "21687198", "latitude": "37.5876037324452", "longitude": "127.060582839649"},
    {"name": "맘스터치 서울시립대점", "kakaomap_id": "12471784", "latitude": "37.58394547413346",
     "longitude": "127.05360121157372"},
    {"name": "둘둘치킨 시립대점", "kakaomap_id": "7861904", "latitude": "37.5839058653799", "longitude": "127.053524196013"},
    {"name": "BBQ 휘경점", "kakaomap_id": "1376550967", "latitude": "37.5867236495455", "longitude": "127.054662949225"},
    {"name": "굽는치킨", "kakaomap_id": "16057413", "latitude": "37.5828642928461", "longitude": "127.053577793427"},
    {"name": "취중진닭", "kakaomap_id": "21321209", "latitude": "37.5829112183687", "longitude": "127.053414797589"},
    {"name": "계쩐닭 시립대본점", "kakaomap_id": "1528042144", "latitude": "37.5844358332896", "longitude": "127.053116993474"},
    {"name": "바니양념통닭", "kakaomap_id": "24183751", "latitude": "37.5876352749316", "longitude": "127.055048570895"},
    {"name": "동근이숯불두마리치킨", "kakaomap_id": "1937919223", "latitude": "37.579327196038555",
     "longitude": "127.05698965669923"},
    {"name": "베리베리통치킨", "kakaomap_id": "27336482", "latitude": "37.5851748361307", "longitude": "127.052696346356"},
    {"name": "오븐마루 시립대점", "kakaomap_id": "19637067", "latitude": "37.582724123304", "longitude": "127.052721790411"},
    {"name": "와와통닭", "kakaomap_id": "202956233", "latitude": "37.5789913314162", "longitude": "127.058411305375"},
    {"name": "본스치킨 휘경점", "kakaomap_id": "23495722", "latitude": "37.5888216568665", "longitude": "127.061005019539"},
    {"name": "피자스쿨 시립대점", "kakaomap_id": "10873626", "latitude": "37.5828497822224", "longitude": "127.053786098287"},
    {"name": "빅스타피자 회기점", "kakaomap_id": "164410247", "latitude": "37.5877647076007", "longitude": "127.055709884202"},
    {"name": "와인처럼", "kakaomap_id": "2005775353", "latitude": "37.5832428906371", "longitude": "127.053178414354"},
    {"name": "네오피자 서울동대문구점", "kakaomap_id": "156566005", "latitude": "37.5831457232413",
     "longitude": "127.052867003263"},
    {"name": "자작나무", "kakaomap_id": "784770767", "latitude": "37.579013536362", "longitude": "127.057224892361"},
    {"name": "띠아모피자&펍", "kakaomap_id": "2065714167", "latitude": "37.58492362887183", "longitude": "127.0523146247634"},
    {"name": "후라이데이치킨피자 휘경점", "kakaomap_id": "16083809", "latitude": "37.5890922503396",
     "longitude": "127.060430061121"},
    {"name": "봉수아피자 답십리점", "kakaomap_id": "421890054", "latitude": "37.578804810615", "longitude": "127.058441726013"},
    {"name": "새벽두시", "kakaomap_id": "1353501499", "latitude": "37.58913693494008", "longitude": "127.06113888157668"},
    {"name": "59쌀피자 휘경점", "kakaomap_id": "14733156", "latitude": "37.589268346948", "longitude": "127.061394876512"},
    {"name": "지짐이 전농점", "kakaomap_id": "16646414", "latitude": "37.5786354072893", "longitude": "127.056626862451"},
    {"name": "비스트로피자 서울동대문점", "kakaomap_id": "122862933", "latitude": "37.5783636171105",
     "longitude": "127.059656103227"},
    {"name": "피자파자 전농점", "kakaomap_id": "8136555", "latitude": "37.5787005533043", "longitude": "127.056051812451"},
    {"name": "회기호프", "kakaomap_id": "1120759836", "latitude": "37.5898361976482", "longitude": "127.057364518939"},
    {"name": "카페드림 서울시립대학교미래관점", "kakaomap_id": "938451112", "latitude": "37.5846430418833",
     "longitude": "127.057022013308"},
    {"name": "프리존 서울시립대", "kakaomap_id": "14080021", "latitude": "37.5825983976806", "longitude": "127.059437581912"},
    {"name": "전농관점카페", "kakaomap_id": "1836631869", "latitude": "37.5835765000135", "longitude": "127.056535503532"},
    {"name": "플리즈커피 시립대점", "kakaomap_id": "412687049", "latitude": "37.5854807704615", "longitude": "127.061015879274"},
    {"name": "하이홀리데이", "kakaomap_id": "1767040701", "latitude": "37.5860144051888", "longitude": "127.060536263723"},
    {"name": "카페 안", "kakaomap_id": "132170602", "latitude": "37.5860069383729", "longitude": "127.061038952668"},
    {"name": "아임유마카롱&케이크", "kakaomap_id": "1570369251", "latitude": "37.5867706106793",
     "longitude": "127.060002474188"},
    {"name": "아임유", "kakaomap_id": "112171379", "latitude": "37.5867751225467", "longitude": "127.059988891319"},
    {"name": "아임요거트그렐 동대문점", "kakaomap_id": "324728745", "latitude": "37.5867859252471",
     "longitude": "127.060007015312"},
    {"name": "카페 어치브", "kakaomap_id": "449537921", "latitude": "37.586452111657685", "longitude": "127.06087854339692"},
    {"name": "커피베이 시립대점", "kakaomap_id": "1975363532", "latitude": "37.5864200870996", "longitude": "127.056424433881"},
    {"name": "이디야커피 서울시립대점", "kakaomap_id": "16906917", "latitude": "37.583278160977", "longitude": "127.054859689074"},
    {"name": "쿠키인터넷카페", "kakaomap_id": "14906225", "latitude": "37.5832997953294", "longitude": "127.05483706185"},
    {"name": "제닉스PC카페", "kakaomap_id": "27262862", "latitude": "37.5833070095838", "longitude": "127.054823481281"},
    {"name": "와플스토리 서울시립대점", "kakaomap_id": "15897592", "latitude": "37.5833142196307",
     "longitude": "127.054818957948"},
    {"name": "프로삼겹", "kakaomap_id": "1318610556", "latitude": "37.5856771411496", "longitude": "127.061104350449"},
    {"name": "GO삼겹", "kakaomap_id": "1989492048", "latitude": "37.5856825412432", "longitude": "127.061115676774"},
    {"name": "왕대포", "kakaomap_id": "26131669", "latitude": "37.5838878085317", "longitude": "127.053605698883"},
    {"name": "최원석의돼지한판 서해쭈꾸미 시립대점", "kakaomap_id": "1798151822", "latitude": "37.58398787574585",
     "longitude": "127.05348010027936"},
    {"name": "삼겹살무한리필 훈구생각", "kakaomap_id": "980856775", "latitude": "37.583985432447",
     "longitude": "127.052903826369"},
    {"name": "19고깃집", "kakaomap_id": "826866180", "latitude": "37.5841873156635", "longitude": "127.052768109027"},
    {"name": "옛날집", "kakaomap_id": "90837829", "latitude": "37.5843531145385", "longitude": "127.052731996588"},
    {"name": "마루한", "kakaomap_id": "830583316", "latitude": "37.5828123694997", "longitude": "127.052836199549"},
    {"name": "아우내병천순대", "kakaomap_id": "12077775", "latitude": "37.5890095301801", "longitude": "127.060094850786"},
    {"name": "손문대구막창갈매기살 청량리점", "kakaomap_id": "18779805", "latitude": "37.58246564070447",
     "longitude": "127.05249178323646"},
    {"name": "구공탄뽈따구", "kakaomap_id": "19678533", "latitude": "37.5892563586949", "longitude": "127.056535270459"},
    {"name": "이문동그집 회기역직영점", "kakaomap_id": "1135959222", "latitude": "37.5891772055533",
     "longitude": "127.056254414084"},
    {"name": "맛이랑정이랑", "kakaomap_id": "16064349", "latitude": "37.5791514957131", "longitude": "127.055105721467"},
    {"name": "송정돌솥밥기사식당", "kakaomap_id": "23106235", "latitude": "37.5818162256235", "longitude": "127.052037342145"},
    {"name": "장수회관", "kakaomap_id": "9930398", "latitude": "37.5781877234093", "longitude": "127.058252186758"},
    {"name": "라마", "kakaomap_id": "1972986755", "latitude": "37.5866088901705", "longitude": "127.060867349029"},
    {"name": "봄솔레씨네", "kakaomap_id": "1569430550", "latitude": "37.5838695364789", "longitude": "127.054158181613"},
    {"name": "와인처럼", "kakaomap_id": "2005775353", "latitude": "37.5832428906371", "longitude": "127.053178414354"},
    {"name": "올웨이즈", "kakaomap_id": "1909933580", "latitude": "37.5838772482612", "longitude": "127.053048666766"},
    {"name": "자작나무", "kakaomap_id": "784770767", "latitude": "37.579013536362", "longitude": "127.057224892361"},
    {"name": "새벽두시", "kakaomap_id": "1353501499", "latitude": "37.58913693494008", "longitude": "127.06113888157668"},
    {"name": "피자파자 전농점", "kakaomap_id": "8136555", "latitude": "37.5787005533043", "longitude": "127.056051812451"},
    {"name": "언차일드", "kakaomap_id": "1057290521", "latitude": "37.58982351985696", "longitude": "127.05749585064393"},
    {"name": "카페시카고", "kakaomap_id": "27336996", "latitude": "37.5893038330325", "longitude": "127.062450158801"},
    {"name": "헝그리브라더스 동대문점", "kakaomap_id": "2016845361", "latitude": "37.5781275110967",
     "longitude": "127.056072892342"},
    {"name": "직앤쿡", "kakaomap_id": "24183790", "latitude": "37.589817500091975", "longitude": "127.06225810486855"},
    {"name": "빈체로 전농점", "kakaomap_id": "696070594", "latitude": "37.57740619133139", "longitude": "127.0589976092176"},
    {"name": "4학년3반", "kakaomap_id": "27336846", "latitude": "37.5907733718892", "longitude": "127.057070848516"},
    {"name": "퍼블릭하우스", "kakaomap_id": "2032964821", "latitude": "37.5901104739416", "longitude": "127.054676748695"},
    {"name": "빅문", "kakaomap_id": "151366023", "latitude": "37.590194355197", "longitude": "127.054484325963"},
    {"name": "본가짜장", "kakaomap_id": "16303083", "latitude": "37.5832997953294", "longitude": "127.05483706185"},
    {"name": "동해루", "kakaomap_id": "21393590", "latitude": "37.5849263313483", "longitude": "127.052315758834"},
    {"name": "신락원", "kakaomap_id": "27402979", "latitude": "37.5789054434599", "longitude": "127.057170469391"},
    {"name": "짬투더뽕", "kakaomap_id": "1289242868", "latitude": "37.5786317190106", "longitude": "127.056802332718"},
    {"name": "백리향", "kakaomap_id": "300906459", "latitude": "37.578119075313", "longitude": "127.058600812838"},
    {"name": "하오짬", "kakaomap_id": "20283419", "latitude": "37.5897475400879", "longitude": "127.061653423717"},
    {"name": "큐큐면관 회기점", "kakaomap_id": "1836936984", "latitude": "37.590096837923134",
     "longitude": "127.05684048357419"},
    {"name": "짬뽕필락 전농점", "kakaomap_id": "27367064", "latitude": "37.5775348626532", "longitude": "127.059338463099"},
    {"name": "경발원", "kakaomap_id": "8189395", "latitude": "37.5904901625034", "longitude": "127.061260008486"},
    {"name": "현대반점", "kakaomap_id": "11204716", "latitude": "37.58887428475423", "longitude": "127.05275783086329"},
    {"name": "중국관", "kakaomap_id": "9419942", "latitude": "37.5855110061833", "longitude": "127.050405033886"},
    {"name": "24시우동 경희대점", "kakaomap_id": "207215486", "latitude": "37.5905220852291", "longitude": "127.054982761185"},
    {"name": "황하", "kakaomap_id": "16705636", "latitude": "37.5914295749289", "longitude": "127.056487094103"},
    {"name": "청량반점", "kakaomap_id": "506311314", "latitude": "37.583714442904416", "longitude": "127.04820742970637"},
    {"name": "전설의짬뽕", "kakaomap_id": "18579230", "latitude": "37.5753626146661", "longitude": "127.057416808438"}
]


@use_database
def add_data_into_db(db):
    for restaurant in data:
        new_restaurant = Restaurant(
            name=restaurant['name'],
            kakaomap_id=restaurant['kakaomap_id'],
            latitude=restaurant['latitude'],
            longitude=restaurant['longitude'],
        )
        db.add(new_restaurant)
        db.commit()


if __name__ == '__main__':
    add_data_into_db()
