import sys

print('"email_hash","category","filename"')

for filepath in sys.argv[1:]:
    fr = open(filepath, "r")
    for line in fr.read().split('\n')[1:-1]:
        print(line + ',"' + filepath.split('/')[-1] + '"')
