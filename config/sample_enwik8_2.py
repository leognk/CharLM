name = 'patch_19-p=2'

init_from = 'resume'
out_dir = f'exp/enwik8/{name}'

data_in_bytes = True

# start = "\n"
start = "What is the answer to life, the universe, and everything?"

num_samples = 5
temperature = 0.8

sub_block_size = 1024
patch_size = 2
max_new_tokens = patch_size * sub_block_size

# device = 'cpu'