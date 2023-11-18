# app/__init__.py
# app/__init__.py
from flask import Flask
import schedule
from threading import Thread

import time
import csv
import re
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
# from datasets import load_dataset
import json
from transformers import AutoTokenizer, AutoModelForCausalLM




def task():
    #     {
    #   "instruction": "Detect the sentiment of the tweet.",
    #   "input": "Positive",
    #   "output": "@p0nd3ea Bitcoin wasn't built to live on exchanges."
    # }

    def get_model_tokenizer():
        BASE_MODEL = "llama-2-7b-chat.Q2_K.gguf"
        
 
        tokenizer = AutoTokenizer.from_pretrained("TheBloke/Llama-2-7B-Chat-AWQ")
        model = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-Chat-AWQ", load_in_8bit=False)

        return model , tokenizer


    def preprocess(row):
        slogan  , mode , level, keywords = row
        slogan = re.sub(r'\d+\.', '', slogan).replace("\"" , "")


        if mode == "creativity":
            instruction = "Generate a slogan with creativity based on input for a marketing campaign based on the following keywords : " + keywords
        elif mode == "style":
            instruction = "Generate a slogan with style based on input for a marketing campaign based on the following keywords : " + keywords
        else:
            instruction = "Generate a slogan with tone for a marketing campaign based on the following keywords : " + keywords


        return {
            "instruction" : instruction,
            "input": level,
            "output": slogan
        }

    def generate_prompt(data_point):
        return f"""Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.  # noqa: E501
            ### Instruction:
            {data_point["instruction"]}
            ### Input:
            {data_point["input"]}
            ### Response:
            {data_point["output"]}"""
 
 
    def tokenize(prompt, add_eos_token=True):
        result = tokenizer(
            prompt,
            truncation=True,
            max_length=CUTOFF_LEN,
            padding=False,
            return_tensors=None,
        )
        if (
            result["input_ids"][-1] != tokenizer.eos_token_id
            and len(result["input_ids"]) < CUTOFF_LEN
            and add_eos_token
        ):
            result["input_ids"].append(tokenizer.eos_token_id)
            result["attention_mask"].append(1)
    
        result["labels"] = result["input_ids"].copy()
    
        return result
    
    def generate_and_tokenize_prompt(data_point):
        full_prompt = generate_prompt(data_point)
        tokenized_full_prompt = tokenize(full_prompt)
        return tokenized_full_prompt

    # File path
    file_path = 'your_file.csv'
    model , tokenizer = get_model_tokenizer()


    data = []
    # Open the CSV file and read its contents
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        
        # Iterate through each row in the CSV file
        for row in reader:
            # Each row is a list representing the columns in that row
            data.append(preprocess(row))


    train_data = (
        data.map(generate_and_tokenize_prompt)
    )



    print(f"Training data size {len(train_data)}")




# Scheduler function
def run_scheduler():
    # Schedule the task to run every 10 seconds
    schedule.every(10* 1000).seconds.do(task)
    while True:
        schedule.run_pending()
        time.sleep(1)



# Start the scheduler in a separate thread when the Flask app starts
# scheduler_thread = Thread(target=run_scheduler)
# scheduler_thread.start()

task()

app = Flask(__name__)
from app.main.controller.routes import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')
