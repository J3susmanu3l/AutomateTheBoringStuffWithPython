import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans
from sklearn import preprocessing

data = pd.read_csv('Example.csv')

# Create a scatter plot using the correct column names
plt.scatter(data[' Score'], data['Gender'])
plt.xlabel('Score')
plt.ylabel('Gender')
plt.title('Score vs Gender')
plt.show()