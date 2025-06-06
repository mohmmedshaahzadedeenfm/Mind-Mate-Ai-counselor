
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re, math
from collections import Counter

ps=PorterStemmer()

WORD = re.compile(r'\w+')
def checkans(ans,oans):
     def sr(txt):
          stop_words=set(stopwords.words('english'))
          word_tokens=word_tokenize(txt)
          filtered_sentence=[w for w in word_tokens if not w.lower() in stop_words]
          filtered_sentence1=[]
          for i in filtered_sentence:
               #filtered_sentence1.append(ps.stem(i))
               filtered_sentence1.append(i)
          print("*************",filtered_sentence1)

          return ' '.join(filtered_sentence1)
     def get_cosine(vec1, vec2):
          intersection = set(vec1.keys()) & set(vec2.keys())
          numerator = sum([vec1[x] * vec2[x] for x in intersection])

          sum1 = sum([vec1[x]**2 for x in vec1.keys()])
          sum2 = sum([vec2[x]**2 for x in vec2.keys()])
          denominator = math.sqrt(sum1) * math.sqrt(sum2)

          if not denominator:
             return 0.0
          else:
             return float(numerator) / denominator

     def text_to_vector(text):
          words = WORD.findall(text)
          return Counter(words)
          ####///////////////////////////////////////////////////////////////////////////////

     text1=sr(ans.lower())
     text2=sr(oans.lower())
     print(text1)
     print(text2)

     vector1=text_to_vector(str(text1))
     vector2=text_to_vector(text2)

     cosine=get_cosine(vector1,vector2)
     print ('Cosine:', cosine)
          #omark = cosine * 10
     return cosine

#///////////////////////////////////////////////////////////////////////////////////
     # text1 = ans
     # text2 = oans

     # vector1 = text_to_vector(text1)
     # vector2 = text_to_vector(text2)

     # cosine = get_cosine(vector1, vector2)

     # print ('Cosine:', cosine)
     # omark = cosine * 10

     # return cosine