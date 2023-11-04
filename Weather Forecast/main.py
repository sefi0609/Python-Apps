import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')

place = st.text_input(label='Place:')

days = st.slider(label='Forecast Days', min_value=1, max_value=5,
                 help='Select the number of forecast days')

option = st.selectbox('Select data to view', ('Temperature', 'Sky'))

weather, date_time = get_data(place, days, option)

# if the user enter a city name
if place:
    # check if the city name exist
    if date_time == [] and weather == []:
        st.error(f'This city name {place} not found. Please enter a valid city name')
    else:
        match option:
            case 'Temperature':
                st.subheader(f'Temperature for the next {days} days in {place.title()}')
                fig = px.line(x=date_time, y=weather, labels={'x': 'Date', 'y': 'Temperature (C)'})
                st.plotly_chart(fig)
            case 'Sky':
                st.subheader(f'Sky for the next {days} days in {place.title()}')
                col1, col2, col3, col4, col5, col6 = st.columns(6)

                # create file path for each timestamp
                weather = [f'images/{icon}.png' for icon in weather]

                with col1:
                    for date, sky in zip(date_time[0::6], weather[0::6]):
                        st.image(sky)
                        st.write(date)
                with col2:
                    for date, sky in zip(date_time[1::6], weather[1::6]):
                        st.image(sky)
                        st.write(date)
                with col3:
                    for date, sky in zip(date_time[2::6], weather[2::6]):
                        st.image(sky)
                        st.write(date)
                with col4:
                    for date, sky in zip(date_time[3::6], weather[3::6]):
                        st.image(sky)
                        st.write(date)
                with col5:
                    for date, sky in zip(date_time[4::6], weather[4::6]):
                        st.image(sky)
                        st.write(date)
                with col6:
                    for date, sky in zip(date_time[5::6], weather[5::6]):
                        st.image(sky)
                        st.write(date)
