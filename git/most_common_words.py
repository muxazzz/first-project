import sys, re
from collections import Counter

try:
    num_words = int(sys.argv[1])
except:
    print("Input number")
    sys.exit(1)


counter = Counter(word.lower() for line in sys.stdin for word in line.strip().split() if len(word)>4)
for item in counter:
    item = re.sub('[?@!,.:]', '', item)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
    
    
    print('heeloo')