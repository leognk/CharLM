name = 'gpt_1'

out_dir = f'exp/enwik8/{name}'
eval_interval = 1000
eval_iters = 200
log_interval = 10

always_save_checkpoint = True

init_from = 'scratch'

wandb_log = True
wandb_project = 'enwik8'
wandb_run_name = name

dataset = 'enwik8'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 1024

n_layer = 12
n_head = 16
n_embd = 512
dropout = 0.0

max_iters = 100000
lr_decay_iters = max_iters

learning_rate = 6e-4
min_lr = learning_rate / 10

warmup_iters = 1000

# compile = False