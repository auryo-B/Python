sessionKarting = max(0.0, float(input("Combien de session de karting faite ce mois-ci : ")))
creditKarting = max(0.0, float(input("Reste de credit du mois dernier : ")))
prixSpotify = max(0.0, float(input("Prix de l'abonnement Spotify : ")))
prixCrunchyroll = max(0.0, float(input("Prix pour accéder à Crunchyroll : ")))
hh = input("Session en happy hour : ")


if hh == "oui" :
	prixSession = 10
else :
	prixSession = 20

def argentPoche():
	
	argentR = 20 - prixSpotify - prixCrunchyroll
	credit_Karting = creditKarting + 20
	
	if sessionKarting >= 1 :
		credit_Karting = credit_Karting - prixSession*sessionKarting
		argentR = argentR + credit_Karting
		return(argentR)
	else :
		argentR = argentR + credit_Karting
		return(argentR)

print(argentPoche())