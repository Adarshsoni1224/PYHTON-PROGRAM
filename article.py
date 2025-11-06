user_input=input("Enter the Sentence :")
article=("a","an","the")
words=user_input.split("  ")
article_count=0
for i in words :
	if i in article:
		article_count+=1

print("Sentence:",user_input)
print("article count:",article_count)
