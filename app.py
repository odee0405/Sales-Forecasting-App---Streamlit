import streamlit as st
import pandas as pd 
import pickle 

# 

# Interface 
st.write("""
# Sales Forecasting App
Fill form and predict!
As easy as that! 👍🏾 
""")
 
# Inputs 
date = st.date_input("Enter date")
store_nbr = st.number_input("Enter store number")
family = st.selectbox("Choose item family",('AUTOMOTIVE', 'BABY CARE', 'BEAUTY', 'BEVERAGES', 'BOOKS', 'BREAD/BAKERY', 'CELEBRATION', 'CLEANING', 'DAIRY', 'DELI', 'EGGS', 'FROZEN FOODS', 'GROCERY I', 'GROCERY II', 'HARDWARE', 'HOME AND KITCHEN I', 'HOME AND KITCHEN II', 'HOME APPLIANCES', 'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN', 'LINGERIE', 'LIQUOR,WINE,BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE', 'PET SUPPLIES', 'PLAYERS AND ELECTRONICS', 'POULTRY', 'PREPARED FOODS', 'PRODUCE', 'SCHOOL AND OFFICE SUPPLIES', 'SEAFOOD'))     
on_promotion = st.selectbox('Is the item on promotion?',('0 - No', '1 - Yes'))
city = st.selectbox("Enter city",('Ambato', 'Babahoyo', 'Cayambe', 'Cuenca', 'Daule', 'El Carmen', 'Esmeraldas', 'Guaranda', 'Guayaquil', 'Ibarra', 'Latacunga', 'Libertad', 'Loja', 'Machala', 'Manta', 'Playas', 'Puyo', 'Quevedo', 'Quito', 'Riobamba', 'Salinas', 'Santo Domingo'))
state = st.selectbox("Enter state",('Azuay', 'Bolivar', 'Chimborazo', 'Cotopaxi', 'El Oro', 'Esmeraldas', 'Guayas', 'Imbabura', 'Loja', 'Los Rios', 'Manabi', 'Pastaza', 'Pichincha', 'Santa Elena', 'Santo Domingo de los Tsachilas', 'Tungurahua')) 
type_x = st.selectbox('type_x',('Holiday', 'Additional', 'Transfer', 'Event', 'Bridge'))
cluster = st.selectbox('Choose cluster',(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17))
oil_price = st.number_input("Enter oil price")
type_y = st.selectbox('type_y',('A', 'B', 'C', 'D', 'E'))

# Prediction button
if st.button('Predict'):
    # Dataframe creation 
    df = pd.DataFrame(
        {
        "date": [date], "store_nbr": [store_nbr], "family": [family], "promotion": [on_promotion], "city": [city], "state": [state], "type_x": [type_x], "cluster": [cluster ], "oil_price": [oil_price], "type_y": [type_y],
        }
    )
    print(f"[Info] Input data as dataframe :\n {df.to_markdown()}")
    
 

 