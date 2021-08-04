import os
import openai
import sys

# Load your API key from an environment variable or secret management service
openai.api_key = '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'

print("resp")
#promptxt = sys.argv[1]
promptxt = "Hello, my name is"

ogpmptxtlen = len(promptxt)
#print("\n Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. \n Jonathan: My name is Jonathan. Can I help you investigate?... I'm quite good! \n Detective: Did you kill Victoria Timbers? \n Jonathan: No. You can check with roy, my guard.  He was watching me.")

if len(promptxt) > 2000:
            n = 2
            while promptxt.replace('Detective: ', 'XXX', n).find('Detective: ')-ogpmptxtlen < (len(promptxt)-2000) or promptxt.replace('Detective: ', 'XXX', n).find('Detective: ') == -1:
                n += 1

            promptxt = promptxt[0:ogpmptxtlen] + \
                promptxt[promptxt.replace(
                    'Detective: ', 'XXX', n).find('Detective: ')-2]
# print(promptxt)

response = openai.Completion.create(
    engine="davinci",
    prompt=promptxt,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["\n", "Detective: ", sys.argv[2]]
)

txtresp = str(response["choices"][0]["text"]).replace("\xa0", "")
print(txtresp)