#1. Given a list of client emails, create a function that takes in the list as an argument and returns
#a new list with only the domain of each email. This was inspired by an actual problem I did at work recently.
#clients = ['brucewayne@gotham.com', 'homer_simpson@springfieldnuclear.com', 'hank_hill@arlenpropane.com', 'petergriffin@pawtucketbrewery.com']
#Example
#get_domains(clients) = ['gotham.com', 'springfieldnuclear.com', 'arlenpropane.com', 'pawtucketbrewery.com']

import re
def get_domains(clients):
    domainList=[]
    for str in clients:
        domain = re.search('@[\w.]+', str)
        pattern = re.compile(r'@+')
        domainList.append(re.sub(pattern, '', domain.group()))
    return domainList

clients = ['brucewayne@gotham.com', 'homer_simpson@springfieldnuclear.com', 'hank_hill@arlenpropane.com', 'petergriffin@pawtucketbrewery.com']
domain=get_domains(clients)
print(domain)

#Using List Comprehension
import re
def get_domains(clients):
    pattern = re.compile(r'@+')
    return [re.sub(pattern, '', re.search('@[\w.]+', str).group()) for str in clients]
clients = ['brucewayne@gotham.com', 'homer_simpson@springfieldnuclear.com', 'hank_hill@arlenpropane.com', 'petergriffin@pawtucketbrewery.com']
print(get_domains(clients))
