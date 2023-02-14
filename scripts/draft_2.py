import os
import requests
import json

def main():
    members = get_members_data()
    parties = group_members_by_party(members)
    dems = parties[0]
    reps = parties[1]
    #print(json.dumps(reps, indent=4))
    dem_sorted = sort_members(dems)
    #print(dem_sorted[0:5])
    #rep_sorted = sort_members(reps)
    #print(json.dumps(members, indent=4))

def get_members_data():
    headers = {'X-API-Key': os.environ["PROPUBLICA_API_KEY"] }
    url = "https://api.propublica.org/congress/v1/117/senate/members.json"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data ['results'][0]['members']


def group_members_by_party(members):
    democrat = []
    republican = []
    for member in members:
        if member['party'] == 'D':
            democrat.append(member)
        elif member['party'] == 'R':
            republican.append(member)
    return [democrat, republican]


def sort_members(mems):
# sorted(x, key=itemgetter('name'), reverse=True)
# [{'name': 'Leqi', 'city': 'Berkeley'}, {'name': 'Jane', 'city': 'Palo Alto'}]
    #for mem in mems:
#return sorted_mems

#I'm confused, shall I sort [democrat] and [republican] seperately?
# Then why did we make a list of lists  grouped_members = [democrat, republican] ?





""" 
sort_percentage_d = "* {first} {last} ({state}) votes against the party {votes_against_party_pct} %of the time."
print(sort_percentage_d.format(first = "first_name", last = "last_name", state = "state", votes_against_party_pct = "votes_against_party_pct"))

sort_percentage_r = "* {first} {last} ({state}) votes against the party {votes_against_party_pct} %of the time."
print(sort_percentage_r.format(first = "first_name", last = "last_name", state = "state", votes_against_party_pct = "votes_against_party_pct"))

"""
main()