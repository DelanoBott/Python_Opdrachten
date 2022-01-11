# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)

report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"

player = "Hans van Breukelen"
first_name_end = player.find(" ")
first_name = player[0:first_name_end]
first_name_len = len(first_name)
last_name_start = player.find(" ")
last_name = player[last_name_start + 1:]
last_name_len = len(last_name)
name_short = first_name[0:1] + ". " + last_name
chant_full = first_name_len * (first_name + "!" + " ")
chant = chant_full[:-1]
good_chant = chant[:-1] != " "

print(scorers)
print(report)
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(good_chant)
