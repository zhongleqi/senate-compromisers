import os
import requests
import json

def main():
    members = get_members_data()
    parties = group_members_by_party(members)
    dems = parties[0]
    reps = parties[1]
    dem_sorted = sort_members(dems)
    rep_sorted = sort_members(reps)
    print("\nSenators most likely to break ranks:\n")
    print_members("Democrat", '-' * len("Democrat"), dem_sorted[0:5])
    print_members("Republican", '-' * len("Republican"), rep_sorted[0:5])

def print_members(party_name, dashline, mems):
    print(party_name)
    print(dashline)
    for mem in mems:
        first_name = mem['first_name']
        last_name = mem['last_name']
        state = mem['state']
        votepct = mem['votes_against_party_pct']
        output = f"* {first_name} {last_name} ({state}) votes against the party {votepct} %of the time."
        print(output)
    print()

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
    mems_sorted = sorted(mems, key=lambda member:member['votes_against_party_pct'],reverse=True)
    return mems_sorted

main()