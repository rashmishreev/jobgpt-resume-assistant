import sys
sys.path.append('path-to-python-3')

from openai import OpenAI
#client = OpenAI()

client = OpenAI(api_key='SECRET-API-KEY')

                  
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)

# file_list = client.files.list()
# print(file_list, sep= "\n")

# from openai import OpenAI

# client.fine_tuning.jobs.create(
#   training_file="file-PwqRr97KhgP74WLDQnqwpPoM",
#   validation_file="file-1CEdzpUBIGiosGm1cr4lQS6K",
#   model="gpt-3.5-turbo"
# )

 #List 10 fine-tuning jobs
# jobs = client.fine_tuning.jobs.list(limit=10)
# print(jobs)

# Delete a fine-tuned model (must be an owner of the org the model was created in)
#client.models.delete("ft:gpt-3.5-turbo-0613:personal::8RmuSjGY")


# content = client.files.retrieve_content("file-5zK6ikFfpCxnkgsL8cX6EpsQ")
# print(content)


# Assuming client.fine_tuning.jobs.list_events() returns a list of events
events = client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-cdjtCSRVA1XewcEF5dNw3AMk", limit=2)

# Print the obtained events
for event in events:
    print(event)

