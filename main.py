from openai 
import time
import pyttsx3
from PyPDF2 import PdfReader
#import functools

openai.api_key = os.environ["OPENAI_API_KEY"]

'''
def extract_text_from_pdf(filename:str)->str: extract text from pdf 
def split_text(text:str)->list[str]: split text in chunks
def genrate_summary(text:str, model="gpt-3.5-turbo")->list[str]: send request to gpt to get summary back 
def text_to_speech(summary:str)->None: text to speech.
filepath="" path of pdf file whose summary you want
'''

def extract_text_from_pdf(filename:str)->str:
   text=''
   with open(filename,'rb') as file:
      pdf_reader = PdfReader(file)
      for page_num in range(len(pdf_reader.pages)):
         page = pdf_reader.pages[page_num]
         text += page.extract_text()
   return text.replace('\t\r','').replace('\xa0','')


def split_text(text:str)->list[str]:
   max_chunk_size = 2048
   chunks = []
   current_chunk = ""
   for sentence in text.split("."):
      if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
      else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
   if current_chunk:
      chunks.append(current_chunk.strip())
   return chunks



#@functools.lru_cache(maxsize=1024)
def generate_summary(text:str) -> str:
    input_chunks = split_text(text)
    output_chunks = []
    for i , chunk in enumerate(input_chunks):
        response = openai.Completion.create(
            engine="davinci",
            prompt = f"Please summarize the following paragraph ({i + 1}):\n{chunk}\n\nSummary:"
            temperature=0.5,
            max_tokens=1024,
            n = 1,
            stop=None
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
    return " ".join(output_chunks)



def text_to_speech(summary:str)->None:
   speaker=pyttsx3.init()
   voices = speaker.getProperty('voice')
   speaker.setProperty('voice', voices) #changing index changes voices but ony 0 and 1 are working here
   speaker.setProperty('rate', 160)    # Speed percent (can go over 100)
   speaker.setProperty('volume', 0.5)
   speaker.say(summary)
   time.sleep(0.2)
   speaker.runAndWait()
   return None
   
   
filepath="sample.pdf"
# extracted text from pdf file
text=extract_text_from_pdf(filepath)
#genrated summary using third party openai library name g4f
summary=genrate_summary(text)
speak_text="".join(summary)
#now pass the genrated summary to speech to text 
text_to_speech(speak_text)


