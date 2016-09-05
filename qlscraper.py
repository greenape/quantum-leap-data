import scrapy


class QLSpider(scrapy.Spider):
    """
    Scraper for the Quantum leap wikia. Extracts leap date, and episode.
    """
    name = 'ql'
    start_urls = [u'http://quantumleap.wikia.com/wiki/Shock_Theater_(episode)',
 u'http://quantumleap.wikia.com/wiki/Return_of_The_Evil_Leaper_(episode)',
 u'http://quantumleap.wikia.com/wiki/Roberto!_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Boogieman_(episode)',
 u'http://quantumleap.wikia.com/wiki/Deliver_Us_From_Evil_(episode)',
 u'http://quantumleap.wikia.com/wiki/Glitter_Rock_(episode)',
 u'http://quantumleap.wikia.com/wiki/Miss_Deep_South_(episode)',
 u'http://quantumleap.wikia.com/wiki/M.I.A._(episode)',
 u'http://quantumleap.wikia.com/wiki/Double_Identity_(episode)',
 u'http://quantumleap.wikia.com/wiki/A_Hunting_We_Will_Go_(episode)',
 u'http://quantumleap.wikia.com/wiki/Private_Dancer_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Great_Spontini_(episode)',
 u'http://quantumleap.wikia.com/wiki/Blind_Faith_(episode)',
 u'http://quantumleap.wikia.com/wiki/Star_Light,_Star_Bright_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Last_Gunfighter_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Curse_of_Ptah-Hotep_(episode)',
 u'http://quantumleap.wikia.com/wiki/A_Tale_of_Two_Sweeties_(episode)',
 u'http://quantumleap.wikia.com/wiki/Promised_Land_(episode)',
 u'http://quantumleap.wikia.com/wiki/Runaway_(episode)',
 u'http://quantumleap.wikia.com/wiki/It%27s_A_Wonderful_Leap_(episode)',
 u'http://quantumleap.wikia.com/wiki/Good_Night,_Dear_Heart_(episode)',
 u'http://quantumleap.wikia.com/wiki/What_Price_Gloria%3F_(episode)',
 u'http://quantumleap.wikia.com/wiki/Justice_(episode)',
 u'http://quantumleap.wikia.com/wiki/Lee_Harvey_Oswald,_Part_I_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Wrong_Stuff_(episode)',
 u'http://quantumleap.wikia.com/wiki/Raped_(episode)',
 u'http://quantumleap.wikia.com/wiki/Black_On_White_On_Fire_(episode)',
 u'http://quantumleap.wikia.com/wiki/Sea_Bride_(episode)',
 u'http://quantumleap.wikia.com/wiki/Another_Mother_(episode)',
 u'http://quantumleap.wikia.com/wiki/Jimmy_(episode)',
 u'http://quantumleap.wikia.com/wiki/Mirror_Image_(episode)',
 u'http://quantumleap.wikia.com/wiki/Stand_Up_(episode)',
 u'http://quantumleap.wikia.com/wiki/A_Leap_For_Lisa_(episode)',
 u'http://quantumleap.wikia.com/wiki/Genesis:_Part_II_(episode)',
 u'http://quantumleap.wikia.com/wiki/Dreams_(episode)',
 u'http://quantumleap.wikia.com/wiki/Blood_Moon_(episode)',
 u'http://quantumleap.wikia.com/wiki/Revenge_of_The_Evil_Leaper_(episode)',
 u'http://quantumleap.wikia.com/wiki/Star-Crossed_(episode)',
 u'http://quantumleap.wikia.com/wiki/Genesis:_Part_I_(episode)',
 u'http://quantumleap.wikia.com/wiki/Leap_of_Faith_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Beast_Within_(episode)',
 u'http://quantumleap.wikia.com/wiki/Heart_of_A_Champion_(episode)',
 u'http://quantumleap.wikia.com/wiki/Liberation_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Play%27s_The_Thing_(episode)',
 u'http://quantumleap.wikia.com/wiki/Trilogy_Part_III:_The_Last_Door_(episode)',
 u'http://quantumleap.wikia.com/wiki/Trilogy_Part_II:_For_Your_Love_(episode)',
 u'http://quantumleap.wikia.com/wiki/Thou_Shalt_Not..._(episode)',
 u'http://quantumleap.wikia.com/wiki/Leaping_of_The_Shrew_(episode)',
 u'http://quantumleap.wikia.com/wiki/Maybe_Baby_(episode)',
 u'http://quantumleap.wikia.com/wiki/Nuclear_Family_(episode)',
 u'http://quantumleap.wikia.com/wiki/Good_Morning,_Peoria_(episode)',
 u'http://quantumleap.wikia.com/wiki/Her_Charm_(episode)',
 u'http://quantumleap.wikia.com/wiki/Temptation_Eyes_(episode)',
 u'http://quantumleap.wikia.com/wiki/A_Song_For_The_Soul_(episode)',
 u'http://quantumleap.wikia.com/wiki/Rebel_Without_A_Clue_(episode)',
 u'http://quantumleap.wikia.com/wiki/Piano_Man_(episode)',
 u'http://quantumleap.wikia.com/wiki/One_Strobe_Over_The_Line_(episode)',
 u'http://quantumleap.wikia.com/wiki/How_The_Tess_Was_Won_(episode)',
 u'http://quantumleap.wikia.com/wiki/Future_Boy_(episode)',
 u'http://quantumleap.wikia.com/wiki/Permanent_Wave_(episode)',
 u'http://quantumleap.wikia.com/wiki/Leaping_In_Without_A_Net_(episode)',
 u'http://quantumleap.wikia.com/wiki/8_1/2_Months_(episode)',
 u'http://quantumleap.wikia.com/wiki/Goodbye_Norma_Jean_(episode)',
 u'http://quantumleap.wikia.com/wiki/Pool_Hall_Blues_(episode)',
 u'http://quantumleap.wikia.com/wiki/All_Americans_(episode)',
 u'http://quantumleap.wikia.com/wiki/Disco_Inferno_(episode)',
 u'http://quantumleap.wikia.com/wiki/Hurricane_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Color_of_Truth_(episode)',
 u'http://quantumleap.wikia.com/wiki/Trilogy_Part_I:_One_Little_Heart_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Leap_Between_The_States_(episode)',
 u'http://quantumleap.wikia.com/wiki/Ghost_Ship_(episode)',
 u'http://quantumleap.wikia.com/wiki/Camikazi_Kid_(episode)',
 u'http://quantumleap.wikia.com/wiki/A_Single_Drop_of_Rain_(episode)',
 u'http://quantumleap.wikia.com/wiki/Lee_Harvey_Oswald,_Part_II_(episode)',
 u'http://quantumleap.wikia.com/wiki/Catch_A_Falling_Star_(episode)',
 u'http://quantumleap.wikia.com/wiki/Animal_Frat_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Right_Hand_of_God_(episode)',
 u'http://quantumleap.wikia.com/wiki/Freedom_(episode)',
 u'http://quantumleap.wikia.com/wiki/Nowhere_To_Run_(episode)',
 u'http://quantumleap.wikia.com/wiki/Last_Dance_Before_An_Execution_(episode)',
 u'http://quantumleap.wikia.com/wiki/Dr._Ruth_(episode)',
 u'http://quantumleap.wikia.com/wiki/Memphis_Melody_(episode)',
 u'http://quantumleap.wikia.com/wiki/Honeymoon_Express_(episode)',
 u'http://quantumleap.wikia.com/wiki/Running_For_Honor_(episode)',
 u'http://quantumleap.wikia.com/wiki/Play_It_Again,_Seymour_(episode)',
 u'http://quantumleap.wikia.com/wiki/Killin%27_Time_(episode)',
 u'http://quantumleap.wikia.com/wiki/A_Portrait_For_Troian_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Leap_Home,_Part_I_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Leap_Back_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Leap_Home,_Part_II_(episode)',
 u'http://quantumleap.wikia.com/wiki/Moments_To_Live_(episode)',
 u'http://quantumleap.wikia.com/wiki/Play_Ball_(episode)',
 u'http://quantumleap.wikia.com/wiki/Southern_Comforts_(episode)',
 u'http://quantumleap.wikia.com/wiki/So_Help_Me_God_(episode)',
 u'http://quantumleap.wikia.com/wiki/Unchained_(episode)',
 u'http://quantumleap.wikia.com/wiki/The_Americanization_of_Machiko_(episode)',
 u'http://quantumleap.wikia.com/wiki/A_Little_Miracle_(episode)']


    def parse(self, response):
        found_date = False
        for td in response.xpath('//td'):
            if found_date:
                print td.extract()
                date = td.xpath('text()').extract().pop().split(';')
                break
            if td.xpath('b/text()').re('Leap Date'):
                found_date = True
        found_number = False
        for tr in response.xpath('//tr'):
            if found_number:
                print tr.xpath('td/text()').extract()[0]
                epnum = int(tr.xpath('td/text()').extract()[0])
                break
            if tr.xpath('td/b/text()').re('Episode No'):
                found_number = True
        yield {
            'date': date,
            'url': response.url,
            'episode': epnum,
        }