adjective = ["Charming","Cruel","Fantastic","Gentle","Huge","Perfect","Rough","Sharp","Tasty","Zealous"]
noun = ["man","woman","teacher","John","Mary","home","office","town","countryside","America","table","car","banana","money","music","love","dog","monkey"]

import random
num = random.randrange(1,100)
adj = random.choice(adjective)
noun = random.choice(noun)
import string
spl_char = string.punctuation
spl =random.choice(spl_char)
print(f"Password Suggestion : {num}{adj}{spl}{noun}")