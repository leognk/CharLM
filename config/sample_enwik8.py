name = 'gpt_1'

init_from = 'resume'
out_dir = f'exp/enwik8/{name}'

data_in_bytes = True

# start = "\n"
start = "What is the answer to life, the universe, and everything?"

num_samples = 5
max_new_tokens = 500
temperature = 0.8

# device = 'cpu'