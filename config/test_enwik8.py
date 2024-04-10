name = 'gpt_1'

out_dir = f'exp/enwik8/{name}'
eval_iters = 200

init_from = 'resume'

dataset = 'enwik8'
batch_size = 128
block_size = 1024

# device = 'cpu'
compile = False