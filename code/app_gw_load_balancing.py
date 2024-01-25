from azure.identity import InteractiveBrowserCredential
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import ConversationChain

# Replace these with your actual values
tenant_id = ",your tenant id"
api_base ="http://4.157.241.196/"
deployment_name = "gpt-35-turbo"

# Managed identites authentication
credential = InteractiveBrowserCredential(tenant_id=tenant_id)
token = credential.get_token("https://cognitiveservices.azure.com/.default")
print(token.token)

chat = AzureChatOpenAI(
    openai_api_type="azure_ad",
    openai_api_key=token.token,
    openai_api_base=api_base,
    openai_api_version="2023-07-01-preview",
    deployment_name=deployment_name,
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