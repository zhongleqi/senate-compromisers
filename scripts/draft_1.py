import os
import requests
import json

def main():
    data = get_members_data()
    for members in data['results'][0]['members']:
        print(members)
    grouped_members = group_members_by_party(members)

    print(json.dumps(members, indent=4))

def get_members_data():
    headers = {'X-API-Key': os.environ["PROPUBLICA_API_KEY"] }
    url = "https://api.propublica.org/congress/v1/118/senate/members.json"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data


# above is what we achieved on Wednesday
# at this point, I seem to have a list of dictionary of data
# Here are the items I need: first name, last name, state, percentage of against votes, party.
# So these are the steps I need to do:
# 1, get the items; 2, divide the data into two groups by party; 3, sort data in each group based on the percentage of against votes; 4, print the result.


def group_members_by_party():
    for member in members ['first_name'] ['last_name'] ['state'] ['party'] ['votes_against_party_pct']:
        democrat = [member in members if member['party'] == "D"]
        republican = [member in members if member['party'] == "R"]
        return member

def sort_percentage_d():
    for d_member in democrat:
        sorted(key=democrat('votes_against_party_pct'), reverse=True)
        return d_member[0,5]

def sort_percentage_r():
    for r_member in republican:
        sorted(key=republican('votes_against_party_pct'), reverse=True)
        return r_member[0,5]

# I'm lost...
# am I getting a list or a dict?

sort_percentage_d = "* {first} {last} ({state}) votes against the party {votes_against_party_pct} %of the time."
print(sort_percentage_d.format(first = "first_name", last = "last_name", state = "state", votes_against_party_pct = "votes_against_party_pct"))

sort_percentage_r = "* {first} {last} ({state}) votes against the party {votes_against_party_pct} %of the time."
print(sort_percentage_r.format(first = "first_name", last = "last_name", state = "state", votes_against_party_pct = "votes_against_party_pct"))


main()