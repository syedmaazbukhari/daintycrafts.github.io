
f = open('template.txt', 'r',encoding='UTF8')
tahir=[]

tahir=f.readlines()
#print(tahir)
c=0
filename=str(input("Enter Product File Name(keyboard): "))

for i in tahir:
    if i == '\t\t\t\t<p> Home/ Headphones </p>\n':
        cat=str(input("Enter Category(Headphones etc): "))
        tahir[c]='\t\t\t\t<p>' +cat+' </p>\n'

    elif i == '\t\t\t\t<h1> Cloud II Gaming By HyperX </h1>\n':
        name=str(input("NAME OF THE PRODUCT: "))
        tahir[c]='\t\t\t\t<h1> '+name +' </h1>\n'

    elif i == '\t\t\t\t<h4> $66 </h4>\n':
        price = str(input("PRICE IN PKR: "))
        tahir[c] = '\t\t\t\t<h4> '+price+'</h4>\n'


    elif i == '\t\t\t\t<p>desc </p>\t\n':
        desc = str(input("Product Description: "))
        tahir[c] = '\t\t\t\t<p>'+desc+' </p>\t\n'


    elif i == '\t<h1 class="pid">PRODUCT ID: 0000</h1>\n':
        pid = str(input("Product ID: "))
        tahir[c] = '\t<h1 class="pid">PRODUCT ID: '+pid+'</h1>\n'

    elif i == '\t\t\t\t\t<h4> Nvidia RTX 3080ti </h4>\n':
        r1 = str(input("Related Product 1 NAME: "))
        tahir[c] = '\t\t\t\t\t<h4> '+r1+' </h4>\n'

    elif i == '\t\t\t\t\t<img src="3080.jpg">\n':
        i1 = str(input("Image Related Product 1(.jpg/png): "))
        tahir[c] = '\t\t\t\t\t<img src="'+i1+'">\n'

    elif i == '\t\t\t\t<p> PKR 128,000 </p>\t\n':
        p1 = str(input("Price Related Product 1: "))
        tahir[c] = '\t\t\t\t<p> '+p1 +' </p>\t\t\n'
    elif i == '\t\t\t\t<a href="p-Details2.html">\t\n':
        h1 = str(input("Href link for Related 1(details.html): "))
        tahir[c] = '\t\t\t\t<a href="' + h1 + '">\t\n'







    elif i == '\t\t\t\t\t<h4> Corsair Gaming k95 Platinum </h4>\n':
        r2 = str(input("Related Product 2 NAME: "))
        tahir[c] = '\t\t\t\t\t<h4> '+r2+' </h4>\n'

    elif i == '\t\t\t\t\t<img src="k95.jpg">\n':
        i2 = str(input("Image Related Product 2(.jpg/png): "))
        tahir[c] = '\t\t\t\t\t<img src="'+i2+'">\n'

    elif i == '\t\t\t\t<p> PKR 24,999 </p>\t\t\n':
        p2 = str(input("Price Related Product 2: "))
        tahir[c] = '\t\t\t\t<p> '+p2 +' </p>\t\t\n'
    elif i == '\t\t\t\t<a href="p-Details4.html">\n':
        h2 = str(input("Href link for Related 2(details.html): "))
        tahir[c] = '\t\t\t\t<a href="'+h2 +'">\n'




    elif i == '\t\t\t\t\t<h4> CORSAIR VENGEANCE RGB PRO </h4>\n':
        r3 = str(input("Related Product 3 NAME: "))
        tahir[c] = '\t\t\t\t\t<h4> '+r3+' </h4>\n'

    elif i == '\t\t\t\t\t<img src="ram1.jpg">\n':
        i3 = str(input("Image Related Product 3(.jpg/png): "))
        tahir[c] = '\t\t\t\t\t<img src="'+i3+'">\n'

    elif i == '\t\t\t\t<p> PKR 19,999 </p>\t\n':
        p3 = str(input("Price Related Product 3: "))
        tahir[c] = '\t\t\t\t<p> '+p3 +' </p>\t\n'
    elif i == '\t\t\t\t<a href="p-Details6.html">\t\n':
        h3 = str(input("Href link for Related 3(details.html): "))
        tahir[c] = '\t\t\t\t<a href="'+h3 +'">\t\n'

    c=c+1
fx = open(filename+".html", "w")
for i in tahir:
    fx.write(i)
f.close()
fx.close()
print("*** FILE" +filename+".html HAS BEEN CREATED SUCESSFULLY ***")



