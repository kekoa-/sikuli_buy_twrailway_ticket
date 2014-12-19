list = ["5232"]

click(Pattern("1418926828169.png").targetOffset(26,2))
click(Pattern("twoTicket-1.png").targetOffset(-3,-23))
list = []
for train in list:
    click("1418926182779.png")
    type(Key.DELETE+ Key.DELETE+ Key.DELETE+ Key.DELETE+ Key.DELETE) 
    type(Key.BACKSPACE+ Key.BACKSPACE+ Key.BACKSPACE+ Key.BACKSPACE+ Key.BACKSPACE)
    type(train)
    click("1418926931560.png") 
    sleep(0.1)
    
    if exists("1418927064591.png"):
        click(Pattern("1418926828169.png").targetOffset(26,2))
        click(Pattern("twoTicket-1.png").targetOffset(-3,-23))
    elif exists("1418926973154.png"):
        click(Pattern("1418926984544.png").targetOffset(14,-10))
        click(Pattern("twoTicket-1.png").targetOffset(-3,-23))
    if exists("1418926611919.png"):
        click(Pattern("1418926638122.png").targetOffset(50,0))
        click(Pattern("twoTicket-1.png").targetOffset(-3,-23))
    click("1418926780388.png")
    sleep(0.5)
    pic = find("1418927190669.png")
    pic.x -= 20
    pic.y -= 20
    capture(pic.x, pic.y, 400, 200)
    key = input( u"The 驗證" )
    type(Pattern("1418927840669.png").targetOffset(-49,-13), key)
    click("1418927859294.png")
    if exists("1418927888872.png"):
        type(Key.BACKSPACE)
        sleep(0.3)
        type(Key.TAB+ Key.BACKSPACE)
        sleep(0.5)   
    else:
        break
        
    