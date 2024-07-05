import openai
import os

os.environ["OPENAI_API_KEY"] = "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"
client = openai.OpenAI()

def chat_API():
    """ This function calls up an interactive chat with the chatGPT API. """    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        prompt = user_input
        
        print(get_completion(prompt))

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    
    """ Basic API call to the gpt-3.5-turbo model. """
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
        ]
    response = client.chat.completions.create(model=model,
                                              messages=messages,
                                              temperature=temperature
                                              )
    return response.choices[0].message.content

def query_index():
    pass

def create_short_summary(prompt, model="gpt-3.5-turbo", temperature = 0.2):
    
    """ This is an API call that creates a short summary of a text that is only one or two sentences long. """
    
    messages = [
    {"role": "system", "content": "You summarize texts in a very concise,  but effective manner. You do not write more than one or two sentences. You do not use more than 50 words at most."},
    {"role": "user", "content": prompt},
    ]
    summary = client.chat.completions.create(model=model,
                                              messages=messages,
                                              temperature=temperature
                                              )
    
    return summary.choices[0].message.content


def create_ner(prompt, model="gpt-3.5-turbo", temperature=0):
    
    """ This is an API call that performs named entity recognition on a text. """
    
    messages = [
    {"role": "system", "content": "You perform named entity recognition on a text. You must only list the named entities within the given text. Write them in only one line, separated by commas."},
    {"role": "user", "content": prompt},
    ]
    named_entities = client.chat.completions.create(model=model,
                                              messages=messages,
                                              temperature=0
                                              )
    return named_entities.choices[0].message.content

def create_keywords(prompt, model="gpt-3.5-turbo", temperature=0.1):
    
    """ This is an API call that creates keywords from the most important words in a text. """
    
    messages = [
    {"role": "system", "content": "You create keywords for the most important topics within the text. You must not create more than 10 keywords. For short texts create only 5 keywords. For bigger texts you may use more, but never more than 10 keywords. Write them in only one line, separated by commas."},
    {"role": "user", "content": prompt},
    ]
    keywords = client.chat.completions.create(model=model,
                                              messages=messages,
                                              temperature=temperature
                                              )
    return keywords.choices[0].message.content

