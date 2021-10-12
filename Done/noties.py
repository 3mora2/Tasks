"""
XPATH:

    //a[text()='second dropdown menu']/following::ul[1]/li/a[text()='link i want to find']

    //a[text()='first dropdown menu']/ul/li[last()]/a/text()
    
    //a[ancestor::ul/preceding::a[1]/text() = 'second dropdown menu']/text()
    
    ul[preceding::a[text()='second dropdown menu' and position()=last()]]/li/a[text()='link i want to find']
    
    //a[text()='second drop down menu'][2]
    
    //div[contains(@class, 'inputInfo') and contains(text(), 'Noon SKU Price')] / *[@class='priceRange']
    
    //div[calss="btnWrapper"]/div[text()="Submit"] | //div[contains(@class,"showAlert")]//div[contains(@class,"solid")][2]


CSS SELECTOR:

    tag[attr=value]
    input[type="search"]
    
    tag#id > tag.class
    div#name > span.any-class
    
    tag:nth-child(1)> first-child
    tr:nth-child(1) > td

    tag[href*="/en"] any tag [its href contains('/en')
    a[href*="/en-sa/noon-catalog/preview/"]


"""