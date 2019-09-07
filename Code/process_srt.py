import pysrt
import glob, sys, os
import string, re
import argparse
from nltk.tokenize import sent_tokenize, word_tokenize


def convert_srt_to_text(fpath):
    # input: filepath of srt file
    # output: plain text of the srt file content
    text =''
    subs = pysrt.open(fpath)
    for sub in subs:
        text+=(sub.text+' ')
    text = text.replace('<i>',' ')
    text = text.replace('</i>',' ')

    text = " ".join(text.split())
    text = text.replace('www.OpenSubtitles.org', '')
    text = text.replace('Subtitles by explosiveskull','')
    return text

def word_list(text):
    sentences = sent_tokenize(text)
    ans = []
    for s in sentences:
        s_lower = s.lower()
        # more preprocessing
        tokens = word_tokenize(s_lower)
        token_list = [x for x in tokens if not re.fullmatch('[' + string.punctuation + ']+', x)]

        ans.append(' '.join('page_'+x for x in token_list)+'\n')
    return ans

if __name__=='__main__':
    try:
        srt_path = sys.argv[1]
    except Exception as e:
        print('directory for srt files not found')
    print(srt_path)
    for file in glob.glob(srt_path+"/*.srt"):
        text = convert_srt_to_text(file)
        word_list = word_list(text)

        with open("../Data/word_list/"+os.path.basename(file)[:-4]+'.txt', 'w+') as text_file:
            text_file.writelines(word_list)
