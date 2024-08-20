import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

def greeting(name):
    print(f"Hello, {name}!")
    print("Welcome to the review bot.")
    print("Wait a second...")
    # Call the ReviewAnalysis function
    rev = ReviewAnalysis(name)
    return rev

def userRev():
    print("What would you like to give a review about in the college?")
    print("e.g., staff, library, etc.")
    user_topic = input("YOU: ")
    print(f"You are giving a review about the college's {user_topic}.")
    print("Write your review about it:")
    user_review = input("YOU: ")
    return user_review

def ReviewAnalysis(name):
    user_rev = userRev()
    
    sia = SentimentIntensityAnalyzer()
    
    sentence = sia.polarity_scores(user_rev)
    
    review_df = pd.DataFrame([sentence])
    
    review_df.insert(0, 'Name', name)
    
    return review_df

# Create an empty DataFrame to hold all reviews
all_reviews_df = pd.DataFrame()

#looping till find 'q'

while True:
    user = input("Enter your name (or type 'q' to quit): ")
    if user.lower() == 'q':
        break
    review_df = greeting(user)
    all_reviews_df = pd.concat([all_reviews_df, review_df], ignore_index=True)


print(all_reviews_df)



