from datasets import load_dataset

dataset = load_dataset("imdb")

print(dataset)

print(dataset.keys())                  
print(dataset["train"].features)       
print(len(dataset["train"]))           
print(dataset["train"][0])            
print(dataset["train"][0]["text"])     
print(dataset["train"][0]["label"])   



