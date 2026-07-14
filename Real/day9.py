from openai import OpenAI


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="OPENAI_API_KEY"
)
# Introduction to templates---------------------------
# template = "My name is {name} and I'm {age} years old."
# final_words =template.format(name="Hadi", age ="16")
# print (final_words)
# or, more practically:
# user_template = "<user_message>{message}</user_message>"
# final_message = user_template.format(message= "Hello World")
# print (final_message)
#-----------------------------------------------------
system_template = "You are a {role} and your job is {work}"
agent_role = "Book info fetcher"
agent_work = "fetch book summaries along with author names"
system_formatted = system_template.format(role=agent_role, work = agent_work)

history = [
    {"role" : "system", "content" : system_formatted}
]
user_template = "<user_message>{message}</user_message>"
print("♥♥♥ Day9 agent online... Fire away any queries below ♥♥♥ ")
while True:
    user_input = input("Ask anything: ")
    
    if user_input.lower() == 'exit':
        print("Disconnecting Agent... ")
        break
    
    user_message_final = user_template.format(message = user_input)
    history.append({"role" : "user", "content" : user_message_final})
    
    response = client.chat.completions.create(
        model = "openrouter/free",
        messages=history
    )
    final_response = response.choices[0].message.content
    print(f"\n AI Response: {final_response} \n")
    history.append({"role" : "assistant", "content" : final_response})
    