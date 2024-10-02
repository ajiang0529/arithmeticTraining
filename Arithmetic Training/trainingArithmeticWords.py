from openai import OpenAI

client = OpenAI(api_key='')
import datasets

# Load the dataset
dataset = datasets.load_dataset('EleutherAI/arithmetic', 'arithmetic_5ds')


# Slice the dataset to get the first 200 rows
sampled_dataset = dataset['validation'].select(range(200))

# Set up OpenAI API
def test_gpt4(problem):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": problem}],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()

# Iterate through the dataset and test GPT-4
results = []
for item in sampled_dataset:
    problem = item['context']
    expected_answer = item['completion'].strip()

    gpt4_answer = test_gpt4(problem).strip()

    result = {
        'problem': problem,
        'expected_answer': expected_answer,
        'gpt4_answer': gpt4_answer,
        'is_correct': gpt4_answer == expected_answer
    }
    results.append(result)

# Analyze results
correct_answers = sum([result['is_correct'] for result in results])
total_problems = len(results)
accuracy = correct_answers / total_problems * 100

print(f'Accuracy: {accuracy:.2f}%')

# Optionally save the results for further analysis
import pandas as pd
df = pd.DataFrame(results)
df.to_csv('gpt4_arithmetic_results.csv', index=False)
