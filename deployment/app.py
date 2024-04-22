import pickle
import pandas as pd
import streamlit as st
from models import  KMeans
from models import  KMedoids
import matplotlib.pyplot as plt
from models import EnsembleClustering 
from sklearn.decomposition import PCA

st.title("Customer Purchase Behavior")

if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False

# Reading csv file with clustering
@st.cache_data
def read_csv():
    df = pd.read_csv("dataset/clustered_dataset.csv")
    return df

# Loading the model
@st.cache_resource
def load_model():
    model = pickle.load(open("model/clustering.pkl", 'rb'))
    return model

# Prediction of cluster on the given feature
@st.cache_data
def predict(_model, features):
    label = _model.predict(features)
    return label.item()

# Form submission
def form_submission():
    st.session_state["form_submitted"] = True

# Data transformation
def transform_data():
    df = read_csv().drop(['Cluster'], axis=1)
    input_data = [st.session_state["Revenue_given"], st.session_state["Frequency"], st.session_state["Recency"], 0 if st.session_state["uk"] == "No" else 1]
    df.loc[len(df)] = input_data
    pca = PCA(n_components = 2, random_state=42)
    features = pca.fit_transform(df)
    return features

# Features clustering centroid points
@st.cache_data
def clusterPointsMean(df):
    clusters = df['Cluster']
    df = df.drop(['Cluster'], axis=1)
    pca = PCA(n_components = 2, random_state=42)
    features = pca.fit_transform(df)

    x1 = [features[i][0] for i in range(len(features))]
    x2 = [features[i][1] for i in range(len(features))]

    cluster = clusters
    data = {
        "X1": x1,
        "X2": x2,
        "Cluster": cluster
    }
    data = pd.DataFrame(data)
    return data

# Display plot
@st.cache_data
def displayPoints(data, feature):
    c1_x, c1_y = data[data['Cluster'] == 0].drop(['Cluster'], axis=1).mean()
    c2_x, c2_y = data[data['Cluster'] == 1].drop(['Cluster'], axis=1).mean()

    fig, ax = plt.subplots()
    ax.scatter(c1_x, c1_y, color="red", label="Cluster-1", s = 150)
    ax.scatter(c2_x, c2_y, color="blue", label="Cluster-2", s = 150)
    ax.scatter(feature[0], feature[1], color="green", label="Data point", s = 150)
    ax.legend()
    st.pyplot(fig=fig)

def main():
    form = st.form(border=False, key="data_form")

    with form:
        c1, c2 = st.columns(2)

        c1.number_input(label="Revenue Contribution", key="Revenue_given")
        c1.number_input(label="Days past since last buy", min_value=0, value=0, key="Recency")

        c2.number_input(label="How Frequently bought", min_value=0, value=0, key="Frequency")
        c2.selectbox(label="From United Kingdom?", options=["Yes", "No"], index=0, key="uk")

        st.form_submit_button(label="Cluster Customer", type='primary', on_click=form_submission)

    if st.session_state["form_submitted"]:

        features = transform_data()

        feature = features[len(features)-1]

        model = load_model()

        st.markdown(f"## The customer falls within Cluster - {predict(model, feature.reshape(1, 2))+1}")

        df = read_csv()

        data = clusterPointsMean(df=df)

        displayPoints(data, feature)

if __name__ == "__main__":
    main()
