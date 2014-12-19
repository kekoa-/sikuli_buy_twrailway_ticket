import shutil
import os.path

def getSklPath():
    return getBundlePath()[:-8]+'/'
        
main_reg = Region(0,87,683,566)
sec_reg = Region(0,0,609,507)
third_reg = Region(0,0,684,619)
def capturingValid(pic_name):
    pos = sec_reg.find("1418978414747.png")
    pic = capture(pos.above(77).nearby(-10))
    skl_pic = getSklPath()+pic_name
    os.remove(skl_pic)
    shutil.move (pic, skl_pic)
def getValidKey(pic_name):
    return -1

def buy_series_train(list):
    Settings.MoveMouseDelay = 0.1
    for train in list:
        main_reg.exists("1418974460310.png", 0.5)
        reg2 = main_reg.find("1418974460310.png").right(175)
        reg2.doubleClick()
        type(Key.DELETE) 
        type(train+Key.TAB)
        wait(0.1)
        buy_two_ticket = Pattern("twoTicket-2.png").similar(0.45).targetOffset(0,-30)
        if not reg2.below(100).exists("1418975901700.png", 0) :
            if reg2.right(300).exists("1418927064591.png", 0):
                reg2.below(100).click(Pattern("1418926828169.png").targetOffset(26,2))
                reg2.below(300).exists(buy_two_ticket, 0.5)
                reg2.below(300).click(buy_two_ticket)
            elif reg2.right(300).exists("1418931581935.png", 0):
                reg2.below(100).click(Pattern("1418926828169.png").targetOffset(26,2))
                reg2.below(300).exists(buy_two_ticket, 0.5)
                reg2.below(300).click(buy_two_ticket)
            else:
                reg2.below(100).click(Pattern("1418976550075.png").similar(0.48))
                reg2.below(300).exists(buy_two_ticket, 0.5)
                reg2.below(300).click(buy_two_ticket)
        reg2.below(300).click("1418926780388.png")
    
        sec_reg.exists("1418927190669.png",0.5)
        sleep(0.05)
        pic = sec_reg.find("1418927190669.png")        
        key = input( u"The 驗證" )
        sec_reg.paste(Pattern("1418927840669.png").targetOffset(-49,-13), key)
        sec_reg.click("1418927859294.png")   
        wait(0.2)
        if third_reg.exists("1418981173919.png", 0.5) or third_reg.exists("1418977601653.png", 0.0) \
                or third_reg.exists("1418952066872.png", 0):
            type(Key.BACKSPACE)
            wait(0.2)
            third_reg.click("1418931108544.png")
        else :
            break
    Settings.MoveMouseDelay = 0.5


def open_website(url, person_id):
    main_reg = Region(0,1,628,406)
    main_reg.find("1418937615372.png").right(200).click()
    type("a", Key.CTRL)
    paste(url)
    type(Key.ENTER)
    main_reg.exists("1418938141435.png")
    main_reg.click("1418938141435.png")
    paste(person_id)
    
list_tai_hua = ["5232", "402", "404", "5204" ,"5672", "5682", "5234", "74", "206", "272", "5408", "5236", "410", "208"] 
list_tai_yi_hua = ["404", "5204" ,"5672", "5682", "206", "272", "208"] 


open_website("http://railway.hinet.net/ctno1.htm?from_station=073&to_station=051&getin_date=2015/01/01", "A128378388")
buy_series_train(list_tai_yi_hua[:5])

#open_website("http://railway.hinet.net/ctno1.htm?from_station=100&to_station=051&getin_date=2015/01/01", "A128378388")
#buy_series_train(list_tai_hua)



#open_website("http://railway.hinet.net/ctno1.htm?from_station=073&to_station=051&getin_date=2015/01/01", "A128378388")
#buy_series_train(list_tai_hua)

#open_website("http://railway.hinet.net/ctno1.htm?from_station=100&to_station=073&getin_date=2015/01/01", "A128378388")
#buy_series_train(list_tai_yi_hua)



    