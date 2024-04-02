import os
import json
import argparse
import requests
from tqdm import tqdm
import openai
from template import pairwise_score_template
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

def pairwise_evaluate(target_set, modelA_name, modelB_name):
    # 1. Get data
    target_files = get_target_files(target_set, modelA_name)

    # 2. Evalute
    for file_A in target_files:
        scores_A = []
        scores_B = []
        data_A = json.load(open(file_A))
        file_B = file_A.replace(modelA_name, modelB_name)
        data_B = json.load(open(file_B))
        print(f"scoring {len(data_A)} samples in {file_A} and {file_B} ...")
        assert len(data_A) == len(data_B), "The number of samples for both models must be the same"
        for idx in tqdm(range(len(data_A))):
            result = single_scoring_function(data_A[idx], data_B[idx], file_A)
            if result == 'A':
                data_A[idx][f'compared to {modelB_name}'] = 'win'
                data_B[idx][f'compared to {modelA_name}'] = 'lose'
            elif result == 'B':
                data_A[idx][f'compared to {modelB_name}'] = 'lose'
                data_B[idx][f'compared to {modelA_name}'] = 'win'
            elif result == 'C':
                data_A[idx][f'compared to {modelB_name}'] = 'tie'
                data_B[idx][f'compared to {modelA_name}'] = 'tie'

            scores_A.append(result == 'A')
            scores_B.append(result == 'B')

        avg_score_A = sum(scores_A)/len(scores_A)
        avg_score_B = sum(scores_B)/len(scores_B)
        print(f"win rate of {modelA_name} = {avg_score_A}")
        print(f"win rate of {modelB_name} = {avg_score_B}")

        # 3. Write result
        with open(file_A.replace('data.json', 'score.text'), 'a') as f:
            f.write(str({f"Compared to {modelB_name}'s win rate": avg_score_A}))
            f.write("\n")
        with open(file_B.replace('data.json', 'score.text'), 'a') as f:
            f.write(str({f"Compared to {modelA_name}'s win rate": avg_score_B}))
            f.write("\n")
        
        json.dump(data_A, open(file_A, 'w'), indent=4)
        json.dump(data_B, open(file_B, 'w'), indent=4)

def score_parser(text):
    """
    This function aims to extract the answer from a string using regular expressions, such as [[A]] -> A
    """
    pattern = r'\[\[(.*?)\]\]'
    matches = re.findall(pattern, text)
    return matches[0]

def single_scoring_function(sample_A, sample_B, category):
    # 1. Find the category
    for key in ["Code", "Creation", "Knowledge Utilization", "Language Generation", "Language Understanding", "Mathematics and Reasoning"]:
        if f'/{key}/' in category:
            category = key
            break
    
    # 2. Buiding conversation
    conversation = ''
    for conv_A, conv_B in zip(sample_A['conversations'], sample_B['conversations']):
        role = conv_A['from']
        if role == 'human':
            conversation += f"{role}: {conv_A['value']}\n"
        else:
            conversation += f"AI Assistant A: {conv_A['value']}\n"
            conversation += f"AI Assistant B: {conv_B['value']}\n"


    # 3. Get the scoring prompt
    if sample_A['reference_answer'] != '':
        category += ' (with reference answer)'
        score_template = pairwise_score_template[category]
        prompt = score_template.format(conversation=conversation, ref_question=sample_A['basic_question'], ref_answer=sample_A['reference_answer'])
    else:
        score_template = pairwise_score_template[category]
        prompt = score_template.format(conversation=conversation)

    messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]

    # 4. Call gpt-4
    response = openai.chat.completions.create(
            model='gpt-4-0125-preview',
            messages=messages,
            stop = ["\n"],
            temperature = 0,
            max_tokens = 200,
        )

    # 5. Parse the answer
    score = score_parser(response)

    return score

if __name__ == "__main__":
    # 1. Create argument parser
    parser = argparse.ArgumentParser(description='Score model predictions')
    parser.add_argument('--modelA_name', type=str, help='Name of the model')
    parser.add_argument('--modelB_name', type=str, help='Name of the model')
    parser.add_argument('--api_key', type=str, help='API key for the scoring function')
    parser.add_argument('--target_set', default='all', type=str, help='The set you want to evaluate, e.g., \"Mathematics and Reasoning/Applied Problems\"')
    args = parser.parse_args()
    
    # 2. Set openai config
    openai.api_key = args.api_key

    # 3. Call function to score model predictions
    pairwise_evaluate(args.target_set, args.modelA_name, args.modelB_name)
