import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"


promptxt = "This is a conversation with a murder suspect named LT, AKA Luke Jones. LT will hide the fact that he committed the murder of the warden victoria unless presented with contradicting evidence.  His alibi is that he was unconscious from drinking too much tea. The detective and him are currently on a prison ship going to the moon because he hacked into the pentagon. He did it because he needed to show everyone the truth that we live in a simulation. \n Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. \n LT: My name is Luke Jones, or LT, but this is actually just the matrix, so who cares. \n Detective: Did you kill Victoria Timbers? \n LT: No.  I was unconscious at the time, having had too much tea."
ogpmptxtlen = len(promptxt)
print("Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. \n LT: My name is Luke Jones, or LT, but this is actually just the matrix, so who cares. \n Detective: Did you kill Victoria Timbers? \n LT: No.  I was unconscious at the time, having had too much tea.")

while True:

    user_in = input("Detective: ")
    promptxt += "\n Detective: " + user_in + "\n LT: "
    # print(promptxt)

    response = openai.Completion.create(
        engine="davinci",
        prompt=promptxt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Detective: ", " LT: "]
    )

    txtresp = str(response["choices"][0]["text"]).replace("\xa0", "")
    # print(response)
    if txtresp != "":
        # print(response)
        print("LT: "+txtresp)

        promptxt += txtresp

        if len(promptxt) > 2000:
            n = 2
            while promptxt.replace('Detective: ', 'XXX', n).find('Detective: ')-ogpmptxtlen < (len(promptxt)-2000) or promptxt.replace('Detective: ', 'XXX', n).find('Detective: ') == -1:
                n += 1

            promptxt = promptxt[0:ogpmptxtlen] + \
                promptxt[promptxt.replace(
                    'Detective: ', 'XXX', n).find('Detective: ')-2]
