# this function takes 3 parameters to update the email with old_domain to email with new_domain.
# email
# old_domain
# new_domain

def update_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index =  email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        print(new_email)
        return new_email
    return email

update_domain("simran.kaur@manulife.com", "manulife.com", "rci.rogers.com")