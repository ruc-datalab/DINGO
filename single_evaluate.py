import os
import json
import argparse
import requests
from tqdm import tqdm
import openai
from template import single_score_template
import re

system_message = "You are a helpful assistant."

def get_target_files(target_set, model_name):
    """
    This function aims to find all data.json files from a multi-level folder
    """
    if target_set == 'all':
        folder = f'data/{model_name}'
    else:
        folder = os.path.join(f'data/{model_name}/', target_set)
    target_files = []
    for root, _, files in os.walk(folder):
        if 'data.json' in files:
            target_files.append(os.path.join(root, 'data.json'))
    return target_files

def single_evaluate(target_set, model_name):
    # 1. Get data
    target_files = get_target_files(target_set, model_name)

    # 2. Evalute
    for file in target_files:
        scores = []
        data = json.load(open(file))
        print(f"scoring {len(data)} samples in {file} ...")
        for idx in tqdm(range(len(data))):
            score = single_scoring_function(data[idx], file)
            data[idx]['score'] = score
            scores.append(score)
        avg_score = sum(scores)/len(scores)
        print(f"average score = {avg_score}")

        # 3. Write result
        with open(file.replace('data.json', 'score.text'), 'a') as f:
            f.write(str({"single evluate score (avg)": avg_score}))
            f.write("\n")
        
        json.dump(data, open(file, 'w'), indent=4)

def score_parser(text):
    """
    This function aims to extract the answer from a string using regular expressions, such as [[12]] ->12
    """
    pattern = r'\[\[(.*?)\]\]'
    matches = re.findall(pattern, text)
    return int(matches[0])

def single_scoring_function(sample, category):
    # 1. Find the category
    for key in ["Code", "Creation", "Knowledge Utilization", "Language Generation", "Language Understanding", "Mathematics and Reasoning"]:
        if f'/{key}/' in category:
            category = key
            break
    
    # 2. Buiding conversation
    conversation = ''
    for conv in sample['conversations']:
        role = conv['from']
        sentence = conv['value']
        conversation += f"{role}: {sentence}\n"

    # 3. Get the scoring prompt
    if sample['reference_answer'] != '':
        category += ' (with reference answer)'
        score_template = single_score_template[category]
        prompt = score_template.format(conversation=conversation, ref_question=sample['basic_question'], ref_answer=sample['reference_answer'])
    else:
        score_template = single_score_template[category]
        prompt = score_template.format(conversation=conversation)

    messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    
    # 4. Call gpt-4
    # response = openai.chat.completions.create(
    #         model='gpt-4-0125-preview',
    #         messages=messages,
    #         stop = ["\n"],
    #         temperature = 0,
    #         max_tokens = 200,
    #     )
    response = '[[10]]'

    # 5. Parse the answer
    score = score_parser(response)

    return score

if __name__ == "__main__":
    # 1. Create argument parser
    parser = argparse.ArgumentParser(description='Score model predictions')
    parser.add_argument('--model_name', type=str, help='Name of the model')
    parser.add_argument('--api_key', type=str, help='API key for the scoring function')
    parser.add_argument('--target_set', default='all', type=str, help='The set you want to evaluate, e.g., \"Mathematics and Reasoning/Applied Problems\"')
    args = parser.parse_args()
    
    # 2. Set openai config
    openai.api_key = args.api_key

    # 3. Call function to score model predictions
    single_evaluate(args.target_set, args.model_name)
