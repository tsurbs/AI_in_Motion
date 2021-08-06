import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"

promptxt = "This is a conversation with a murder suspect named roy on a train to the moon. Roy did not commit the murder of victoria, but he did know her.  He recently had a falling out with her as she started working for big pharma, turning down his offer of joining his business of selling insulin for cheap. Roy would never murder her though. Roy is a guard on the train, but he left his post on the night of the murder to get his insulin supply. \n Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. \n Roy: My name is Roy. "
ogpmptxtlen = len(promptxt)
print("Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. \n Roy: My name is Roy.")

while True:

    user_in = input("Detective: ")
    if user_in == "exit": print(promptxt)
    promptxt += "\n Detective: " + user_in + "\n Roy: "
    #print(promptxt)

    response = openai.Completion.create(
    engine="davinci",
    prompt=promptxt,
    temperature=0.6,
    max_tokens=150,
    top_p=1,
    frequency_penalty=.1,
    presence_penalty=0.6,
    stop=["\n", " Detective: ", " Roy: "]
    )

    txtresp = str(response["choices"][0]["text"])#.replace("\xa0", "")
    #print(response)
    print("Roy: "+txtresp)

    promptxt += txtresp

    if len(promptxt)>2000: 
        n=2
        while promptxt.replace('Detective: ', 'XXX', n).find('Detective: ')-ogpmptxtlen<(len(promptxt)-2000) or promptxt.replace('Detective: ', 'XXX', n).find('Detective: ') == -1:
            n+=1

        promptxt = promptxt[0:ogpmptxtlen]+promptxt[promptxt.replace('Detective: ', 'XXX', n).find('Detective: ')-2]
