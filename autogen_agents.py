import os
import autogen

os.environ['AUTOGEN_USE_DOCKER'] = "None"
os.environ["OPENAI_API_KEY"] = "openai_api_key"

config_list = [
    {
        "model": "gpt-3.5-turbo",
        "api_key": os.environ["OPENAI_API_KEY"],
    }
]

user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human user seeking property investment advice.",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=1,
)

property_analyst = autogen.AssistantAgent(
    name="Property_Analyst",
    system_message="You are a property investment analyst. Provide analysis based on market trends and data.",
    llm_config={"config_list": config_list},
    max_consecutive_auto_reply=1,
)

financial_advisor = autogen.AssistantAgent(
    name="Financial_Advisor",
    system_message="You are a financial advisor specializing in property investments. Provide financial advice and investment strategies.",
    llm_config={"config_list": config_list},
    max_consecutive_auto_reply=1,
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, property_analyst, financial_advisor],
    messages=[],
    max_round=5,
)

manager = autogen.GroupChatManager(groupchat=groupchat)
