#!/usr/bin/env python3

def beer_price(vendor, name, volume, price):
    #Calculates the price (R$) per beer volume (mL)
    price_per_liter = round(price/(volume/1000), 2)
    print (u"O litro da %s %smL no %s é R$%s/L\n" %(name, volume, vendor, str(price_per_liter)))
    return price_per_liter

print("\nFiesta Latina: Latão Brahma 473mL a 2.25/unidade ou R$4,76/L no Extra - mês 09 (120L e cerca de 150 pessoas).\n")
#beer_price("Extra", "Brahma", 473, 2.25)

print("Cabra Macabra: Latão Brahma 473mL a 2.45/unidade ou R$5,18/L no Extra - mês 10 (120L e cerca de 100 pessoas, sobrou 1 terço da breja).\n")

#beer_price("Tonin", "Brahma", 350, 1.98)

#beer_price("Tonin", "Latão", 550, 3.13)

#beer_price("Tonin", "Kaiser", 350, 1.69)

#beer_price("Extra", "Latão", 473, 2.45)

print("Cotação da Cher-ry Christmas:")

#beer_price("Carrefour", "Heineken", Leve 3 pague 2)

beer_price("Tonin", "Brahma", 550, 3.54)

beer_price("Tonin", "Brahma", 550, 3.54)

beer_price("Tonin", "Kaiser", 350, 1.83)

beer_price("Tonin", "Skoll", 350, 2.30)

beer_price("Tonin", "Skoll", 473, 2.99)
beer_price("Tonin", "Skoll", 473, 2.95)

beer_price("Tonin", "Skoll", 550, 3.54)

beer_price("Tonin", "Heineken", 350, 3.19)

print("Cotação da Cher-ry Christmas Extra - Black Friday")

beer_price("Extra", "Skoll", 269, 1.66)

beer_price("Extra", "Skoll Retornável até 27", 300, 1.59)

beer_price("Extra", "Einsenbahn", 350, 2.49)

print("Ihullll!!!!!!!!!!!!")
beer_price("Extra", "Amstel", 350, 1.86)
print("Ihullll!!!!!!!!!!!!")

beer_price("Extra", "Brahma", 269, 1.49)

beer_price("Extra", "Eisenbahn", 600, 3.99)

beer_price("Extra", "Eisenbahn", 355, 2.49)

beer_price("Extra", "Eisenbahn", 600, 3.99)

beer_price("Extra", "Estrella Galícia", 600, 3.99)

beer_price("Extra", "Estrella Galícia", 330, 2.99)

beer_price("Extra", "Estrella Galícia", 200, 1.89)

beer_price("Extra", "Estrella Galícia", 269, 1.79)

beer_price("Extra", "Brahma Extra Lager", 350, 1.99)

beer_price("Extra", "Colorado", 600, 9.24)

beer_price("Extra", "Antártica Original", 300, 2.65)

beer_price("Extra", "Skoll Ultra", 310, 1.99)

print("Cotação da Cher-ry Christmas Extra - FdS")

beer_price("Extra", "Itaipava", 350, 1.69)

beer_price("Extra", "Brahma", 269, 1.59)

print("Ihullll!!!!!!!!!!!!")
beer_price("Extra", "Brahma Latão", 473, 2.46)
print("Ihullll!!!!!!!!!!!!")

beer_price("Extra", "Skoll", 350, 2.24)

beer_price("Tradere", "Trairagem", 600, 18)
beer_price("Tradere", "Trairagem", 500, 15)
