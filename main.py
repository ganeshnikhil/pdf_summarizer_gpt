import g4f #free version of openai thrid party downloaded software 
import time
import pyttsx3
from PyPDF2 import PdfReader
'''
it convert pdf to a summarized audio .
def extract_text_from_pdf(filename): to extract text from pdf. 
def split_text(text): split text in chunks 
def genrate_summary(text, model="gpt-3.5-turbo"): genrate summary using gpt
def text_to_speech(summary): text to speech . audio of genrated summary
'''
def extract_text_from_pdf(filename):
   text=''
   with open(filename,'rb') as file:
      pdf_reader = PdfReader(file)
      for page_num in range(len(pdf_reader.pages)):
         page = pdf_reader.pages[page_num]
         text += page.extract_text()
   return text.replace('\t\r','').replace('\xa0','')


def split_text(text):
   max_chunk_size = 1024
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




def genrate_summary(text, model="gpt-3.5-turbo"):
   input_chunks=split_text(text)
   output_chunks=[]
   for chunk in input_chunks:
      prompt=f"Please summarize the following text:\n{chunk}\n\nSummary:"
      
      messages = [{"role": "user", "content": prompt}]
      response = g4f.ChatCompletion.create(
         model=model,
         messages=messages,
         stream=True,
      )
      textify="".join([message for message in response])
      output_chunks.append(textify)
      time.sleep(0.1)
   return output_chunks



def text_to_speech(summary):
   speaker=pyttsx3.init()
   voices = speaker.getProperty('voice')
   speaker.setProperty('voice', voices) #changing index changes voices but ony 0 and 1 are working here
   speaker.setProperty('rate', 160)    # Speed percent (can go over 100)
   speaker.setProperty('volume', 0.5)
   speaker.say(summary)
   time.sleep(0.2)
   speaker.runAndWait()
   
   
filename="sample.pdf"
# extracted text from pdf file
text=extract_text_from_pdf(filename)
#genrated summary using third party openai library name g4f
summary=genrate_summary(text)
speak_text="".join(summary)

#now pass the genrated summary to speech to text 
text_to_speech(speak_text)


