import sys
sys.path.append('path-to-python-3')

from openai import OpenAI
#client = OpenAI()

client = OpenAI(api_key='SECRET-API-KEY')

response = client.chat.completions.create(
  #model="ft:gpt-3.5-turbo-0613:personal::8RmuSjGY",
  model="ft:gpt-3.5-turbo-0613:personal::8RoHogRu",
  messages=[
    {"role": "system", "content": "You are an exceptional resume writer and enhancer who helps people write, modify, or tailor their resumes for a specific job description."},
    {"role": "user", "content": "Please provide a bullet point for my resume based on the given job description. Include an action verb that demonstrates an accomplishment, quantify the impact, and showcase the skills you acquired or utilized during your work. Here is the job desciption: As a Data Analyst at Mammoth Growth, you will leverage analytics to create data analysis strategies, track and report performance, and influence strategic decisions, improving marketing tactics and overall customer experience for our clients.\n\nWhat You'll Do:\n- Manage core analyst consulting projects with our high growth and fast-paced clients\n- Manipulate and analyze various types of data across multiple platforms to solve problems and identify opportunities\n- Monitor the integrity and validity of the data reported\n- Meet with clients weekly to document and make recommendations on key questions and business metrics and present findings\n- Complete critical analysis that will drive growth for our clients\n- Work independently but also be a valued member of a cross-functional team\n- Explore new data sources and regularly become certified in cutting-edge data tools\n\nWhat You'll Need:\n- Ability to perform in-depth analyses in a variety of analytics tools (Excel, Amplitude, Segment, Looker)\n- 1-3+ years of cross-functional analytics experience, preferably in marketing\n- Ideally, you have completed an Undergraduate or Master's Degree in Business, Econ, Marketing, Mathematics, Finance, Data Analytics or other quantitative field (relevant experience or data bootcamp certification will be considered)\n- You have some experience with query languages (SQL, Python)\n- You are smart, intellectually curious, fiercely independent and driven\n- Excellent communication (written and verbal) and interpersonal skills\n- You are a great teammate that loves to have fun at work and contribute with your experience and positive attitude\n- Prior experience clearly explaining technical concepts to varied audiencesX"}
  ]
)
print(response.choices[0].message)