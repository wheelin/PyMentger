#! python
__author__ = 'Gregory'
import csv
from random import shuffle

gF_teams = "work_teams.csv"
gF_matches = "matches.txt"
gL_adult_teams = []
gL_kid_teams = []
gL_matches = []

def fill_team_list():
    with open(gF_teams, 'r') as csv_team:
    	rdr = csv.reader(csv_team, delimiter=';')
    	for row in rdr:
    		if len(row) == 4:
	    		if row[1] == 'a':
	    			gL_adult_teams.append(row[0])
	    		elif row[1] == 'k':
	    			gL_kid_teams.append(row[0])

def compute_match_list(tl):
	ml = []
	i = 0
	j = 1
	while i < len(tl):
		while j < len(tl):
			if tl[i] is not tl[j]:
				ml.append([tl[i], tl[j]])
			j += 1
		i += 1
		j = i + 1
	return ml

def count_matches(tl):
	i = len(tl) - 1
	num_matches = 0;
	while i != 0:
		num_matches += i
		i -= 1
	return num_matches


def randomize_match_list(ml):
	shuffle(ml)
	rml = []
	i = 0
	append_first = False
	added = False
	length = len(ml)
	rml.append(ml.pop(0))
	while len(rml) is not length:
		print("pass : {0}".format(i))
		if ml[i][0] not in rml[-1] and ml[i][1] not in rml[-1]:
			rml.append(ml.pop(i))
			added = True
		if i >= len(ml) - 1:
			i = 0
			if added is False:
				rml.append(ml.pop(0))
				print("added follower")
			added = False
		else:
			i += 1
	return rml


def print_list(l):
	for e in l:
		print(e)

def check_randomization(ml):
	i = 1
	while i < len(ml):
		if ml[i - 1][0] in ml[i] or ml[i - 1][1] in ml[i]:
			print(ml[i - 1])
			print(ml[i])

fill_team_list()
print(gL_adult_teams)
print(gL_kid_teams)
print("\n")
gL_matches = compute_match_list(gL_adult_teams)
print(gL_matches)
rml = randomize_match_list(gL_matches)
print_list(rml)
print(len(rml))