name = 'gpt_1'

out_dir = f'exp/enwik8/{name}'
eval_interval = 500
eval_iters = 200
log_interval = 10

always_save_checkpoint = True

init_from = 'scratch'

wandb_log = True
wandb_project = 'enwik8'
wandb_run_name = name

dataset = 'enwik8'
gradient_accumulation_steps = 1
batch_size = 60
block_size = 1024

n_layer = 12
n_head = 12
n_embd = 768
dropout = 0.0

max_iters = 50000
lr_decay_iters = max_iters

learning_rate = 6e-4
min_lr = learning_rate / 10

warmup_iters = 500

# compile = False