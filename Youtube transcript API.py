#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The easiest way to get a transcript for a given video is to execute: Recuerda solo se pone el video ID, no el URL completo del video

from youtube_transcript_api import YouTubeTranscriptApi

YouTubeTranscriptApi.get_transcript('GeyDf4ooPdo')


# In[ ]:


# Si el video está dentro de una lista de prepoducción https://www.youtube.com/watch?v=N_KYcCWHg6Q&list=PLhkHcc7EKtBbgJm27Q_ghvqL7LUFBindr&index=1

#el ID del video se encuentra inmediatamente después de watch?v=N_KYcCWHg6Q y antes de &list=


# In[3]:


#If you want to list all transcripts which are available for a given video you can call:

transcript_list = YouTubeTranscriptApi.list_transcripts('GeyDf4ooPdo')

print(transcript_list)


# In[4]:


#el string se hace con corchetes (corrección)...en realidad lo que he hecho es una lista...
from youtube_transcript_api import YouTubeTranscriptApi

video_ids = ['GeyDf4ooPdo', 'tLMpdBjA2SU']
YouTubeTranscriptApi.get_transcripts(video_ids)


# In[ ]:


#Ejemplo de uso con el video 'El nuevo coronavirus de Wuhan: atrapados en el centro del virus' de la Vanguardia
# Al encontrase dentro de una lista de reproducción el ID se encuentra inmediatamente después del primer = 
# y hasta justo antes de &list #


# In[1]:


from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi.list_transcripts('N_KYcCWHg6Q')

print(transcript_list)


# In[7]:


transcript = transcript_list.find_transcript(['es'])

print(transcript)


# In[8]:


transcript.fetch()


# In[2]:


YouTubeTranscriptApi.get_transcript('N_KYcCWHg6Q', languages=['es'])


# In[1]:


from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

transcript = YouTubeTranscriptApi.get_transcript('0_4KEb08xrE', languages=['en'])

formatter = TextFormatter()

print(formatter)

TextFormatter = formatter.format_transcript(transcript)

with open('D:your_filename.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(TextFormatter)



# In[2]:


print(transcript)


# In[5]:


from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

transcript2 = YouTubeTranscriptApi.get_transcript('N_KYcCWHg6Q', languages=['es'])

formatter = JSONFormatter()

JSONFormatter = formatter.format_transcript(transcript2)

with open('your_filename.json', 'w', encoding='utf-8') as json_file:
    json_file.write(JSONFormatter)


# In[6]:


print(transcript2)


# In[ ]:


# This code uses an undocumented part of the YouTube API, which is called by the YouTube web-client.
#So there is no guarantee that it won't stop working tomorrow, if they change how things work.
#I will however do my best to make things working again as soon as possible if that happens.
#So if it stops working, let me know!

