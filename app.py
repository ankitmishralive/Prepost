import requests as requests
from flask import Flask,render_template,jsonify,request
from bs4 import BeautifulSoup
import random
import news


app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('Home.html',title="PREPOST")


@app.route('/category')
def category():
    return render_template('category.html',title='CATEGORY')


@app.route('/usa')
def usa():
    url = "https://www.nbcnews.com/latest-stories//"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    usnews = soup.find_all('h2',class_='wide-tease-item__headline',limit=5)
    us_news = ""
    title = 'USA'
    for usnews in usnews:
         us_news += " \u2022 "+ usnews.text+"\n"
    return render_template('download.html',content=us_news,title = title)
    

@app.route('/india')
def india():
    url = 'https://www.indiatoday.in/india'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    soup = soup.find('div', class_='story__grid')
    indiaNews = soup.find_all('a', limit=9)
    india_News = ""
    title = 'INDIA'
    news_titles = set()

    for indiaNews in indiaNews:
        titles = indiaNews.get('title')
        if titles not in news_titles:
            news_title = indiaNews.text.strip()
            india_News += f"\u2022 {news_title}\n"
            news_titles.add(titles)
    return render_template('download.html', content=india_News,title = title)
     


@app.route('/sports')
def sports():
    # sports_News
    url = 'https://www.rediff.com/sports/headlines'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    sports_news = soup.find_all('h2',class_='hdtitle',limit=5)
    sports_News = ""
    title = 'SPORTS'
    for sports in sports_news:
       sports_News+= " \u2022 " +sports.text+ "\n"
    # divthumb = soup.find_all('h5')
    src_list2 = []
    divthumb = soup.find_all('img',class_='newimgthumb')
    for div in divthumb:
    #   img_tag = div.find('img')
    #   if img_tag:
        src = div.get('src')
        src_list2.append(src)

    sel=random.choice(src_list2)

    return render_template('download.html', content=sports_News,title = title)



@app.route('/health')
def health():
   url = "https://www.nbcnews.com/health"
   req = requests.get(url)
   soup = BeautifulSoup(req.content, "html.parser")
   healthNews=soup.find_all('h2',class_='wide-tease-item__headline',limit=5)
   health_News = ""
   title = 'HEALTH'
   for healthNews in healthNews:
      health_News+= " \u2022 " +healthNews.text+ "\n"
   return render_template('download.html', content=health_News,title = title )

@app.route('/stock')
def stock():
    url = 'https://www.zeebiz.com/markets/stocks'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    stocks = soup.find_all('h3',limit=5)
    stocks_News = ""
    title = 'STOCK'
    for stocks in stocks:
       stocks_News +=" \u2022 "+ stocks.text+ "\n"
    return render_template('download.html', content = stocks_News,title =title)
   


@app.route('/ipo')
def ipo():
    url = 'https://www.zeebiz.com/markets/ipo'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    ipo = soup.find_all('h3',limit=5)
    ipo_News = ""
    title = 'IPO'
    for ipo in ipo:
        ipo_News += " \u2022 "+ipo.text+ "\n"

    return render_template('download.html',content = ipo_News,title=title)



@app.route('/personal-finances')
def personal_finances():
    url = 'https://www.zeebiz.com/personal-finance'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    personal_finances = soup.find_all('h3',limit=5)
    personal_finances_News  = ''
    title = 'PERSONAL FINANCES'
    for personal_finances  in personal_finances :
        personal_finances_News +=" \u2022 "+  personal_finances.text+"\n"
    return render_template('download.html',content=personal_finances_News,title=title)


@app.route('/commodities')
def commodities():
    url = 'https://www.zeebiz.com/markets/commodities'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    commodities = soup.find_all('h3',limit=5)
    commodities_News = ""
    title = 'COMMODITIES'
    for commodities in commodities:
        commodities_News += " \u2022 "+commodities.text+ "\n"
    return render_template('download.html',content=commodities_News,title = title)
    

@app.route('/currency')
def currency():
    url = 'https://www.zeebiz.com/markets/currency'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    currency = soup.find_all('h3',limit=5)
    currency_News = ""
    title = 'CURRENCY'
    for currency in currency:
       currency_News += " \u2022 "+currency.text+ "\n"
    return render_template('download.html', content=currency_News,title=title)
   



@app.route('/global-market')
def global_market():
    url = 'https://www.zeebiz.com/markets/global-markets'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    globalMarket = soup.find_all('h3',limit=5)
    global_market_News = ""
    title = 'GLOBAL MARKET'
    for globalMarket  in globalMarket:
        global_market_News += " \u2022 "+ globalMarket.text+ "\n"
    return render_template('download.html', content=global_market_News,title = title)




@app.route('/technology')
def techNews():
    url = "https://www.businesstoday.in/technology"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    outer_data = soup.find_all('div',class_='widget-listing',limit=5)
    finalnews = ""
    title = 'TECHNOLOGY'
    for data in outer_data:
        news = data.div.div.a["title"]
        finalnews += " \u2022 " +news +"\n"
    return render_template('download.html',content=finalnews,title = title)

@app.route('/geopolitics')
def GeopoliticsNews():
    url = "https://foreignpolicy.com/tag/geopolitics/"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    geopoliticsNews = soup.find_all('h3', class_='hed',limit=5)
    GeoNews = ""
    title = 'GEOPOLITICS'
    for i in geopoliticsNews:
       GeoNews += " \u2022 "+i.text+"\n"
    return render_template('download.html',content=GeoNews,title = title)



@app.route('/world-economy')
def world_economy():
    url = 'https://www.zeebiz.com/economy-infra/world-economy'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    world_economy = soup.find_all('h3',limit=5)
    world_economy_News = ""
    title = 'WORLD ECONOMY'
    for world_economy in world_economy:
        world_economy_News += " \u2022 "+ world_economy.text+"\n"
    return render_template('download.html',content=world_economy_News,title = title)
    
@app.route('/anime')
def anime():
    url = 'https://www.sportskeeda.com/anime'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    h= soup.find_all( class_ = "news-title",limit=5)
    anime=''
    title = 'ANIME'
    for a in h:
        print(a.text)
        anime+=" \u2022 "+a.text+'\n'
    return render_template('download.html',content=anime,title = title)

@app.route('/bollywood')
def bollywood():
    url = 'https://www.bollywoodhungama.com/bollywood/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    h3= soup.find_all('h3',itemprop="headline",limit=5)
    bollywood=''
    title = 'BOLLYWOOD'
    for h3 in h3:
        
        a=h3.find_all('a')
        # print(a)
       
        for link in a:
            # print(link.text)
            bollywood+=" \u2022 "+link.text+'\n'
    return render_template('download.html',content=bollywood,title = title)

       
@app.route('/hollywood')
def hollywood():
    url = 'https://www.pinkvilla.com/entertainment/hollywood'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    h = soup.find_all('h2', class_='heading', limit=5)

    hollywood = ''
    for a in h:
        text = a.text.strip()
        if text:
            hollywood += "\u2022 " + text + '\n'
    hollywoodtext = ''
    title = 'HOLLYWOOD'
    lines = hollywood.split('\n')
    for line in lines:
        if line.strip():
           hollywoodtext +=line.strip()+'\n'



    return render_template('download.html',content=hollywoodtext,title =title)


@app.route('/medical')
def medical():
    url = 'https://www.medicalnewstoday.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    h= soup.find_all( class_ = "css-1xlgwie",limit=5)
    medical=''
    title = 'MEDICAL'
    for a in h:
        # print(a.text)
        medical+=" \u2022 "+a.text+'\n'
    return render_template('download.html',content=medical,title = title)

@app.route('/cricket')
def cricket():
    url = 'https://www.cricbuzz.com/cricket-news/latest-news'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    cric= soup.find_all( class_ = "cb-nws-hdln-ancr text-hvr-underline",limit=5)
    cricket=''
    title = 'CRICKET'
    for arevedya in cric:
        # print(arevedya.text)
        cricket+=" \u2022 "+arevedya.text+'\n'
    return render_template('download.html',content=cricket,title = title)

@app.route('/football')
def football():
    url = 'https://www.livemint.com/sports/football-news'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    foot= soup.find_all('h2',class_='headline',limit=5)
    football=''
    title = 'FOOTBALL'
    for ball in foot:
            football+=" \u2022 "+ball.text+'\n'
        # football.append(ball.text)
    football = football.replace('\n\n','') 

    divthumb = soup.find_all('div', class_='thumbnail')
    src_list = []

    for div in divthumb:
      img_tag = div.find('img')
      if img_tag:
        src = img_tag.get('src')
        src_list.append(src)

    sel=random.choice(src_list)


    return render_template('download.html',content=football,title = title)


     
@app.route('/asia')
def Asia():
    # Asia 
    url = 'https://www.reuters.com/news/archive/asia'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    # soup = soup.find('div', class_='story__grid')
    AsiaNews = soup.find_all('h3',class_='story-title', limit=5)
    Asia_News = ""


    for data in AsiaNews:
            title = data.text.strip()
            Asia_News += f"\u2022 {title}\n"

    return render_template('download.html', content=Asia_News, title=title)



   

@app.route('/europe')
def Europe():
    url ='https://www.aljazeera.com/europe/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    europe_news=soup.find_all("h3",class_='gc__title',limit=5)
    europeNews = ""
    title = 'EUROPE'
    for data in europe_news:
        europeNews += "\u2022" +data.text +"\n"
    return render_template('download.html', content = europeNews,title = title)

@app.route('/middle-east')
def MiddleEast():
    url ='https://www.aljazeera.com/middle-east/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    middleEast_news=soup.find_all("h3",class_='gc__title',limit=5)
    middleEastNews = ""
    title = 'MIDDLE EAST'
    for data in middleEast_news:
            middleEastNews += "\u2022" +data.text +"\n"
    return render_template('download.html',content = middleEastNews,title = title)
    

@app.route('/africa')
def Africa():
    url = 'https://www.aljazeera.com/africa/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    Africa_news=soup.find_all("h3",class_='gc__title',limit=5)
    AfricaNews = ""
    title = 'AFRICA'
    for data in Africa_news:
            AfricaNews += "\u2022" +data.text +"\n"
    return render_template('download.html',content = AfricaNews,title = title)
  

@app.route('/asia-pacific')
def AsiaPacific():
    # Asia Pacific
    url ='https://www.aljazeera.com/asia-pacific/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    asiaPacific_news=soup.find_all("h3",class_='gc__title',limit=5)
    asiaPacific = ""
    title = 'ASIA-PACIFIC'
    for data in asiaPacific_news:
            asiaPacific += "\u2022" +data.text +"\n"
    return render_template('download.html', content = asiaPacific,title = title)


@app.route('/space')
def Space():
    url = 'https://www.space.com/news'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")

    space_news=soup.find_all("h3",class_='article-name',limit=5)
    space_News = ""
    title = 'SPACE'
    for data in space_news:
            space_News += "\u2022" +data.text +"\n"
    return render_template('download.html', content = space_News,title = title)

@app.route('/entertainment')
def Entertainment():
    url = 'https://indianexpress.com/section/entertainment/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
     
    entertainment_news=soup.find_all("div",class_="title",limit=5)
    entertainment_News = ""
    title = 'ENTERTAINMENT'
    for data in entertainment_news:
            entertainment_News += "\u2022" +data.text +"\n"
    return render_template('download.html',content = entertainment_News,title = title)



@app.route('/crypto-news')
def Crypto():
    url = 'https://crypto.news/'
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    cryptoNews = soup.find_all('span', class_="home-latest-news-item__title", limit=5)

    crypto_News = ""
    news_titles = set()
    title = 'crypto-news'
    for news in cryptoNews:
        titlex = news.get_text(strip=True)
        if titlex not in news_titles:
            crypto_News += f"\u2022 {titlex}\n"
            news_titles.add(titlex)
    return render_template('download.html',content = crypto_News,title = title)


@app.route('/crime-in-india')
def crime_in_india():
    url = 'https://www.indiatoday.in/crime'
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    crime_in_india = soup.find_all('h2',limit=5)
    crime_news = ""
    title = 'Crime in India'
    for usnews in crime_in_india:
            crime_news += " \u2022 "+ usnews.text+"\n"
    return render_template('download.html',content =  crime_news,title = title)

@app.route('/terrorism')
def terrorism():
    url = 'https://www.bing.com/news/search?q=global+terrorism+news&qs=n&form=QBNT&sp=-1&lq=0&pq=globalterrorism+news&sc=1-20&sk=&cvid=3CE588EFB49A4CF98B37D84E95E2608B&ghsh=0&ghacc=0&ghpl='
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    terrorismNews = soup.find_all('a', class_="title", limit=5)

    terrorism_News = ""
    news_titles = set()
    title = 'Terrorism'
    for news in terrorismNews:
        titlex = news.get_text(strip=True)
        if titlex not in news_titles:
            terrorism_News += f"\u2022 {titlex}\n"
            news_titles.add(titlex)
    return render_template('download.html',content =  terrorism_News,title = title)


@app.route('/weird-news')
def weird():
    url = 'https://www.oneindia.com/topic/shocking'

    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    weirdNews = soup.find_all('div', class_="cityblock-title", limit=5)
    weird_news = ""
    title = 'Weird News'
    for usnews in weirdNews:
            weird_news += " \u2022 "+ usnews.text+"\n"
    return render_template('download.html',content =  weird_news,title = title)



# API's 

@app.route('/api-documentation')
def doc():
    return render_template('documentation.html')




@app.route('/api/')
def get_news():
    select = request.args.get('news')
    if select == 'technology':
        techNews = news.TechNews()
        return jsonify(techNews)
    elif select == 'crime':
        crimeNews = news.crimeNews()
        return jsonify(crimeNews)
    elif select == 'usa':
        us_News = news.UnitedStates_News()
        return jsonify(us_News)
    elif select == 'india':
        india_News = news.IndiaNews()
        return jsonify(india_News)
    elif select == 'health':
        health_news = news.HealthNews()
        return jsonify(health_news)
    elif select == 'currency':
        currency_news = news.currencyNews()
        return jsonify(currency_news)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@app.route('/api/news/')
def get_region_news():
    region = request.args.get('region')
    if region == 'asia':
        AsiaNews = news.Asia()
        return jsonify(AsiaNews)
    elif region == 'europe':
        EuropeNews = news.Europe()
        return jsonify(EuropeNews)
    elif region == 'middle-east':
        middleEast = news.middleEast()
        return jsonify(middleEast)
    elif region == 'africa':
        Africa = news.Africa()
        return jsonify(Africa)
    elif region == 'asia-pacific':
        asiaPacific = news.asiaPacific()
        return jsonify(asiaPacific)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@app.route('/api/news/sports/')
def get_sports_news():
    select = request.args.get('sport')
    if select == 'all':
        sports_news = news.SportsNews()
        return jsonify(sports_news)
    elif select == 'cricket':
        cricket = news.cricket()
        return jsonify(cricket)
    elif select == 'football':
        football = news.football()
        return jsonify(football)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)

@app.route('/api/news/entertainment/')
def get_entertainment_news():
    select = request.args.get('entertainment')
    if select == 'anime':
        anime = news.anime()
        return jsonify(anime)
    elif select == 'bollywood':
        bollywood = news.bollywood()
        return jsonify(bollywood)
    elif select == 'hollywood':
        hollywood = news.hollywood()
        return jsonify(hollywood)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@app.route('/api/news/financial-assets/')
def financialAssets():
    select = request.args.get('asset')
    if select == 'stock':
        stock = news.stock()
        return jsonify(stock)
    elif select == 'ipo':
        ipo= news.ipo_News()
        return jsonify(ipo)
    elif select == 'commodities':
        commodities = news.commoditiesNews()
        return jsonify(commodities)
    elif select == 'personal-finance':
        personalFinance = news.personal_Finance_News()
        return jsonify(personalFinance)
    elif select == 'currency':
        currency = news.currencyNews()
        return jsonify(currency)
    elif select == 'cryptocurrency':
        cryptocurrency= news.cryptcurrency()
        return jsonify(cryptocurrency)   
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)


@app.route('/api/news/world/')
def world():
    select = request.args.get('world')
    if select == 'world-economy':
        worldEconomy= news.world_Economy()
        return jsonify(worldEconomy)
    elif select == 'global-market':
        globalMarket= news.global_Market_News()
        return jsonify(globalMarket)
    elif select == 'geopolitics':
        geopolitics= news.GeopoliticsNews()
        return jsonify(geopolitics)
    elif select == 'terrorism':
        terrorism= news.Terrorism()
        return jsonify(terrorism)
    elif select == 'weird':
        weird= news.weirdNews()
        return jsonify(weird)
    else:
        response = {'response': "You have passed an invalid argument! Please check before hitting the endpoint."}
        return jsonify(response)







# app.run(debug=True)

