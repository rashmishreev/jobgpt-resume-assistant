# jobgpt-resume-assistant
Fine-tune ChatGPT with few-shot learning for personalized resume bullet points. 

I initiated this project in response to the challenges in the job market and the growing importance of tailoring resumes to specific job requirements. Inspired by the increasing use of Large Language Models, especially their fine-tuning for specific purposes, I decided to experiment with few-shot fine-tuning GPT 3.5 turbo to create a system that streamlines the process of customizing resumes for job descriptions.

### Analyzing Successful Examples and Crafting Impactful Bullet Points
The initial phase involved reviewing successful resumes on platforms like LinkedIn, including those of classmates and alumni, to identify effective formats and content. Subsequently, these selected resumes, along with a guide on crafting impactful resume bullet points, such as the one provided by [Columbia University](https://www.careereducation.columbia.edu/resources/resumes-impact-creating-strong-bullet-points), were used to create a guideline for fine-tuning the model for generating bullet points.

### Data Preparation and Model Training: Crafting Conversations for Real-World Simulation
In the following stage, a dataset with prompt-answer pairs was compiled for training the model, guided by OpenAI's [documentation](https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset). This involved crafting diverse conversations to simulate real-world scenarios the model might encounter in production. Job descriptions from LinkedIn were utilized, employing the STAR method to tailor robust bullet points for each role. Additionally, ChatGPT 3.5, with descriptive prompts, was used to generate extra bullet points.

https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset
