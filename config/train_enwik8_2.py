name = 'patch'

out_dir = f'exp/enwik8/{name}'
eval_interval = 1000
eval_iters = 200
log_interval = 10

always_save_checkpoint = False

init_from = 'scratch'

wandb_log = True
wandb_project = 'enwik8'
wandb_run_name = name

dataset = 'enwik8'

sub_block_size = 1024
patch_size = 2
block_size = patch_size * sub_block_size

gradient_accumulation_steps = 1
batch_size = 16 // patch_size

n_layer = 10
n_head = 16
n_embd = 512
dropout = 0.2

max_iters = 200000
lr_decay_iters = max_iters

learning_rate = 1e-3
min_lr = 1e-4

warmup_iters = 1000

weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95

# compile = False