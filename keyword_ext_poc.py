import json, re
from collections import defaultdict

inverted_index = defaultdict(list)
tag_counts = defaultdict(lambda: defaultdict(int))

with open('B00I11N2VO_tags_45.json') as fp:
    j = json.load(fp)['B00I11N2VO']

    for i in range(len(j)):
        for obj in j[i]:
            print(obj)
            tag = re.split('- ', obj['attribute'])
            if len(tag) > 3:
                continue
            t = ' '.join(tag)
            inverted_index[t].append(i)
            senti = obj['sentiment']
            tag_counts[t][senti] += 1
            tag_counts[t]['total'] += 1
            

with open('inv_ind.json', 'w+') as json_file:
    json.dump(inverted_index, json_file, indent=4)

with open('tag_counts.json', 'w+') as json_file:
    json.dump(tag_counts, json_file, indent=4)
