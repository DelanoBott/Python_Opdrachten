# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = "Gullit"
scorer_1 = "van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + str(goal_0), scorer_1 + str(goal_1)

report = "%s scored in the %snd minute." % (
    scorer_0, goal_0), "%s scored in the %snd minute." % (scorer_1, goal_1)

player = "Hans van Breukelen"
first_name = player[0:4]
last_name_start = player.find("v")
last_name = player[last_name_start:]
last_name_len = len(last_name)
name_short = player[0:1] + ". " + last_name
chant = last_name_len * "Hans! "

print(scorers)
print(report)
print(first_name)
print(last_name_len)
print(name_short)
print(chant[:-1])
