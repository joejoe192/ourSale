import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df = pd.read_csv('all_df.csv')
df_sale= df.groupby('Month')['Total'].sum().sort_values()
st.set_page_config(page_title='My Sale Dashboard',page_icon=':bar_chart:')
st.sidebar.header('Please filter here')
user_product = st.sidebar.multiselect(
 'Select Product',
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5]
)
user_city = st.sidebar.multiselect(
  'Select City',
    options = df['City'].unique(),
    default = df['City'].unique()[:5]
)
user_month = st.sidebar.multiselect(
  'Select Month',
    options = df['Month'].unique(),
    default = df['Month'].unique()[:5]
)
st.title(':bar_chart: Sale Dashboard for 2019')
our_total = df['Total'].sum()
no_of_product=df['Product'].nunique()
left_col,right_col = st.columns(2)
with left_col:
    st.subheader('Total Sales')
    st.subheader(f'Us ${our_total}')
with right_col:
    st.subheader('No. Of Products')
    st.subheader(f'{no_of_product}')
user_select = df.query('Product==@user_product and City==@user_city and Month==@user_month')
sale_by_product=user_select.groupby('Product')['Total'].sum().sort_values()
sale_by_month=user_select.groupby('Month')['Total'].sum().sort_values()
sale_by_product_fig = px.bar(sale_by_product, x=sale_by_product.index, y=sale_by_product.values,title='Sales by Product')
sale_by_month_fig = px.bar(sale_by_month, x=sale_by_month.index, y=sale_by_month.values,title='Sales by Month')
sale_by_city= user_select.groupby('City')['Total'].sum().sort_values()
sale_by_city_fig = px.pie(sale_by_city,values=sale_by_city.values,names=sale_by_city.index,title='Sales by City')
#sale_by_product_fig.show()
a,b,c=st.columns(3)
a.plotly_chart(sale_by_product_fig,use_container_width = True)
b.plotly_chart(sale_by_city_fig,user_container_width = True)
c.plotly_chart(sale_by_month_fig,use_container_width = True)
d,e = st.columns(2)
d.plotly_chart(fig_sale_by_month_line,use_container_width = True)
fig_scatter = px.scatter(df,x='Total',y='QuantityOrdered',title='Sales By Amount Quantity')
e.plotly_chart(fig_scatter,use_container_width = True)

    
    
 
                     
