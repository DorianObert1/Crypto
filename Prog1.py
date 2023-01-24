import ccxt
import time

def prix_du_BTC():
    exchange = ccxt.binance()
    symbol = 'BTC/EUR'

    montant_en_eur = 1000
    argent_disponible = 0
    prix_precedent = 0
    gain_total = 0
    achat_en_cours = True
    run = True
    while run:
        print()
        try:
            ticker = exchange.fetch_ticker(symbol)
            dernier_prix = ticker['last']
            if dernier_prix > prix_precedent:
                if not achat_en_cours:
                    if argent_disponible >= montant_en_eur:
                        achat_en_cours = True
                        argent_disponible -= montant_en_eur
                        print("Achat effectué, prix :", dernier_prix, "€, argent disponible :", argent_disponible, "€")
            elif dernier_prix < prix_precedent:
                if achat_en_cours:
                    gain = montant_en_eur * (dernier_prix / prix_precedent)
                    achat_en_cours = False
                    gain_total += gain
                    montant_en_eur += gain
                    print("Vente effectuée, prix :", dernier_prix, "€, gains réalisés :", gain_total, "€")
            prix_precedent = dernier_prix
            print('Gain total :', gain_total, '€')
            print('Le prix de BTC est de :', ticker['last'])

        except ccxt.RequestTimeout as e:
            print("RequestTimeout caught, retrying...")
        except ccxt.DDoSProtection as e:
            print("DDoSProtection caught, retrying...")
        time.sleep(1)