def stopWords(file_name):
    excludewords = []
    f = open(file_name, 'r')
    for line in f.readlines():
        excludewords.append(line.strip())
    return excludewords