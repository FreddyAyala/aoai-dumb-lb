from azure.identity import InteractiveBrowserCredential
# Replace these with your actual values
tenant_id = "dea6f2e5-c64a-4e29-8a83-5f1eb4136640"
#client_id = "68468802-fb57-4e2e-8310-b3b95fab1490"

credential = InteractiveBrowserCredential(tenant_id=tenant_id)

token = credential.get_token("https://cognitiveservices.azure.com/.default")
print(token.token)
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import ConversationChain

chat = AzureChatOpenAI(
    openai_api_type="azure_ad",
    openai_api_key=token.token,
    openai_api_base="http://20.220.107.45/",
    openai_api_version="2023-07-01-preview",
    deployment_name="gpt-4-32k",
    max_tokens=100,
    temperature=0.3
)

conversation = ConversationChain(llm=chat)

response1 = conversation.predict(input="What is the difference between OpenAI and Azure OpenAI?")
response2 = conversation.predict(input="What are other LLMs?")
response3 = conversation.predict(input="Which LLM is the best?")
response3 = conversation.predict(input="Which LLM is the best4?")
response3 = conversation.predict(input="Which LLM is the best?5")
print(response1 + "\n" + response2 + "\n" + response3)