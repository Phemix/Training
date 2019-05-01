import whois
w = input("enter a domain name, no need for quotes:  ")
domainDetails = whois.whois(w)
domainAge = (domainDetails.expiration_date - domainDetails.creation_date)
print("Domain Age is", domainAge)
print ("\nother domain details are: \n")
print (type(domainDetails))
print (dict(domainDetails))
