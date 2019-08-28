import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
#logging.basicConfig(level=logging.INFO)



tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

class bert_evaluation():

  def __init__(self):
    # Load pre-trained model (weights)
    self.model = BertModel.from_pretrained('bert-base-uncased')

    # Put the model in "evaluation" mode, meaning feed-forward operation.
    self.model.eval()

  def embed(self, text):
    marked_text = "[CLS] " + text + " [SEP]"
    tokenized_text = tokenizer.tokenize(marked_text)

    indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
    segments_ids = [1] * len(tokenized_text)

    # Convert inputs to PyTorch tensors
    tokens_tensor = torch.tensor([indexed_tokens])
    segments_tensors = torch.tensor([segments_ids])


    # Predict hidden states features for each layer
    with torch.no_grad():
      encoded_layers, _ = self.model(tokens_tensor, segments_tensors)

    batch_i = 0

    # Convert the hidden state embeddings into single token vectors
    # Holds the list of 12 layer embeddings for each token
    # Will have the shape: [# tokens, # layers, # features]
    token_embeddings = [] 

    # For each token in the sentence...
    for token_i in range(len(tokenized_text)):
      
      # Holds 12 layers of hidden states for each token 
      hidden_layers = [] 
      
      # For each of the 12 layers...
      for layer_i in range(len(encoded_layers)):
        
        # Lookup the vector for `token_i` in `layer_i`
        vec = encoded_layers[layer_i][batch_i][token_i]
        
        hidden_layers.append(vec)
        
      token_embeddings.append(hidden_layers)

    summed_last_4_layers = [torch.sum(torch.stack(layer)[-4:], 0) for layer in token_embeddings] # [number_of_tokens, 768]

    return {s:vec for s,vec in zip(tokenized_text,summed_last_4_layers)}



