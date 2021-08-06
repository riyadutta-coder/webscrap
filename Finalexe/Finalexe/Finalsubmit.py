from bs4 import BeautifulSoup
import requests
def flipkart(str1):


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r1 = requests.get(
        f'https://www.flipkart.com/search?q={str1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',
        headers=headers)
    htmlcontent2 = r1.content
    soup2 = BeautifulSoup(htmlcontent2, "html.parser")
    price1 = soup2.findAll(class_="_30jeq3 _1_WHN1")
    price2 = soup2.findAll(class_="_30jeq3")
    price3 = soup2.findAll(class_="_30jeq3")
    name1 = soup2.findAll(class_="s1Q9rs")
    flipkart_name = soup2.findAll(class_='_4rR01T')
    names = soup2.findAll(class_="_2WkVRV");
    # print(name1)
    # print(flipkart_name)
    # print(names)
    listprice = []
    namelist = []
    k = len(name1)
    j = len(flipkart_name)
    l = len(names)
    if k > 10:
        k = 10
    if j > 10:
        j = 10
    if l > 10:
        l = 10

    for i in range(k):
        p = price3[i].text
        p = p.replace("₹", "")
        p = p.replace(",", "")
        b = name1[i].text
        namelist.append(b)
        # print(b + "" + p)
        listprice.append(int(p))
    for i in range(j):
        p = price1[i].text
        p = p.replace("₹", "")
        p = p.replace(",", "")
        b = flipkart_name[i].text
        namelist.append(b)
        # print(b + " " + p)
        listprice.append(int(p))
    for i in range(l):
        p = price2[i].text
        p = p.replace("₹", "")
        p = p.replace(",", "")
        b = names[i].text
        namelist.append(b)
        #  print(b + " " + p)
        listprice.append(int(p))
    f = min(listprice)
    idx = listprice.index(f)
    print("Minimum Price in Flipkart")
    print(namelist[idx] + " Rs ", end="")
    print(f)

    pricestring =str(f)
    return [namelist[idx]+pricestring,f]

def amazon(str1):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    name1 = str1.replace(" ", "-")
    name2 = str1.replace(" ", "+")

    r2 = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
    htmlcontent2 = r2.content
    soup2 = BeautifulSoup(htmlcontent2, 'html.parser')
    price2 = soup2.findAll(class_="a-price-whole")
    # price2 = soup2.find('.a-price-whole')
    # price2=soup2.find(class_= 'a-price')
    name1 = soup2.findAll(class_="a-size-base-plus a-color-base a-text-normal")
    name2 = soup2.findAll(class_="a-size-medium a-color-base a-text-normal")
    p = len(name1)
    p1 = len(name2)
  #  print(name1)
   # print(price2)

    l1 = []
    l2=[]
    if p!=0:
        for i in range(10):
            b = price2[i].text
            b = b.replace(",", "")
            b = b.replace(" ", "")
           # print(name1[i].text)
            a = int(b)
            l1.append(a)
            k = name1[i].text
            # print(k)
            l2.append(k)

    elif p1!=0:

        for i in range(10):
            b = price2[i].text
            b = b.replace(",", "")
            b = b.replace(" ", "")
            #print(name2[i].text)
            b=b.replace(".","")
            a = int(b)
            l1.append(a)
            k = name2[i].text
            # print(k)
            l2.append(k)


    f = min(l1)
    idx = l1.index(f)
    print(l2[idx])
    listfinal=[]
    listfinal.append(l2[idx])
    listfinal.append(f)

    return listfinal



#main function
k=True
while(k):

    print("Welcome to the product searching portal")
    print("---------------------------------------")
    print("Menu:")
    print("Press 1 for Flipkart Low Price")
    print("Press 2 for Amazon low Price")

    choice =input("Press 3 for overall low price")
    if choice=='1':
        str1 = input("Enter the product name")
        listflipkart=flipkart(str1)
        print("Lowest Flipkart Price of Product:"+listflipkart[0])
        print("Price is "+str(listflipkart[1]))
    elif choice=='2':
        str1 = input("Enter the product name")
        listamazon=amazon(str1)
        print("Lowest Flipkart Price of Product:" + listamazon[0])
        print("Price is " + str(listamazon[1]))
    elif choice=='3':
        str1 = input("Enter the product name")
        listflipkart = flipkart(str1)
        print("Lowest Flipkart Price of Product:" + listflipkart[0])
        print("Price is " + str(listflipkart[1]))
        listamazon = amazon(str1)
        print("Lowest Flipkart Price of Product:" + listamazon[0])
        print("Price is " + str(listamazon[1]))
    else:
        print("wrong input")
    y = input("enter y to continue searching other keys to exit")
    if y == 'y' or y == "Y":
     k = True

    else:
     k = False


