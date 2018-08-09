from Crypto.Hash import MD5
from Crypto.Hash import SHA

secret = "6655fcfadca4adff9933c07842161c65f993c9bd";
pwd = "7ab9495396df849963e683d724f85086";

print("BITS: "+ str(len(secret)*4))
print("BITS: "+ str(len(pwd)*4))
print()

secrets = ['6655fcfadca4adff9933c07842161c65f993c9bd', '201b8f20dd1695d7d46e80a23f0487d1cb91e255', '460b8dde3c375c9f9b87e3ab44ffce3fa1305744', '97ea5599536ab294f94a47c4194c2c6d488d2725', 'fa0754b9861f7065fd7c6270efb07fc6ac3b0ad8']
pwds = ['7ab9495396df849963e683d724f85086','88b4ce63d49305ffd3570c7c24c0c5b0','66ce76c7795eb6325705fb6efe0afc1d','90f441eed2c426e09ae41eb53095623e','5e815814b6c62056f25078ef388f1b53']
salts = [632, 470, 101, 642, 987]

def my_hash(type, word):
	hash = type.new()
	hash.update(word.encode('utf-8'))
	return hash.hexdigest()

words = open('dict/words');
i = 0
print("SECRETS:")
for secret in secrets:
	salt = salts[i]
	for word in words:
		w = word.replace('\n', '')
		digest = my_hash(SHA, w)
		if(digest == secret):
			print(w)
	words.seek(0)


print("\nPWDS:")
words.seek(0)
i = 0
for pwd in pwds:
	salt = salts[i]
	i += 1
	for word in words:
		w = word.replace('\n', '')
		digest = my_hash(MD5, str(salt)+w)
		if(digest == pwd):
			print(w)
	words.seek(0)

