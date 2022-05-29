import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import nltk


sw = ["100", "oz", "use", "product", "12", "black", "white", "blue", "red", "yellow",
"new", "high", "nan", "pack", "free", "easy", "size", "one", "10", "clean","color","weight"
"made", "durable"]


def k_means():
    df = pd.read_csv("C:/Users/mirza/Downloads/walmart_preprocessed (1).csv")
    df['Category']=df['Category'].str.split(pat = "|").str[0]
    from nltk.corpus import stopwords
    stops = stopwords.words('english')
    stops.extend(sw)
    documents = df['Product Name'].values.astype("U")
    vectorizer = TfidfVectorizer(stop_words=stops)
    features = vectorizer.fit_transform(documents)
    k=7
    model = KMeans(n_clusters=k,init='k-means++',max_iter=100,n_init=1)
    model.fit(features)
    df['cluster'] = model.labels_
    df.to_csv('C:/Users/mirza/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/api/walmart_fin.csv')

