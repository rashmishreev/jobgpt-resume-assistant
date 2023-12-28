# jobgpt-resume-assistant
Fine-tune ChatGPT with few-shot learning for personalized resume bullet points. 

I initiated this project in response to the challenges in the job market and the growing importance of tailoring resumes to specific job requirements. Inspired by the increasing use of Large Language Models, especially their fine-tuning for specific purposes, I decided to experiment with few-shot fine-tuning GPT 3.5 turbo to create a system that streamlines the process of customizing resumes for job descriptions.

### 1. Analyzing Successful Examples and Crafting Impactful Bullet Points
The initial phase involved reviewing successful resumes on platforms like LinkedIn, including those of classmates and alumni, to identify effective formats and content. Subsequently, these selected resumes, along with a guide on crafting impactful resume bullet points, such as the one provided by [Columbia University](https://www.careereducation.columbia.edu/resources/resumes-impact-creating-strong-bullet-points), were used to create a guideline for fine-tuning the model for generating bullet points.

### 2. Data Preparation
In the following stage, a dataset with prompt-answer pairs was compiled for training the model, guided by OpenAI's [documentation](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset). This involved crafting diverse conversations to simulate real-world scenarios the model might encounter in production. Job descriptions from LinkedIn were utilized, employing the STAR method to tailor robust bullet points for each role. Additionally, ChatGPT 3.5, with descriptive prompts, was used to generate extra bullet points. The final dataset, stored in the ['prompt-answer-pairs.jsonl'](https://github.com/rashmishreev/jobgpt-resume-assistant/blob/main/prompt-answer-pairs.jsonl), was developed and utilized for fine-tuning the model.
<img align="center" src="https://github.com/rashmishreev/jobgpt-resume-assistant/blob/main/Images/image.png"> 

### 3. The project flow is outlined below:
<img align="center" width="500" height="500" src="https://github.com/rashmishreev/jobgpt-resume-assistant/blob/main/Images/architecture.png"> 

### 4. Fine-Tuned Model Output and Experiment Insights
The results from the fine-tuned model are as follows. Despite a limited fine-tuning dataset, the model performed well with few-shot examples. Opportunities for improvement include enhancing dataset diversity, creating a user interface, etc. It's important to note that this was a small-scale experiment.
<img align="center" src="https://github.com/rashmishreev/jobgpt-resume-assistant/blob/main/Images/finetuning-output.png"> 
