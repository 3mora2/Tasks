'''
//a[text()='second dropdown menu']/following::ul[1]/li/a[text()='link i want to find']
//a[text()='first dropdown menu']/ul/li[last()]/a/text()
//a[ancestor::ul/preceding::a[1]/text() = 'second dropdown menu']/text()
ul[preceding::a[text()='second dropdown menu' and position()=last()]]/li/a[text()='link i want to find']
//a[text()='second drop down menu'][2]


'''