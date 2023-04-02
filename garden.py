import spacy

# load english model and assign to variable nlp
nlp = spacy.load('en_core_web_sm')

#list of garden path sentences
gardenpathSentences = ["The old man the boat.",    
"The horse raced past the barn fell.",    
"The cotton clothing is made of grows in Mississippi.",
"I convinced her children are noisy.",    
"The rat the cat the dog chased killed ate."]

# Hold the analyis of each string
output = ""

# Loop through each sentence in the gardenpathSentences
for sentence in gardenpathSentences:
    output = ""
    # For each word in a sentence pass the word through 
    # language model (nlp)
    for word in nlp(sentence):
        output += f"({word.text} - {word.pos_})"
    
    print(output)

# Meaning of two entities
print("\n Print the meaning of two entities")
print(spacy.explain("ADP"))
print(spacy.explain("AUX"))

# ADP Explanation 
# Stands for adposition - "An adposition is a word 
# that expresses the relationship between a noun or 
# pronoun and other words in a sentence" 
# The word "past" was associated with adposition but
# in the sentence "The horse raced past the barn fell."
# past is a verb - in this case it did not make sense

# AUX Explanation
# Stands for auxiliary, which is a type of verb that 
# is used to support the main verb in a sentence. 
# Auxiliaries are also known as helping verbs because 
# they "help" to form different grammatical constructions, 
# such as questions, negations, and verb tenses.
# The word "are" was associated with an auxillary verb
# In the sentence "I convinced her children are noisy.""
# this is correct and made sense
