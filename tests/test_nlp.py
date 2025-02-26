from app.nlp_utils import tokenize, bag_of_words

def test_tokenize():
    text = "Hello, Chatbot!"
    tokens = tokenize(text)
    assert isinstance(tokens, list)
    assert "hello" in tokens

def test_bag_of_words():
    tokens = ["hello", "chatbot"]
    all_words = ["hello", "chatbot", "test"]
    bag = bag_of_words(tokens, all_words)
    assert bag == [1, 1, 0]
