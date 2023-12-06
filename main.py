import g4f
import os
from curl_cffi.requests import AsyncSession
import asyncio

isStart = True

# Can get from browser
cookie = ""


def Chat_GPT(demande):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        # provider=g4f.Provider.DeepAi,
        provider=g4f.Provider.Acytoo,
        # model=g4f.models.gpt_35_turbo,
        # provider=g4f.Provider.OpenaiChat,
        messages=[{"role": "user", "content": demande}],
        # cookies={"__Secure-next-auth.session-token": cookie},
        # auth=True,
    )
    print("Chat_GPT :")
    print(response)
    
    # Write prompt to file
    with open("prompt.md", "w") as file:
        file.write(response)

######################### MAIN ###########################

# while isStart == True:
#     correctResponse = False
#     print(
#         """#############################################
#     ____  ____  ____  ____        ___  ____  ____
# (  __)(  _ \(  __)(  __)      / __)(  _ \(_  _)
#     ) _)  )   / ) _)  ) _)  ____( (_ \ ) __/  )(
# (__)  (__\_)(____)(____)(____)\___/(__)   (__)

# #################################################
# """
#     )
#     print("You :")
#     question = input()

#     if question == "quit()":
#         isStart = False
#         break
#     Chat_GPT(question)


with open("prompt.txt", "r") as file:
    file_content = file.read()
    Chat_GPT(file_content)
