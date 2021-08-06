from GPTJ.gptj_api import Completion

context = "This is a conversation with a murder suspect named roy on a train to the moon. Roy did not commit the murder of victoria, but he did know her.  He recently had a falling out with her as she started working for big pharma, turning down his offer of joining his business of selling insulin for cheap. Roy would never murder her though. Roy is a guard on the train, but he left his post on the night of the murder to get his insulin supply."

examples = {"Detective: Hello.  I am investigating the murder of Victoria Timbers, as you already know.  Please state your name. ": "Roy: My name is Roy."}

while True:
    context_setting = Completion(context, examples)
    #print(context_setting)
    prompt = input("Detective: ") + "Roy: "

    User = "Detective: "

    Bot = "Roy: "

    max_tokens = 150

    temperature = 0.7

    top_probability = 1.0

    response = context_setting.completion(prompt,
                                        user=User,
                                        bot=Bot,
                                        max_tokens=max_tokens,
                                        temperature=temperature,
                                        top_p=top_probability)

    print("Roy: "+response[0:response.lower().find("detective: ")])
    print(examples)
    examples["Detective: "+prompt[0:-5]] = "Roy: "+response[0:response.lower().find("detective: ")]
