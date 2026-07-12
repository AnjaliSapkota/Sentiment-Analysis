from datasets import load_dataset

dataset = load_dataset("imdb")

train = dataset["train"]
test = dataset["test"]