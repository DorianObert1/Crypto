import ccxt
import time

def prix_du_BTC():
    exchange = ccxt.binance()
    symbol = 'BTC/EUR'

    solde = 1000
    argent_place = 0
    gain_total = 0
    prix_precedent = 0
    achat_en_cours = False
    run = True
    while run:
        print()
        try:
            gain = 0
            ticker = exchange.fetch_ticker(symbol)
            dernier_prix = ticker['last']
            if dernier_prix >= prix_precedent:
                if not achat_en_cours:
                    argent_place = solde
                    achat_en_cours = True
                    print("Achat effectué, prix :", dernier_prix, "€, argent placé :", round(argent_place,2), "€")
                elif achat_en_cours:
                    argent_place = argent_place * dernier_prix / prix_precedent
                    print('Argent placé :', round(argent_place,2), '€')
            elif dernier_prix < prix_precedent:
                if achat_en_cours:
                    gain = argent_place - solde
                    achat_en_cours = False
                    solde = argent_place
                    argent_place = 0
                    print("Vente effectuée, prix :", dernier_prix, "€, argent placé :", round(argent_place,2), "€ gain :", round(gain,2), "€")
            prix_precedent = dernier_prix
            gain_total += gain
            print("Gain total :", round(gain_total,2), "€")
            print('Le prix de BTC est de :', ticker['last'])

        except ccxt.RequestTimeout as e:
            print("RequestTimeout caught, retrying...")
        except ccxt.DDoSProtection as e:
            print("DDoSProtection caught, retrying...")
        time.sleep(1)