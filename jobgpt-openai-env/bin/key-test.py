#!/Users/sanjay/Documents/GitHub/jobgpt-resume-assistant/jobgpt-openai-env/bin/python
# from openai import OpenAI
# import os

# #client = OpenAI()
# # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("OPENAI_API_KEY_JOBGPT"),
# )


from openai import OpenAI
client = OpenAI()

file_list = client.files.list()
print(file_list, sep= "\n")
