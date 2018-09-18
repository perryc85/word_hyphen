# target word
word = input('Enter word: ').strip()

# each index is a space in the target word. 
# Each val is the score of that space.
scores = [0] * len(word) 
scores.pop() # minus one 

DOT = "."

def stripped_patterns(pattern):
    stripped_pattern = ''
    for char in pattern:
        # strip out all non-alpha chars and store them into temp var
        if char.isalpha():
            stripped_pattern += char
    return stripped_pattern

def find_score_indexs(pattern):
    # the index of scores in the pattern
    list_vals = [] 
    for i, value in enumerate(pattern):
        if value.isdigit():
            list_vals.append(i)
    return list_vals

def count_scores(pattern):
    num_of_scores = 0
    for i, value in enumerate(pattern):
        if value.isdigit():
            # keep track of the number of scores in pattern
            num_of_scores += 1
    return num_of_scores

def pattern_in_string(pattern):
    # index of stripped_pattern in the target word
    pattern_match = word.find(stripped_pattern)
    list_vals = find_score_indexs(pattern)
    num_of_scores = count_scores(pattern)

def score_spaces(pattern, scores, pattern_match, list_vals, dot_in_front):
    print(f'Pattern: {pattern}')

    # find index of scores in pattern
    scores_index = find_score_indexs(pattern)

    # the formula to find the correct space score -- 
    # the PM + list_vals - num_of scores
    if dot_in_front:
        num_of_scores = 2
    else:
        num_of_scores = 1
    
    for val in scores_index:
        # var to hold proper space in scores list
        proper_space = pattern_match + val - num_of_scores
        if len(scores) - 1 >= proper_space \
            and int(pattern[val]) > int(scores[proper_space]):
            scores[proper_space] = pattern[val]
        num_of_scores += 1

    print(f'Scores: {scores}')
    return scores

def hyphen_word(pattern, scores, word):
    # create string with hyphens
    hyphen_word = ''

    # the actual hyphen
    hyphen = '-'

    num_of_hyphens = 1

    for i, w in enumerate(word):
        if i <= len(scores) - 1 \
        and int(scores[i]) % 2 != 0:
            hyphen_word += w + hyphen 
        else:
            hyphen_word += w

    return hyphen_word

# read file containing patterns -- main part of program
with open('patterns.txt','r') as f:

    # iterate over file
    for pattern in f:
        pattern = pattern.strip()

        stripped_pattern = stripped_patterns(pattern)
        pattern_match = word.find(stripped_pattern)
        list_vals = find_score_indexs(pattern)

        # if dot at start, pattern must appear in beg.
        if DOT == pattern[0] and pattern_match == 0:
            list_vals = find_score_indexs(pattern)
            num_of_scores = count_scores(pattern)
            scores = score_spaces(pattern, scores, pattern_match, list_vals, True)
        # if dot at end, pattern must appear at the end
        elif DOT == pattern[-1] and len(stripped_pattern) + pattern_match == len(word):
            list_vals = find_score_indexs(pattern)
            num_of_scores = count_scores(pattern)
            scores = score_spaces(pattern, scores, pattern_match, list_vals, False)
        # if pattern appears in string, score it according to the rules.
        elif pattern_match >= 0 and DOT != pattern[0] and DOT != pattern[-1]:
            pattern_in_string(pattern)
            scores = score_spaces(pattern, scores, pattern_match, list_vals, False)

    print(hyphen_word(pattern, scores, word))