from dict import get_word
from dict import get_sentence

from Crypto.Hash import MD5
from Crypto.Hash import SHA
from Crypto.Hash import SHA256

def my_hash(type, word):
	hash = type.new()
	hash.update(word.encode('utf-8'))
	return hash.hexdigest()

# gera palavra
palavra = get_word()
sentence = get_sentence()

print("Word:")

print("MD5: "+str(len(my_hash(MD5, palavra))*4))
print("SHA: "+str(len(my_hash(SHA, palavra))*4))
print("SHA256: "+str(len(my_hash(SHA256, palavra))*4))

print("\nSentence")

print("MD5: "+str(len(my_hash(MD5, sentence))*4))
print("SHA: "+str(len(my_hash(SHA, sentence))*4))
print("SHA256: "+str(len(my_hash(SHA256, sentence))*4))

