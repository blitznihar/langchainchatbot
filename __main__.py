from chatbot import openaichain

def chat(humanCommand):
    return openaichain.chat(humanCommand)

continuechat = True
while continuechat:
    humanCommand = input('>>')
    if humanCommand.lower() == "exit":
        continuechat = False
    else:
        result = chat(humanCommand)
        print(result)