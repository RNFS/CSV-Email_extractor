import csv 

import re

emails  = []
# regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
c = 0
# change this for the targted file 
with open ("an_data.csv", "r") as f:
    for x in f :
        if res := re.search(r'^([a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3})$', x):
            email = res.group(1)
            if email not in emails:
                emails.append(email)
                print(c)
                c += 1 



with open("series_emails.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["email"])
    for email in emails:  
        writer.writerow({"email": email})