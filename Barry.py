import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


promptxt = "This is a conversation between a detective and an insane murder suspect named Jonathan. Jonathan did not murder the warden victoria. His alibi for victoria’s murder is that Roy, his guard, was watching him. Although he didn’t kill Victoria, he did kill his coworker Johnny. He killed Johnny because Johnny didn't understand him. Because he was convicted of johnny’s murder, he is now on a train to the moon.  This train is where the murder of victoria was committed. \n Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. \n Jonathan: My name is Jonathan. Can I help you investigate?... I'm quite good! \n Detective: Did you kill Victoria Timbers? \n Jonathan: No. You can check with roy, my guard.  He was watching me."
ogpmptxtlen = len(promptxt)
print("\n Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. \n Jonathan: My name is Jonathan. Can I help you investigate?... I'm quite good! \n Detective: Did you kill Victoria Timbers? \n Jonathan: No. You can check with roy, my guard.  He was watching me.")

while True:

    user_in = input("Detective: ")
    promptxt += "\n Detective: " + user_in + "\n Jonathan: "
    # print(promptxt)

    response = openai.Completion.create(
        engine="davinci",
        prompt=promptxt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Detective: ", " Jonathan: "]
    )

    txtresp = str(response["choices"][0]["text"]).replace("\xa0", "")
    #txtresp = ''.join([i for i in txtresp if i.isalnum() or i ==" "])
    # print(response)
    if txtresp != "":
        # print(response)
        print("Jonathan: "+txtresp)

        promptxt += txtresp

        if len(promptxt) > 2000:
            n = 2
            while promptxt.replace('Detective: ', 'XXX', n).find('Detective: ')-ogpmptxtlen < (len(promptxt)-2000) or promptxt.replace('Detective: ', 'XXX', n).find('Detective: ') == -1:
                n += 1

            promptxt = promptxt[0:ogpmptxtlen]+promptxt[promptxt.replace(
                'Detective: ', 'XXX', n).find('Detective: ')-2]
