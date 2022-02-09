import streamlit as st
import pandas_profiling
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import pandas as pd
import PIL

st.set_page_config(page_title='page_title',layout="wide", page_icon='🐼')
st.image("pandasprofiling/images/logo.png", width=200)
st.markdown("## Pandas profiler for summary statistics")

with st.expander("What is the Pandas Profiler?"):


    st.image("pandasprofiling/images/pandas_profiler_logo.png", width=600)
    st.markdown(''' **Pandas profiler was created by Simon Brugman, weve just made it a bit easy to use for those who havent used python!**
     
Generates profile reports from a pandas DataFrame. The pandas df.describe() function is great but a little basic for serious exploratory data analysis. pandas_profiling extends the pandas DataFrame with df.profile_report() for quick data analysis.For each column the following statistics - if relevant for the column type - are presented in an interactive HTML report:

* Type inference: detect the types of columns in a dataframe.
* Essentials: type, unique values, missing values
* Quantile statistics like minimum value, Q1, median, Q3, maximum, range, interquartile range
* Descriptive statistics like mean, mode, standard deviation, sum, median absolute deviation, coefficient of variation, kurtosis, skewness
* Most frequent values
* Histograms
* Correlations highlighting of highly correlated variables, Spearman, Pearson and Kendall matrices
* Missing values matrix, count, heatmap and dendrogram of missing values
* Duplicate rows Lists the most occurring duplicate rows
* Text analysis learn about categories (Uppercase, Space), scripts (Latin, Cyrillic) and blocks (ASCII) of text data

https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/
''')

uploaded_file = st.file_uploader(label='Upload a your data', type=('.csv', '.xlsx'))
go = st.button('Submit data')

if go:
    
    if uploaded_file != None:

        with st.spinner('Uploading your data'):
            if '.xlsx' in uploaded_file.name:
                df = pd.read_excel(uploaded_file)
            elif '.csv' in uploaded_file.name:
                df = pd.read_csv(uploaded_file)
    else:
        st.warning('Sorry there is no data to upload!')
    
    pr = ProfileReport(df, title="Summary Report on Dataset")

    st_profile_report(pr)
