import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt 

st.set_page_config(
    page_icon="🧊",
    page_title="Diwali sales analysis",
    layout="wide")
# Load your dataset
df = pd.read_csv('data.csv', encoding='unicode_escape')

# Add Streamlit app title and header
st.title('Diwali Sales Analysis')

# Display data summary
st.write('## Data Summary')
st.write('Shape of the dataset:', df.shape)
st.write(df)

# Add interactive visualizations using Streamlit components
st.write('## Visualizations')

# Countplot for Gender
def save_plot_as_image(figure, digipodium):
    figure.savefig(digipodium, bbox_inches='tight')
    st.image(digipodium)
def save_seaborn_plot_as_image(figure, digipodium):
    figure.savefig(digipodium, bbox_inches='tight')
    st.image(digipodium)

# Countplot for Gender
st.subheader('Gender Distribution')
gender_countplot = sb.countplot(x='Gender', data=df)
# save_plot_as_image(gender_countplot.get_figure(), 'gender_distribution.png')
st.write('### Gender Distribution:')
st.write(' Female Dominance: The data indicates a higher representation of female buyers compared to males. :')
st.write(' This suggests a significant female presence in the customer base during the Diwali sales period.')
st.write('---')

# Countplot for Age Group
st.subheader('Age Group Distribution')
age_group_countplot = sb.countplot(data=df, x='Age Group', hue='Gender')
# save_plot_as_image(age_group_countplot.get_figure(), 'age_group_distribution.png')

# Age Group Distribution Conclusion
st.write('### Age Group Distribution:')
st.write('The majority of buyers belong to the 26-35 age group, particularly females.')
st.write('This age group is the most active in terms of making purchases.')
st.write('---')
# State-wise Orders
st.subheader('State-wise Orders')
state_orders = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False)
st.bar_chart(state_orders.set_index('State')['Orders'])



# State-wise Total Sales/Amount
st.subheader('State-wise Total Sales/Amount')
state_sales = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.bar_chart(state_sales.set_index('State')['Amount'])

# State-wise Orders and Total Sales Conclusion
st.write('### State-wise Orders and Total Sales:')
st.write('Uttar Pradesh, Maharashtra, and Karnataka are the top states in terms of both order quantity and total sales.')
st.write('These states have a higher market share and contribute significantly to overall sales.')
st.write('---')

st.subheader('Marital Status Distribution')
marital_status_countplot = sb.countplot(data=df, x='Marital_Status')
# save_seaborn_plot_as_image(marital_status_countplot.get_figure(), 'marital_status_distribution.png')

# Marital Status Distribution
st.subheader('Marital Status Distribution')
marital_status_countplot = sb.countplot(data=df, x='Marital_Status')
# save_seaborn_plot_as_image(marital_status_countplot.get_figure(), 'marital_status_distribution.png')

# Marital Status vs. Amount with Gender hue
st.subheader('Marital Status vs. Amount with Gender Hue')
marital_status_vs_amount = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
st.bar_chart(marital_status_vs_amount.set_index('Marital_Status')['Amount'])

#Marital Status Distribution Conclusion
st.write('### Marital Status Distribution:')
st.write('Most buyers are married, especially women.')
st.write('Married buyers, particularly married women, make up a substantial portion of the customer base.')
st.write('---')
# Occupation Distribution
st.subheader('Occupation Distribution')
plt.figure(figsize=(19, 5))
occupation_countplot = sb.countplot(data=df, x='Occupation')
# save_seaborn_plot_as_image(occupation_countplot.get_figure(), 'occupation_distribution.png')

# Occupation Distribution Conclusion
st.write('### Occupation Distribution:')
st.write('The top occupations of buyers are in IT, Healthcare, and Aviation sectors.')
st.write('These sectors have a higher number of buyers, possibly due to higher disposable income.')
st.write('---')
# Top 10 Most Sold Products
st.subheader('Top 10 Most Sold Products')
top_10_products = df.groupby(['Product_Category'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
st.bar_chart(top_10_products.set_index('Product_Category')['Orders'])

# Top 10 Most Sold Products Conclusion
st.write('### Top 10 Most Sold Products:')
st.write('The top-selling products have higher order quantities.')
st.write('Identifying these products can help in optimizing inventory and marketing efforts.')

st.write('---')
st.write('### Conclusion')
conclusion = """


The Diwali sales analysis highlights several key insights:

- Female buyers play a pivotal role, with a notable presence in the customer base.
- The 26-35 age group is the most active, especially among females.
- States like Uttar Pradesh, Maharashtra, and Karnataka are crucial for sales.
- Married individuals, particularly women, form a substantial part of our customer base.
- Top occupations include IT, Healthcare, and Aviation sectors.
- Identifying and prioritizing top-selling products can optimize inventory and marketing efforts.

These findings underscore the importance of tailoring marketing strategies and product offerings to cater to the preferences of female buyers and the dominant age group. 
Focusing on key states, marital status segments, and top occupations can lead to sustained growth and success in future Diwali sales campaigns.
"""

# Display the conclusion
st.write(conclusion)
st.write('------')
st.markdown('### Developed by Vinayak Shukla')