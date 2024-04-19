name = 'patch_19-p=2'

out_dir = f'exp/enwik8/{name}'
eval_iters = 400

init_from = 'resume'

dataset = 'enwik8'

sub_block_size = 1024
patch_size = 2
block_size = patch_size * sub_block_size

batch_size = 32 // patch_size

compute_stats = True

# device = 'cpu'
compile = False