import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# OIT=(-47070.44224)+0.927644394*Visible.Market+(-0.115119959)*Market.Size+
# 61485.99355*Win.Rate+2.60727E-07*Med.device.total.sales
# +(-5.600350397)*Med.device.total.sales.pc+(-20592.91843)*Med.device.total.sales.in.GDP
# +257802.74*Med.device.total.sales.in.HE


# Y variable( OIT) follows normal distribution with Mean: 45,599 and SD: 34,334

VM = st.number_input(label='Visible Market',step=1.,format='%.2f')
MS = st.number_input(label='Market Size',step=1.,format='%.2f')
WR=st.number_input(label='Win Rate',step=1.,format='%.2f')
MD_TS=st.number_input(label='Med Device Total Sales',step=1.,format='%.2f')
MD_TS_PC=st.number_input(label='Med Device Total Sales PC',step=1.,format='%.2f')
MD_TS_GDP=st.number_input(label='Med Device Total Sales in GDP',step=1.,format='%.2f')
MD_TS_HE=st.number_input(label='Med Device Total Sales in HE',step=1.,format='%.2f')

y_pred=(-47070.44224)+0.927644394*VM+(-0.115119959)*MS+61485.99355*WR+2.60727E-07*MD_TS+(-5.600350397)*MD_TS_PC+(-20592.91843)*MD_TS_GDP+257802.74*MD_TS_HE
st.write(f'Predicted Value is: {y_pred}')


def highlight_value_in_histogram(data, value_to_highlight, bins=100):
    # Create the histogram
    counts, bins, patches = plt.hist(data, bins=bins, edgecolor='black')

    # Highlight the specified value
    for i in range(len(bins) - 1):
        if bins[i] <= value_to_highlight < bins[i + 1]:
            patches[i].set_facecolor('red')
            break

   
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram with Highlighted Value')
    st.pyplot(plt.gcf())

np.random.seed(0)
data = np.random.normal(loc=45599, scale=34334, size=10000)
positive_data = list(filter(lambda x : x > 0, data))
value_to_highlight = int(y_pred)

highlight_value_in_histogram(positive_data, value_to_highlight)
