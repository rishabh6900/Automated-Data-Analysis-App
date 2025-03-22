import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import pandas_profiling
#from ydata_profiling import ProfileReport




def clean_data(df):
    return df.replace([float('inf'), float('-inf')], pd.NA)

def main():
    st.title("Automated Data Analysis App")
    st.write("Upload a CSV file for quick insights and visualizations!")
    
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = clean_data(df)  # Cleaning infinite values

        # Display Data Information
        st.write("## Data Preview")
        st.dataframe(df.head())
        st.write("## Sample Data")
        st.dataframe(df.sample())
        st.write("## Summary Statistics")
        st.write(df.describe())
        st.write("## Missing Values")
        st.write(df.isnull().sum())

        # Identify Numerical and Categorical Columns
        num_cols = df.select_dtypes(include=['number']).columns.tolist()
        cat_cols = df.select_dtypes(exclude=['number']).columns.tolist()

        # Data Visualization Section
        st.write("## Data Visualization")

        try:
            # Box Plot
            if num_cols and cat_cols:
                st.write("### Box Plot")
                x_col = st.selectbox("Select categorical column", cat_cols, key="box_x")
                y_col = st.selectbox("Select numerical column", num_cols, key="box_y")
                fig, ax = plt.subplots()
                sns.boxplot(x=df[x_col], y=df[y_col], palette="coolwarm", ax=ax)
                st.pyplot(fig)
                st.success("Box plot successfully plotted!")
        except Exception as e:
            st.error(f"Error in Box Plot: {e}")
        
        try:
            # Histogram
            if num_cols:
                st.write("### Histogram")
                hist_col = st.selectbox("Select numerical column for Histogram", num_cols, key="hist")
                fig, ax = plt.subplots()
                sns.histplot(df[hist_col], bins=30, kde=True, ax=ax)
                st.pyplot(fig)
                st.success("Histogram successfully plotted!")
        except Exception as e:
            st.error(f"Error in Histogram: {e}")
        
        try:
            # Correlation Heatmap
            if num_cols:
                st.write("### Correlation Heatmap")
                fig, ax = plt.subplots()
                sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
                st.pyplot(fig)
                st.success("Correlation heatmap successfully plotted!")
        except Exception as e:
            st.error(f"Error in Correlation Heatmap: {e}")
        
        try:
            # Scatter Plot
            if len(num_cols) > 1:
                st.write("### Scatter Plot")
                x_col = st.selectbox("Select X-axis", num_cols, key="scatter_x")
                y_col = st.selectbox("Select Y-axis", num_cols, key="scatter_y")
                fig, ax = plt.subplots()
                sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
                st.pyplot(fig)
                st.success("Scatter plot successfully plotted!")
        except Exception as e:
            st.error(f"Error in Scatter Plot: {e}")
        
        try:
            # Pairplot
            if len(num_cols) > 1:
                st.write("### Pairplot")
                fig = sns.pairplot(df[num_cols], diag_kind='kde')
                st.pyplot(fig)
                st.success("Pairplot successfully plotted!")
        except Exception as e:
            st.error(f"Error in Pairplot: {e}")
        
        try:
            # Regression Plot
            if len(num_cols) > 1:
                st.write("### Regression Plot")
                reg_x = st.selectbox("Select X-axis", num_cols, key="reg_x")
                reg_y = st.selectbox("Select Y-axis", num_cols, key="reg_y")
                fig, ax = plt.subplots()
                sns.regplot(x=df[reg_x], y=df[reg_y], ax=ax)
                st.pyplot(fig)
                st.success("Regression plot successfully plotted!")
        except Exception as e:
            st.error(f"Error in Regression Plot: {e}")
        
        try:
            # Pie Chart
            if cat_cols:
                st.write("### Pie Chart")
                pie_col = st.selectbox("Select categorical column for Pie Chart", cat_cols, key="pie_col")
                pie_data = df[pie_col].value_counts()
                fig, ax = plt.subplots()
                ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
                ax.axis('equal')
                st.pyplot(fig)
                st.success("Pie chart successfully plotted!")
        except Exception as e:
            st.error(f"Error in Pie Chart: {e}")
        
        try:
            # Pandas Profiling Report
            st.write("## Detailed Data Report")
            #profile = ydata_profiling.ProfileReport(df)
            profile = pandas_profiling.ProfileReport(df)
            st_profile_report(profile)
            st.success("Pandas profiling report successfully generated!")
        except Exception as e:
            st.error(f"Error in Pandas Profiling Report: {e}")

if __name__ == "__main__":
    main()

# Sidebar Information
st.sidebar.image("image.png")
st.sidebar.title("Automated Data Analysis App")
