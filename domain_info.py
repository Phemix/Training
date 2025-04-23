# domain_info.py

import whois

def get_domain_details(domain_name):
    details = whois.whois(domain_name)
    domain_age = details.expiration_date - details.creation_date
    return {
        "age": domain_age,
        "details": dict(details)
    }
