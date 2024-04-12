name = 'patch_4'

out_dir = f'exp/enwik8/{name}'
eval_iters = 200

init_from = 'resume'

dataset = 'enwik8'

sub_block_size = 1024
patch_size = 2
block_size = patch_size * sub_block_size

batch_size = 128 // patch_size

# device = 'cpu'
compile = False