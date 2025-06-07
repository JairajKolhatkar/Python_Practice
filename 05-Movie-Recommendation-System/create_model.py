import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dummy data for sentiment analysis
texts = [
    "This movie was great! I loved it.",
    "Amazing film, highly recommended.",
    "One of the best movies I've seen.",
    "Terrible movie, waste of time.",
    "I hated this film, so boring.",
    "Worst movie ever, don't watch it."
]

labels = np.array([1, 1, 1, 0, 0, 0])  # 1 for positive, 0 for negative

# Create and train a simple model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
clf = MultinomialNB()
clf.fit(X, labels)

# Save the model and vectorizer to disk
pickle.dump(clf, open('nlp_model.pkl', 'wb'))
pickle.dump(vectorizer, open('tranform.pkl', 'wb'))

print("Model files created successfully.") 