import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
import numpy as np


def generate_ratings_data(num_users=100, num_products=20):
    data ={
        "user_id": [f'User{i}' for i in range(1,num_users+1) for _ in range(5)],
        "product_id":[f'Product{np.random.randint(1,num_products+1)}' for _ in range(num_users * 5)],
        'rating': np.random.randint(1,6,num_users * 5)

    }
    return pd.DataFrame(data)

ratings_data =generate_ratings_data()
reader = Reader(rating_scale=(1,5))
data = Dataset.load_from_df(ratings_data[['user_id','product_id','rating']],reader)
trainset, testset = train_test_split(data, test_size=0.2)

model = SVD()
model.fit(trainset)
predictions = model.test(testset)
accuracy.rmse(predictions)

def get_product_recommendations(user_id, n_recommendations=5):
    all_products = ratings_data['product_id'].unique()
    rated_products = ratings_data[ratings_data['user_id'] == user_id]['product_id']
    recommendations = []
    for product in all_products:
        if product not in rated_products.values:
            predicted_rating = model.predict(user_id,product).est
            recommendations.append((product, predicted_rating))
    
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:n_recommendations]


user_id_demo = 'User1'
recommended_products = get_product_recommendations(user_id_demo)
print(f"Recommended products for {user_id_demo}:")
for product, rating in recommended_products:
    print(f"{product} (Predicted rating: {rating:.2f})")




        


