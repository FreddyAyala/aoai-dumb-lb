import requests
import itertools
import random
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import ConversationChain

endpoints = [
    {"url": "https://aoai-test-lb-01.openai.azure.com/", "deployment_name": "gpt-4-32k", "api_key": ""},
    {"url": "https://aoai-test-lb-02.openai.azure.com/", "deployment_name": "gpt-4-32k", "api_key": ""}
    # add more endpoints, deployment_names and api_keys
]

# Randomize the order of the endpoints
random.shuffle(endpoints)

def send_request(endpoint, deployment_name, api_key, prompt):
    chat = AzureChatOpenAI(
        openai_api_key=api_key,
        openai_api_base=endpoint,
        openai_api_version="2023-07-01-preview",
        deployment_name=deployment_name,
        max_tokens=100,
        temperature=0.3
    )

    conversation = ConversationChain(llm=chat)
    response = conversation.predict(input=prompt)
    return response

def send_request_to_random_endpoint(endpoints, prompt, max_retries=6):
    cycle_endpoints = itertools.cycle(endpoints)
    for _ in range(max_retries):
        endpoint = next(cycle_endpoints)
        try:
            print(endpoint["url"])
            response = send_request(endpoint["url"], endpoint["deployment_name"], endpoint["api_key"], prompt)
            raise Exception("Simulated exception")
            return response
        except Exception as e:
            print(f"An error occurred: {str(e)}. Retrying...")
    return None

prompts = [
    "What is the difference between OpenAI and Azure OpenAI?",
    "What are other LLMs?",
    "Which LLM is the best?",
    "Which LLM is the best4?",
    "Which LLM is the best?5"
]

for prompt in prompts:
    response = send_request_to_random_endpoint(endpoints, prompt)
    if response is not None:
        print(response)
    else:
        print(f"All requests for prompt '{prompt}' failed.")