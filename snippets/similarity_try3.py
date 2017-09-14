from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from textblob import TextBlob
 
def penn_to_wn(tag):
    if tag.startswith('N'):
        return 'n'
    if tag.startswith('V'):
        return 'v'
    if tag.startswith('J'):
        return 'a'
    if tag.startswith('R'):
        return 'r'
    return None



def tagged_to_synset(word,tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:
        return wn.synsets(word, wn_tag)[0]
    except:
        return None



def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    sentence1 = sentence1.tags
    sentence2 = sentence2.tags
    
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]
    
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]
    
    score, count = 0.0, 0
    
    for synset in synsets1:
        
        li=[synset.path_similarity(ss) for ss in synsets2]
        m=0
        for i in range(len(li)):
            if li[i] is not None and m<li[i]:
                m=li[i]
        if m != 0:
            score += m
            count += 1

    if count is 0:
        score = 0
    else:
        score /= count
    return score

def checkSimilarity(sentence,focus_sentence):
    a1=sentence_similarity(focus_sentence, sentence)
    a2=sentence_similarity( sentence,focus_sentence)

    return max(a1,a2)
print(checkSimilarity(TextBlob("documents is selected"),TextBlob("documents is preferred")))

