import pandas as pd
import streamlit as st
import numpy as np
import time
import plotly
import plotly.express as px
import plotly.offline as py
from PIL import Image
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns
from matplotlib.backends.backend_agg import RendererAgg
import matplotlib.pyplot as plt
import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import gensim, spacy, logging, warnings
import gensim.corpora as corpora
from gensim import utils
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
import spacy
from wordcloud import STOPWORDS
df = pd.read_csv('responsesfinal.csv')
transposed_df1 = pd.read_csv('population.csv')
leb =  pd.read_csv('lebanon.csv')
jor = pd.read_csv('jor.csv')
syr = pd.read_csv('syr.csv')
gz = pd.read_csv('gz.csv')
wb = pd.read_csv('wb.csv')
rg = pd.read_csv('Regis.csv')
rs = pd.read_csv('registered.csv')
st.set_option('deprecation.showPyplotGlobalUse', False)

pick = st.sidebar.selectbox("What do you want to know?", ('Overview: The Refugee Situation In Lebanon',
            "The Data: Constituents and Features", "Educational Levels and Employment Status", "Industries, Training, and More", "Executive Summary")) #"Challenges and Obstacles: Implementing LDA and Topic Modelling",

if pick == 'Overview: The Refugee Situation In Lebanon':
    st.title("Palestinian Refugees Across Land and Time")

    add_selectbox = st.sidebar.selectbox(
    'Select Location',
    ('Lebanon', 'Jordan', 'Syria', "West Bank", "Gaza")
    )

    if add_selectbox == 'Lebanon': #and add_slider == "1970":
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            dfR = leb['Population']
            dfF= leb['Founded']
            countR= dfR.value_counts()
            countF=dfF.value_counts()
            trace = go.Bar(
                x=countF.index,
                y=dfR.values,text = dfR.values,  textposition='auto',
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = dfR.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )
            data = [trace]
            layout = go.Layout(barmode = "group", title = 'Population Across Different Camps In Lebanon', width=800, height=800, plot_bgcolor='rgba(0,0,0,0)')
            fig = go.Figure(data = data, layout = layout)
            fig.update_layout(
            xaxis_title="Camp Name",
            yaxis_title="Population")
            st.plotly_chart(fig)

        with c3:
            trace2 = go.Scatter(
                        x = transposed_df1.Year,
                        y = transposed_df1.Lebanon,
                        mode = "lines+markers",
                        name = "Lebanon",
                        marker = dict(color = '#008080'),
                        text= 'Year')
            data = [trace2]
            layout = dict(title = 'Number of Refugees Across The Years',  width=800, height=800, plot_bgcolor='rgba(0,0,0,0)',
            xaxis= dict(title= 'Year',ticklen= 9,zeroline= True)
                 )
            fig = go.Figure(data = data, layout = layout)
            fig.update_layout(
            yaxis_title="Population")
            st.plotly_chart(fig)

        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            labels = 'Education', 'Health'
            sizes = [1707, 297]
            explode = (0.1, 0)  # explode 1st slice
            fig1 = px.pie(names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Sector Distribution')
            fig1.update_layout(width=620, height=620, plot_bgcolor='rgba(0,0,0,0)')
            fig1.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig1)
            #st.write('Data source: UNRWA online database.')

            #data = [trace]
            #ayout = go.Layout(barmode = "group", title = 'Sector Distribution', width=800, height=800)
            #fig = go.Figure(data = data, layout = layout)
            #st.plotly_chart(fig)

        with c3:
            dfRl = rs.Lebanon
            dfFl= rs.Status
            countR1= dfRl.values
            countF1=dfFl.index
            trace1 = go.Bar(
                x=dfFl,
                y=dfRl.values, text = dfRl.values,  textposition='auto',
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = dfRl.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )
            data1 = [trace1]
            layout = go.Layout(barmode = "group", title='Registration of Refugees', width=900, height=800, plot_bgcolor='rgba(0,0,0,0)')
            fig = go.Figure(data = data1, layout = layout)
            fig.update_layout(
            xaxis_title="Type of Registration",
            yaxis_title="Population")
            fig
            st.markdown("Data source: UNRWA online database. UNRWA's definition of Other Registered Persons refer to those who, at the time of original registration did not satisfy all of UNRWA’s Palestine refugee criteria, but who were determined to have suffered significant loss and/or hardship for reasons related to the 1948 conflict in Palestine; they also include persons who belong to the families of other registered persons.")

    if add_selectbox == 'Jordan': #and add_slider == "1970":
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            dfR = jor['Population']
            dfF= jor['Founded']
            countR= dfR.value_counts()
            countF=dfF.value_counts()
            trace = go.Bar(
                x=countF.index,
                y=dfR.values,text = dfR.values,  textposition='auto',
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = dfR.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )
            data = [trace]
            layout = go.Layout(barmode = "group", title='Population Across Different Camps In Jordan', plot_bgcolor='rgba(0,0,0,0)')
            fig = go.Figure(data = data, layout = layout)
            fig.update_layout(
            xaxis_title="Camp Name",
            yaxis_title="Population")
            st.plotly_chart(fig)

        with c3:
            trace2 = go.Scatter(
                        x = transposed_df1.Year,
                        y = transposed_df1.Jordan,
                        mode = "lines+markers",
                        name = "Jor",
                        marker = dict(color = '#008080'))
            data = [trace2]
            layout = dict(title = 'Number of Refugees Across The Years',  width=800, height=800, plot_bgcolor='rgba(0,0,0,0)',
            xaxis= dict(title= 'Year',ticklen= 9,zeroline= True),
                 )
            fig = go.Figure(data = data, layout = layout)
            st.plotly_chart(fig)
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))

        with c1:
            labels = 'Education', 'Health'
            sizes = [4641, 680]
            explode = (0.1, 0)  # explode 1st slice
            fig = px.pie(names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Sector Distribution')
            fig.update_layout(width=620, height=620,)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

        with c3:
            with c3:
                dfRl = rs.Jordan
                dfFl= rs.Status
                countR1= dfRl.values
                countF1=dfFl.index
                trace1 = go.Bar(
                    x=dfFl,
                    y=dfRl.values, text = dfRl.values,  textposition='auto',
                    marker=dict(
                    #color = np.random.randn(500), #set color equal to a variable
                        color = dfRl.values,
                        colorscale='Tealgrn',
                        showscale=False
                        ),
                        )
                data1 = [trace1]
                layout = go.Layout(barmode = "group", title='Registration of Refugees', width=900, height=800, plot_bgcolor='rgba(0,0,0,0)')
                fig = go.Figure(data = data1, layout = layout)
                fig.update_layout(
                xaxis_title="Type of Registration",
                yaxis_title="Population")
                fig

    if add_selectbox == 'Syria': #and add_slider == "1970":
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            dfR = syr['Population']
            dfF= syr['Founded']
            countR= dfR.value_counts()
            countF=dfF.value_counts()
            trace = go.Bar(
                x=countF.index,
                y=dfR.values, text = dfR.values,  textposition='auto',
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = dfR.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )
            data = [trace]
            layout = go.Layout(barmode = "group", title ='Population Across Different Camps In Syria')
            fig = go.Figure(data = data, layout = layout)
            st.plotly_chart(fig)
        with c3:
            trace2 = go.Scatter(
                        x = transposed_df1.Year,
                        y = transposed_df1.Syria,
                        mode = "lines+markers",
                        name = "Syria",
                        marker = dict(color = '#008080'),
                        text= 'Syria')
            data = [trace2]
            layout = dict(title = 'Number of Refugees Across The Years',  width=800, height=800,  plot_bgcolor='rgba(0,0,0,0)',
            xaxis= dict(title= 'Year',ticklen= 9,zeroline= True)
                 )
            fig = go.Figure(data = data, layout = layout)
            st.plotly_chart(fig)

        c1, c2, c3 = st.beta_columns((2, 0.5, 2))

        with c1:
            labels = 'Education', 'Health'
            sizes = [1922, 430]
            explode = (0.1, 0)  # explode 1st slice
            fig = px.pie(names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Sector Distribution')
            fig.update_layout(width=620, height=620,)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)
        with c3:
            with c3:
                dfRl = rs.Syria
                dfFl= rs.Status
                countR1= dfRl.values
                countF1=dfFl.index
                trace1 = go.Bar(
                    x=dfFl,
                    y=dfRl.values, text = dfRl.values,  textposition='auto',
                    marker=dict(
                    #color = np.random.randn(500), #set color equal to a variable
                        color = dfRl.values,
                        colorscale='Tealgrn',
                        showscale=False
                        ),
                        )
                data1 = [trace1]
                layout = go.Layout(barmode = "group", title='Registration of Refugees', width=900, height=800, plot_bgcolor='rgba(0,0,0,0)')
                fig = go.Figure(data = data1, layout = layout)
                fig.update_layout(
                xaxis_title="Type of Registration",
                yaxis_title="Population")
                fig

    if add_selectbox == 'West Bank': #and add_slider == "1970":
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            dfR = wb['Population']
            dfF= wb['Founded']
            countR= dfR.value_counts()
            countF=dfF.value_counts()
            trace = go.Bar(
                x=countF.index,
                y=dfR.values, text = dfR.values,  textposition='auto',
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = dfR.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )
            data = [trace]
            layout = go.Layout(barmode = "group", title ='Population Across Different Camps In West Bank', plot_bgcolor='rgba(0,0,0,0)')
            fig = go.Figure(data = data, layout = layout)
            fig.update_layout(
            xaxis_title="Camp Name",
            yaxis_title="Population")
            st.plotly_chart(fig)

        with c3:
            trace2 = go.Scatter(
                        x = transposed_df1.Year,
                        y = transposed_df1['West Bank'],
                        mode = "lines+markers",
                        name = "West Bank",
                        marker = dict(color = '#008080'),
                        text= 'West Bank')
            data = [trace2]
            layout = dict(title = 'Number of Refugees Across The Years',  width=800, height=800, plot_bgcolor='rgba(0,0,0,0)',
            xaxis= dict(title= 'Year',ticklen= 9,zeroline= True)
                 )
            fig = go.Figure(data = data, layout = layout)
            st.plotly_chart(fig)

        c1, c2, c3 = st.beta_columns((2, 0.5, 2))

        with c1:
            labels = 'Education', 'Health'
            sizes = [2332, 693]
            fig = px.pie(names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Sector Distribution')
            fig.update_layout(width=620, height=620,)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

        with c3:
            with c3:
                dfRl = rs['West Bank']
                dfFl= rs.Status
                countR1= dfRl.values
                countF1=dfFl.index
                trace1 = go.Bar(
                    x=dfFl,
                    y=dfRl.values, text = dfRl.values,  textposition='auto',
                    marker=dict(
                    #color = np.random.randn(500), #set color equal to a variable
                        color = dfRl.values,
                        colorscale='Tealgrn',
                        showscale=False
                        ),
                        )
                data1 = [trace1]
                layout = go.Layout(barmode = "group", title='Registration of Refugees', width=900, height=800, plot_bgcolor='rgba(0,0,0,0)')
                fig = go.Figure(data = data1, layout = layout)
                fig.update_layout(
                xaxis_title="Type of Registration",
                yaxis_title="Population")
                fig

    if add_selectbox == 'Gaza': #and add_slider == "1970":
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            dfR = gz['Population']
            dfF= gz['Founded']
            countR= dfR.value_counts()
            countF=dfF.value_counts()
            trace = go.Bar(
                x=countF.index,
                y=dfR.values, text = dfR.values,  textposition='auto',
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = dfR.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )
            data = [trace]
            layout = go.Layout(barmode = "group", title='Population Across Different Camps In Gaza', plot_bgcolor='rgba(0,0,0,0)')
            fig = go.Figure(data = data, layout = layout)
            fig.update_layout(
            xaxis_title="Camp Name",
            yaxis_title="Population")
            st.plotly_chart(fig)
        with c3:
            trace2 = go.Scatter(
                        x = transposed_df1.Year,
                        y = transposed_df1['Gaza Strip'],
                        mode = "lines+markers",
                        name = "Gaza",
                        marker = dict(color = '#008080'),
                        text= 'Gaza')
            data = [trace2]
            layout = dict(title = 'Number of Refugees Across The Years',  width=800, height=800, plot_bgcolor='rgba(0,0,0,0)',
            xaxis= dict(title= 'Year',ticklen= 9,zeroline= True)
                 )
            fig = go.Figure(data = data, layout = layout)
            st.plotly_chart(fig)

        c1, c2, c3 = st.beta_columns((2, 0.5, 2))

        with c1:
            labels = 'Education', 'Health'
            sizes = [9544, 886]
            explode = (0.1, 0)  # explode 1st slice
            fig = px.pie(names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Sector Distribution')
            fig.update_layout(width=620, height=620,)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)
        with c3:
            dfRl = rs['Gaza Strip']
            dfFl= rs.Status
            countR1= dfRl.values
            countF1=dfFl.index
            trace1 = go.Bar(
                x=dfFl,
                y=dfRl.values, text = dfRl.values,  textposition='auto',
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = dfRl.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )
            data1 = [trace1]
            layout = go.Layout(barmode = "group", title='Registration of Refugees', width=900, height=800, plot_bgcolor='rgba(0,0,0,0)')
            fig = go.Figure(data = data1, layout = layout)
            fig.update_layout(
            xaxis_title="Type of Registration",
            yaxis_title="Population")

            fig
#    add_slider = st.select_slider(
#    'Select Year',
#    options=['1970', '1980', '1990', '2000', '2004', '2009', '2018']
#      )
if pick == "The Data: Constituents and Features":

    st.title('Data Overview')
    st.markdown('The data collected was based on the survey that was written with the approval of all responsible entities.')
    st.markdown('The data was predominantly of the qualitiative nature, which has shown to be interesting to work with and get insights from.')
    st.markdown('Below is some general information about the data collected and some important notes to make.')

    st.markdown('#')
    c1, c2, c3 = st.beta_columns((2, 0.5, 2))
    with c1:
        qtions = len(df.columns)
        st.markdown('Number of questions')
        x = st.write(qtions)

    with c3:
        index = df.index
        number_of_rows = len(index)
        st.markdown('Number of respondents')
        x = st.write(number_of_rows)

        st.markdown('#')

    st.markdown('If you want to see what the dataset responses look like, click on the below button.')
    if st.button('Data'):
        df

    c1, c2, c3 = st.beta_columns((2, 0.5, 2))
    with c1:
        cor = pd.read_csv('coor.txt')
        mapbox_access_token='eyJ1IjoibW9uenMiLCJhIjoiY2tzZ3BoNDFvMW0zejJwbzMzbml0aDVlNyJ9.lKnYbpwc1uc7Dq09OabDmA'
        fig = go.Figure(go.Scattermapbox(
        fill = "none",
        lon = [35.8308,	35.3729, 35.5973, 36.211, 35.2038, 35.5018, 35.9019], lat = [34.4381, 33.5571, 33.8101,	34.0047, 33.2705, 33.8938, 33.8463],
        marker = { 'size': cor.resp, 'color': "teal" }))

        col1= cor['resp']
        cor_sorted = cor.nlargest(5, 'resp')
        y = cor_sorted['key'][0]
        maxresp = col1.max()
        fig.update_layout(
                    mapbox = {
                    'style': "stamen-terrain",
                    'center': {'lon': 35.8623, 'lat': 33.8547 },
                    'zoom': 7.5},
                    showlegend = False)
        fig.update_layout(
                autosize=False,
                width=800,
                height=780, title='Geographic Distribution of Respondents', title_x=0.5)
        fig.update_traces(hovertext=cor.key, selector=dict(type='scattermapbox'))
        st.plotly_chart(fig)
        #st.markdown(f'The largest number of respondents was **{maxresp}** and  were from the **{y}** area.')



    with c3:
        dfR = df['Area of Residency ']
        countR= dfR.value_counts()
        trace = go.Bar(
            x=countR.index,
            y=countR.values, text = countR.values,  textposition='auto',
            marker=dict(
            #color = np.random.randn(500), #set color equal to a variable
                color = countR.values,
                colorscale='Tealgrn',
                showscale=False
                ),
                )
        layout = go.Layout(title='Geographic Locations of Respondents', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)', height=800, width=800)
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)
        #st.markdown(f'The largest number of respondents was {maxresp} from the {y} area.')
    with c1:
        dfR = df['Residency ']
        countR= dfR.value_counts()
        trace = go.Bar(
                x=countR.index,
                y=countR.values,
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = countR.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    )

        layout = go.Layout(title='Areas of Residency', title_x=0.5,  plot_bgcolor='rgba(0,0,0,0)', width=800, height=800)
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        fig
    with c3:
        cnt_srs = df['Gender'].value_counts()
        trace = go.Bar(
            x=cnt_srs.index,
            y=cnt_srs.values, text = cnt_srs.values,  textposition='auto',
            marker=dict(
            #color = np.random.randn(500), #set color equal to a variable
                color = cnt_srs.values,
                colorscale='Tealgrn',
                showscale=False
                ),
                )

        layout = go.Layout(title='Gender Distribution of Respondents', title_x=0.5, width=800, height=800, plot_bgcolor='rgba(0,0,0,0)')
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)

    c1, c2, c3 = st.beta_columns((2, 0.5, 2))
    with c1:
        dfN = df.iloc[:, [3]]
        temp_series = dfN.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dfN, names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Nationality Distribution')
        fig.update_layout(title_x=0.7)
        fig.update_layout(width=800, height=800)
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        st.plotly_chart(fig)

        with c3:
            dfX = df.iloc[:, [8]]
            temp_series = dfX.value_counts()
            labels = (np.array(temp_series.index))
            sizes = (np.array((temp_series / temp_series.sum())*100))
            fig = px.pie(dfN, names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Age of Respondents')
            fig.update_layout(title_x=0.7)
            fig.update_layout(width=620, height=620)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.write('##')
            st.write('##')
            st.plotly_chart(fig)


    c1, c2, c3 = st.beta_columns((2, 0.5, 2))
    with c1:
        dfM = df['Marital Status']
        cnt_srsm = df['Marital Status'].value_counts()
        temp_series = dfM.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dfM, names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Marital Status of Respondents')
        fig.update_layout(title_x=0.7)
        fig.update_layout(width=620, height=620)
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        st.plotly_chart(fig)

    with c3:
        temp_series = df['Do you have any disability?'].value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(df['Do you have any disability?'], names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Disability?')
        fig.update_layout(title_x=0.7)
        fig.update_layout(width=620, height=620)
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        st.plotly_chart(fig)




if pick == "Educational Levels and Employment Status":
    st.title('Educational Levels, Employment Status, Job Search Methods Adopted, and More')
    st.markdown('The below highlights the insights that were generated by conducting the study on the various enities across the different regions in Lebanon, to be able to identify exactly what they are lacking and where opportunities can be given.')
    st.write('##')
    selectgen = st.sidebar.selectbox('Please select one option to view the Employment Status', ('Male', 'Female', 'All'))
    c1, c2, c3 = st.beta_columns((2, 0.5, 2))
    if selectgen == 'Male':
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            st.markdown('This question was tailored to understand the employment status of the respondents as of now, in which they answered as follows.')
            dfmale = df[df.Gender == 'Male']

            dfS = dfmale['Employment Status']
            countS= dfS.value_counts()
            trace1 = go.Bar(
                y=countS.index, text = countS.values,  textposition='auto',
                x=countS.values,
                marker=dict(color = countS.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    orientation = 'h') # width=800, height=400)

            layout1 = go.Layout(title='Employment Status', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
            data1 = [trace1]
            fig1 = go.Figure(data=data1, layout=layout1)
            fig1.update_layout(
            #autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig1)

            st.markdown('This question was tailored to understand what job search methods do the respondents employ, in which they answered as follows.')
            dfO = dfmale['In case of job search, methods used in search']
            countO= dfO.value_counts()
            trace = go.Bar(
                y=countO.index, text = countO.values,  textposition='auto',
                x=countO.values,
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = countO.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ), orientation = 'h')

            layout = go.Layout(title='Job Search Methods Adopted', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')#, width=700, height=600)
            data = [trace]
            fig = go.Figure(data=data, layout=layout)
            fig.update_layout(
            autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig)



        with c3:
            st.markdown('For those who are currently working, when asked about if the work they do is in their field, they answered as follows.')
            dfx = dfmale['In case of work (current or former), do you work in your field?']
            temp_series = dfx.value_counts()
            labels = (np.array(temp_series.index))
            sizes = (np.array((temp_series / temp_series.sum())*100))
            fig = px.pie(dfx, names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Work vs Field Relation?')
            fig.update_layout(title_x=0.5)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

            st.write('')
            st.write('')
            st.write('')
            st.markdown('This question was to understand whether the respondents preferred or were mostly in the field of self-employment, in which they answered as follows.')
            dfself = dfmale['Did you try self-employment?']
            st.write('')
            temp_series = dfself.value_counts()
            labels = (np.array(temp_series.index))
            sizes = (np.array((temp_series / temp_series.sum())*100))
            fig = px.pie(dfself, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Self-Employment?')
            fig.update_layout(
                title='Self Employment?', title_x=0.5
            )
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

        with c1:
            st.markdown('This question was tailored to see the general educational level obtained by the repondents, in which they answered as follows.')
            dfE = dfmale['Educational Level']
            countE= dfE.value_counts()
            trace = go.Bar(
                y=countE.index, text = countE.values,  textposition='auto',
                x=countE.values,
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = countE.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ), orientation ='h')

            layout = go.Layout(title='Educational Level of Respondents', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
            data = [trace]
            fig = go.Figure(data=data, layout=layout)
            fig.update_layout(
            autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig)



        with c3:
            st.write('')
            st.write('')
            st.markdown('This cloud highlights the most frequently mentioned job titles when respondents who do work were asked about their job titles, in which they answered as follows.')
            st.write("##")
            st.write("##")
            # st.write("##")
            stopwords = set(STOPWORDS)
            stopwords.update(['nan','Ruby','bared','cbr','Nahr','Al','Central'])
            text1 = " ".join(review for review in dfmale['In case of employment, please mention the job title.'].astype(str))
            wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text1)
            plt.subplots(figsize = (8,8))
            plt.tight_layout(pad=1)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.show()
            st.pyplot()


    if selectgen == 'Female':
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:

            dffemale = df[df.Gender == 'Female']
            st.markdown('This question was tailored to understand the employment status of the respondents as of now, in which they answered as follows.')
            dfS = dffemale['Employment Status']
            countS= dfS.value_counts()
            trace1 = go.Bar(
                y=countS.index, text = countS.values,  textposition='auto',
                x=countS.values,
                marker=dict(color = countS.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    orientation = 'h') # width=800, height=400)

            layout1 = go.Layout(title='Employment Status', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
            data1 = [trace1]
            fig1 = go.Figure(data=data1, layout=layout1)
            fig1.update_layout(
            #autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig1)

            st.markdown('This question was tailored to understand what job search methods do the respondents employ, in which they answered as follows.')
            dfO = dffemale['In case of job search, methods used in search']
            countO= dfO.value_counts()
            trace = go.Bar(
                y=countO.index, text = countO.values,  textposition='auto',
                x=countO.values,
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = countO.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ), orientation = 'h')

            layout = go.Layout(title='Job Search Methods Adopted', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')#, width=700, height=600)
            data = [trace]
            fig = go.Figure(data=data, layout=layout)
            fig.update_layout(
            autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig)



        with c3:
            st.markdown('For those who are currently working, when asked about if the work they do is in their field, they answered as follows.')
            dfx = dffemale['In case of work (current or former), do you work in your field?']
            temp_series = dfx.value_counts()
            labels = (np.array(temp_series.index))
            sizes = (np.array((temp_series / temp_series.sum())*100))
            fig = px.pie(dfx, names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Work vs Field Relation?')
            fig.update_layout(title_x=0.5)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

            st.write('')
            st.write('')
            st.write('')
            st.markdown('This question was to understand whether the respondents preferred or were mostly in the field of self-employment, in which they answered as follows.')
            dfself = dffemale['Did you try self-employment?']
            temp_series = dfself.value_counts()
            labels = (np.array(temp_series.index))
            sizes = (np.array((temp_series / temp_series.sum())*100))
            fig = px.pie(dfself, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Self-Employment?')
            fig.update_layout(
                title='Self Employment?', title_x=0.5
            )
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

        with c1:
            st.markdown('This question was tailored to see the general educational level obtained by the repondents, in which they answered as follows.')
            dfE = dffemale['Educational Level']
            countE= dfE.value_counts()
            trace = go.Bar(
                y=countE.index, text = countE.values,  textposition='auto',
                x=countE.values,
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = countE.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ), orientation ='h')

            layout = go.Layout(title='Educational Level of Respondents', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
            data = [trace]
            fig = go.Figure(data=data, layout=layout)
            fig.update_layout(
            autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig)



        with c3:
            #st.write("Job Titles?")
            st.write('')
            st.write('')
            st.write('')
            st.markdown('This cloud highlights the most frequently mentioned job titles when respondents who do work were asked about their job titles, in which they answered as follows.')
            st.write("##")
            st.write("##")
            stopwords = set(STOPWORDS)
            stopwords.update(['nan','Ruby','bared','cbr','Nahr','Al','Central', 'Bud', 'Aqsa'])
            text1 = " ".join(review for review in dffemale['In case of employment, please mention the job title.'].astype(str))
            wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text1)
            plt.subplots(figsize = (8,8))
            plt.tight_layout(pad=1)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.show()
            st.pyplot()

    if selectgen == 'All':
        c1, c2, c3 = st.beta_columns((2, 0.5, 2))
        with c1:
            st.markdown('This question was tailored to understand the employment status of the respondents as of now, in which they answered as follows.')
            dfS = df['Employment Status']
            countS= dfS.value_counts()
            trace1 = go.Bar(
                y=countS.index, text = countS.values,  textposition='auto',
                x=countS.values,
                marker=dict(color = countS.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ),
                    orientation = 'h') # width=800, height=400)

            layout1 = go.Layout(title='Employment Status', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
            data1 = [trace1]
            fig1 = go.Figure(data=data1, layout=layout1)
            fig1.update_layout(
            #autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig1)

            st.markdown('This question was tailored to understand what job search methods do the respondents employ, in which they answered as follows.')
            dfO = df['In case of job search, methods used in search']
            countO= dfO.value_counts()
            trace = go.Bar(
                y=countO.index, text = countO.values,  textposition='auto',
                x=countO.values,
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = countO.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ), orientation = 'h')

            layout = go.Layout(title='Job Search Methods Adopted', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')#, width=700, height=600)
            data = [trace]
            fig = go.Figure(data=data, layout=layout)
            fig.update_layout(
            autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig)



        with c3:
            st.markdown('For those who are currently working, when asked about if the work they do is in their field, they answered as follows.')
            dfx = df['In case of work (current or former), do you work in your field?']
            temp_series = dfx.value_counts()
            labels = (np.array(temp_series.index))
            sizes = (np.array((temp_series / temp_series.sum())*100))
            fig = px.pie(dfx, names = labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title = 'Work vs Field Relation?')
            fig.update_layout(title_x=0.5)
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

            st.write('')
            st.write('')
            st.write('')
            st.markdown('This question was to understand whether the respondents preferred or were mostly in the field of self-employment, in which they answered as follows.')
            dfself = df['Did you try self-employment?']
            temp_series = dfself.value_counts()
            labels = (np.array(temp_series.index))
            sizes = (np.array((temp_series / temp_series.sum())*100))
            fig = px.pie(dfself, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Self-Employment?')
            fig.update_layout(
                title='Self Employment?', title_x=0.5
            )
            fig.update_traces(
            texttemplate="%{percent:.1%f}")
            st.plotly_chart(fig)

        with c1:
            st.markdown('This question was tailored to see the general educational level obtained by the repondents, in which they answered as follows.')
            dfE = df['Educational Level']
            countE= dfE.value_counts()
            trace = go.Bar(
                y=countE.index, text = countE.values,  textposition='auto',
                x=countE.values,
                marker=dict(
                #color = np.random.randn(500), #set color equal to a variable
                    color = countE.values,
                    colorscale='Tealgrn',
                    showscale=False
                    ), orientation ='h')

            layout = go.Layout(title='Educational Level of Respondents', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
            data = [trace]
            fig = go.Figure(data=data, layout=layout)
            fig.update_layout(
            autosize=False,
            width=750,
            height=500)
            st.plotly_chart(fig)



        with c3:
            #st.write("Job Titles?")
            st.write('')
            st.write('')
            st.markdown('This cloud highlights the most frequently mentioned job titles when respondents who do work were asked about their job titles, in which they answered as follows.')
            st.write("##")
            st.write("##")
            stopwords = set(STOPWORDS)
            stopwords.update(['nan','Ruby','bared','cbr','Nahr','Al','Central','Bud'])
            text1 = " ".join(review for review in df['In case of employment, please mention the job title.'].astype(str))
            wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text1)
            plt.subplots(figsize = (8,8))
            plt.tight_layout(pad=1)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.show()
            st.pyplot()


if pick == "Industries, Training, and More":
    import nltk
    from nltk.tokenize import word_tokenize
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    import string
    stopwords = nltk.corpus.stopwords.words('english')

    st.title('Industries, Job Titles, and Training Concerns')
    st.markdown('Here we can see what industries the respondents work mostly in.')
    st.markdown('We can also understand their willingness for training, and in what particular fields as well they wish to do so.')
    st.markdown('In addition, we can assess the reasons behind their rejection of offers and what whether they look to training  opportunities or they do not.')
    st.write('##')
    c1, c2, c3 = st.beta_columns((2, 0.5, 2))
    with c1:
        st.markdown('For the portion of our respondents who do work, when asked what sector do they work in, they answered as follows.')
        df['Sector'] = df['If working, please mention the sector'].str.extract('([A-Z]\w{0,})', expand=True)
        temp=df.Sector.fillna("0")
        df['Sector2'] = pd.np.where(temp.str.contains("Local"), "Local NGOs",
                    pd.np.where(temp.str.contains("Tutoring"), "Education",
                    pd.np.where(temp.str.contains("Art"), "Art and Culture",
                    pd.np.where(temp.str.contains("Manufacturing"), "Industry and Manufacturing",
                    pd.np.where(temp.str.contains("International"), "International NGOs",
                    pd.np.where(temp.str.contains("Social"), "Social",
                    pd.np.where(temp.str.contains("Dental"), "Health",
                    pd.np.where(temp.str.contains("Gas"), "Industry and Manufacturing",
                    pd.np.where(temp.str.contains("Engineering"), "Industry and Manufacturing",
                    pd.np.where(temp.str.contains("Commercial"), "Social",
                    pd.np.where(temp.str.contains("Painter"), "Art and Culture",
                    pd.np.where(temp.str.contains("Photography"), "Photography",
                    pd.np.where(temp.str.contains("Women"), "Cosmetics", "Other")))))))))))))
        df.Sector2 = df.Sector2[~(df.Sector2.str.contains("Other"))]

        dfm = df['Sector2']
        countm= dfm.value_counts()
        trace = go.Bar(
            x=countm.index,
            y=countm.values, text = countm.values,  textposition='auto',
            marker=dict(
            #color = np.random.randn(500), #set color equal to a variable
                color = countm.values,
                colorscale='Tealgrn',
                showscale=False
                ),
                )

        layout = go.Layout(title='Industries Mentioned', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        fig.update_layout(
        autosize=False,
        width=750,
        height=650)
        st.plotly_chart(fig)

    with c3:
        st.write('For the portion of our respondents who do work, when asked what job titles they hold, they answered as follows.')
        dfY = df['In case of employment, please mention the job title.']
        dfY1 = dfY[dfY.notnull()]
        dfY2 = dfY1[dfY1 != "Central Ruby"]
        dfY3 = dfY2[dfY2 != "Cbr"]
        job = dfY3

        def matcher(x):
            for i in job:
                if i.lower() in x.lower():
                    return i
            else:
                return np.nan

        df['JobTitle'] = job.apply(matcher)
        df['JobTitle'].value_counts()
        jobno = df['JobTitle'].dropna()
        jobno1 = jobno.copy()
        jobno1 = np.where(jobno.str.contains("Volunteer"), "Volunteer",
        np.where(jobno.str.contains("Tutor"), "Teacher",
        np.where(jobno.str.contains("Teaching"), "Teacher",
        np.where(jobno.str.contains("Teacher"), "Teacher",
        np.where(jobno.str.contains("teacher"), "Teacher",
        np.where(jobno.str.contains("Secretary"), "Secretary",
        np.where(jobno.str.contains("Accounting"), "Accountant",
        np.where(jobno.str.contains("Cashier"), "Accountant",
        np.where(jobno.str.contains("employee"), "General Employee",
        np.where(jobno.str.contains("worker"), "General Employee",
        np.where(jobno.str.contains("Waiter"), "Waiter",
        np.where(jobno.str.contains("Cashier"), "Accountant",
        np.where(jobno.str.contains("Women"), "Cosmetics Specialist",
        np.where(jobno.str.contains("rights"), "Social Worker",
        np.where(jobno.str.contains("Accountant"), "Accountant",
        np.where(jobno.str.contains("Journalist"), "Journalist",
        np.where(jobno.str.contains("Photograph"), "Photographer",
        np.where(jobno.str.contains("Photography"), "Photographer",
        np.where(jobno.str.contains("Wedding"), "Wedding Planner",
        np.where(jobno.str.contains("Painter"), "Painter",
        np.where(jobno.str.contains("Social"), "Social Worker",
        np.where(jobno.str.contains("Anera"), "Social Worker",
        np.where(jobno.str.contains("Sterilization"), "Clinic Assistant",
        np.where(jobno.str.contains("Dental"), "Clinic Assistant", "Sales Assistant"))))))))))))))))))))))))


        jobdf = pd.DataFrame(jobno1, columns = ['Job Title'])
        a1 = jobdf['Job Title'].value_counts()
        x1 = list(a1.index)
        y1 = list(a1)

        data1 = [go.Bar(
           x = x1,
           y = y1, text = y1,  textposition='auto',
           marker=dict(
           #color = np.random.randn(500), #set color equal to a variable
               color = a1.values,
               colorscale='Tealgrn',
               showscale=False
               ),
               )
        ]
        layout = go.Layout(title='Job Titles', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        fig = go.Figure(data=data1, layout=layout)
        fig.update_layout(
        autosize=False,
        width=750,
        height=650)
        st.plotly_chart(fig)

    with c1:
        st.write('Here, our respondents were asked whether they volunteer or engagine in trainings when possible and available.')
        dfini = df['Do you look up to volunteer or train?']
        temp_series = dfini.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dfini, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Self-Employment?')
        fig.update_layout(
            title='Do You Look to Volunteer or Train?'
        )
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        fig.update_layout(width=800, height=600)
        st.plotly_chart(fig)

    with c3:
        st.write('The respondents were asked whether they had ever rejected an employment opprtunity, and they had answered as follows.')
        dfrej = df['Have you ever rejected any offer or employment opportunity?']
        temp_series = dfrej.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dfrej, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Rejection of Opportunity??')
        fig.update_layout(
            title='Have You Rejected A Job Opportunity Before?'
        )
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        fig.update_layout(width=800, height=600)
        st.plotly_chart(fig)

    with c3:
        st.write('For the portion of our respondents who said they had rejected it, we wanted to dig a little deeper and understand why they did so.')
        dfrej1 = temp = df['In case of yes, please specify the cause']
        dfrej2 = dfrej1.dropna()

        dfrejs = dfrej2.astype(str)

        def matcher(x):
            for i in dfrejs:
                if i.lower() in x.lower():
                    return i
            else:
                return np.nan

        df['Reasons For Giving Up Opportunities'] = dfrejs.apply(matcher)

        dfreason = df['Reasons For Giving Up Opportunities']
        dfreasonn = dfreason.dropna()

        dfreason1 = np.where(dfreasonn.str.contains("wage"), "Salary",
        np.where(dfreasonn.str.contains("Salary"), "Salary",
        np.where(dfreasonn.str.contains("time"), "Time Inadequate and Conflicting",
        np.where(dfreasonn.str.contains("suitable"), "Not In Field",
        np.where(dfreasonn.str.contains("field"), "Not In Field",
        np.where(dfreasonn.str.contains("hours"), "Working Hours",
        np.where(dfreasonn.str.contains("Nationality"), "Nationality",
        np.where(dfreasonn.str.contains("Family"), "Personal Reasons","Other"))))))))

        dfreason2 = pd.DataFrame(dfreason1, columns = ['Reason for Giving Up Job Opportunity'])
        a1 = dfreason2['Reason for Giving Up Job Opportunity'].value_counts()

        x1 = list(a1.index)
        y1 = list(a1)

        data1 = [go.Bar(
           x = x1,
           y = y1, text = y1,  textposition='auto',
           marker=dict(
           #color = np.random.randn(500), #set color equal to a variable
               color = a1.values,
               colorscale='Tealgrn',
               showscale=False
               ),
               )
        ]
        layout = go.Layout(title='Reasons for Rejection', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        fig = go.Figure(data=data1, layout=layout)
        fig.update_layout(
        autosize=False,
        width=750,
        height=650)
        st.plotly_chart(fig)

    with c1:
        st.write('For the portion of our respondents who said they would like more training, when asked in what, they answered as follows.')
        dfyes = df['If yes, in what field?']
        dfyess = dfyes.astype('string')
        dfye = dfyess[dfyess != "<NA"]
        #dfye
        def matcher(r):
            for i in dfye:
                if i.lower() in r.lower():
                    return i
            else:
                return np.nan

        df['Training Needs'] = dfye.apply(matcher)
        dftrains1 = df['Training Needs'].dropna()
        dfTtext = dftrains1.astype(str)
        # in the below code if the word isnt in stop words then we want it.
        def cleaning_stopwords(text):
            return " ".join([word for word in str(text).split() if word not in stopwords])

        dfTtext = dfTtext.apply(lambda message : cleaning_stopwords(message))
        dfTtext1= dfTtext.str.lower()
        temp = dfTtext1
        areas1 = np.where(temp.str.contains("social") ,"Social Skills",
                  np.where(temp.str.contains("work") ,"Social Skills",
               np.where(temp.str.contains("sociology") ,"Social Skills",
               np.where(temp.str.contains("volunteering") ,"Social Skills",
               np.where(temp.str.contains("volunteer") ,"Social Skills",
               np.where(temp.str.contains("communcation") ,"Communication",
               np.where(temp.str.contains("coding"), "Computer Skills",
               np.where(temp.str.contains('computer'), "Computer Skills",
               np.where(temp.str.contains('digital'), "Computer Skills",
               np.where(temp.str.contains('technological'), "Computer Skills",
               np.where(temp.str.contains('technology'), "Computer Skills",
               np.where(temp.str.contains('electronics'), "Computer Skills",
               np.where(temp.str.contains('programming'), "Computer Skills",
               np.where(temp.str.contains("business"), "Business and Leadership Skills",
               np.where(temp.str.contains('leadership'), "Business and Leadership Skills",
               np.where(temp.str.contains('accounting'), "Business and Leadership Skills",
               np.where(temp.str.contains("management"), "Business and Leadership Skills",
               np.where(temp.str.contains("editing"), "Photography and Design",
               np.where(temp.str.contains("art"), "Art",
               np.where(temp.str.contains('photography'), "Photography and Design",
               np.where(temp.str.contains('design'), "Photography and Design",
               np.where(temp.str.contains("life"), "Self Development Skills",
               np.where(temp.str.contains("self"), "Self Development Skills",
               np.where(temp.str.contains('free'), "Self Development Skills",
               np.where(temp.str.contains("photo"), "Photography and Design",
               np.where(temp.str.contains('nalist'), "Photography and Design",
               np.where(temp.str.contains('drawing'), "Photography and Design",
               np.where(temp.str.contains("education"), "Teaching Skills",
               np.where(temp.str.contains('teacher'), "Teaching Skills",
               np.where(temp.str.contains("teach"), "Teaching Skills",
               np.where(temp.str.contains("tutor"), "Teaching Skills",
               np.where(temp.str.contains("medical"), "Medical Skills",
               np.where(temp.str.contains('clinic'), "Medical Skills",
               np.where(temp.str.contains('nurs'), "Medical Skills",
               np.where(temp.str.contains('dental'), "Medical Skills",
               np.where(temp.str.contains("language"), "Language Skills",
               np.where(temp.str.contains('english'), "Language Skills",
               np.where(temp.str.contains('building'), "Engineering ",
                np.where(temp.str.contains('construction'), "Engineering",
                np.where(temp.str.contains('engineering'), "Engineering","Life Skills"))))))))))))))))))))))))))))))))))))))))

        dftr = pd.DataFrame(areas1, columns=['Needs'])
        az = dftr['Needs'].value_counts()

        xz = list(az.index)
        yz = list(az)

        dataz = [go.Bar(
           x = xz,
           y = yz, text = yz,  textposition='auto',
           marker=dict(
           #color = np.random.randn(500), #set color equal to a variable
               color = az.values,
               colorscale='Tealgrn',
               showscale=False
               ),
               )
        ]
        layoutz = go.Layout(title='Training Needed In', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        fig = go.Figure(data=dataz, layout=layoutz)
        fig.update_layout(
        autosize=False,
        width=800,
        height=650)
        st.plotly_chart(fig)

# import nltk
# from nltk.corpus import stopwords
# import string
# stopwords = nltk.corpus.stopwords.words('english')

# if pick == 'Challenges and Obstacles: Implementing LDA and Topic Modelling':
#
#     st.title('Challenges and Obstacles')
#     st.markdown('This page is dedicated to highlight the obstacles that the respondents stated they face in their employment journey.')
#     add_selectbox = st.sidebar.radio(
#     'Click any of the below to see how we arrived at analyzing the qualitative responses, particularly those for challenges.',
#     ('None', 'LDA: Dominant Topics', 'Word Cloud and Challenges'))
#     c1, c2, c3 = st.beta_columns((2, 0.5, 2))
#     chal = df['What are the main challenges you face in work/job search?']
#     chal1=chal.dropna()
#     chal2 = chal1.astype(str)
#
#     def matcher(f):
#         for i in chal2:
#             if i.lower() in f.lower():
#                 return i
#         else:
#             return np.nan
#
#     df['Challenges Faced'] = chal2.apply(matcher)
#     dfcal = df['Challenges Faced'].dropna()
#     chal01 = dfcal.astype(str)
#     all_text1 = chal01.str.cat(sep = ' ')
#     all_text2 = all_text1.lower()
#
#     # in the below code if the word isnt in stop words then we want it.
#     def cleaning_stopwords(text):
#         return " ".join([word for word in str(text).split() if word not in stopwords])
#
#     dfTtext01 = chal01.apply(lambda message : cleaning_stopwords(message))
#     dfTtext02= dfTtext01.str.lower()
#
#     def sent_to_words(sentences):
#         for sent in sentences:
#             sent = gensim.utils.simple_preprocess(str(sent), deacc=True)
#             yield(sent)
#
#     data2 = dfTtext02.values.tolist()
#     data_words2 = list(sent_to_words(data2))
#
#     # Build the bigram and trigram models
#     bigram = gensim.models.Phrases(data_words2, min_count=5, threshold=10) # higher threshold fewer phrases.
#     trigram = gensim.models.Phrases(bigram[data_words2], threshold=10)
#     bigram_mod = gensim.models.phrases.Phraser(bigram)
#     trigram_mod = gensim.models.phrases.Phraser(trigram)
#
#     def process_words(texts, stop_words=stopwords, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
#     #"""Remove Stopwords, Form Bigrams, Trigrams and Lemmatization"""
#         texts = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]
#         texts = [bigram_mod[doc] for doc in texts]
#         texts = [trigram_mod[bigram_mod[doc]] for doc in texts]
#         texts_out = []
#
#         nlp = spacy.load(("en_core_web_sm"), disable=['parser', 'ner'])
#
#         for sent in texts:
#             doc = nlp(" ".join(sent))
#             texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
#             # remove stopwords once more after lemmatization
#             texts_out = [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts_out]
#         return texts_out
#
#     data_ready2 = process_words(data_words2)  # processed Text Data!
#
#         # Create Dictionary
#     id2word = corpora.Dictionary(data_ready2)
#
#     # Create Corpus: Term Document Frequency
#     corpus = [id2word.doc2bow(text) for text in data_ready2]
#
#     # Build LDA model
#     lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
#                                                id2word=id2word,
#                                                num_topics=5,
#                                                random_state=100,
#                                                update_every=1,
#                                                chunksize=10,
#                                                passes=10,
#                                                alpha='symmetric',
#                                                iterations=100,
#                                                per_word_topics=True)
#
#     #with c1:
#             #Here we can ask the question: what is the Dominant topic and its percentage contribution in each document?
#     def format_topics_sentences(ldamodel=None, corpus=corpus, texts=data2):
#         # Init output
#         sent_topics_df = pd.DataFrame()
#
#         # Get main topic in each document
#         for i, row_list in enumerate(ldamodel[corpus]):
#             row = row_list[0] if ldamodel.per_word_topics else row_list
#             # print(row)
#             row = sorted(row, key=lambda x: (x[1]), reverse=True)
#             # Get the Dominant topic, Perc Contribution and Keywords for each document
#             for j, (topic_num, prop_topic) in enumerate(row):
#                 if j == 0:  # => dominant topic
#                     wp = ldamodel.show_topic(topic_num)
#                     topic_keywords = ", ".join([word for word, prop in wp])
#                     sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
#                 else:
#                     break
#         sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']
#
#         # Add original text to the end of the output
#         contents = pd.Series(texts)
#         sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
#         return(sent_topics_df)
#
#
#     df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model, corpus=corpus, texts=data_ready2)
#
#     # Format
#     df_dominant_topic = df_topic_sents_keywords.reset_index()
#     df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
#
#
# #with c3:
#     #Plotting a world cloud for the top 4 topics with weighted size to words frequency proportionality (the larger the word the more frequently it occurs)
#
#     import matplotlib.colors as mcolors
#
#     #cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]  # more colors: 'mcolors.XKCD_COLORS'
#
#     cloud = WordCloud(stopwords=stopwords,
#                       background_color='white',
#                       width=2500,
#                       height=1800,
#                       max_words=10)
#                       # colormap='tab10',
#                       # color_func=lambda *args, **kwargs: cols[i],
#                       # prefer_horizontal=1.0)
#
#     topics = lda_model.show_topics(formatted=False)
#
#     fig, axes = plt.subplots(2, 2, figsize=(10,10), sharex=True, sharey=True)
#
#     for i, ax in enumerate(axes.flatten()):
#         fig.add_subplot(ax)
#         topic_words = dict(topics[i][1])
#         cloud.generate_from_frequencies(topic_words, max_font_size=300)
#         plt.gca().imshow(cloud)
#         plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
#         plt.gca().axis('off')
#
#
#     plt.subplots_adjust(wspace=0, hspace=0)
#     plt.axis('off')
#     plt.margins(x=0, y=0)
#     plt.tight_layout()
#     plt.show()
#
#     if add_selectbox == 'None':
#                 ""
#
#     if add_selectbox == 'LDA: Dominant Topics':
#         st.markdown('LDA: Dominant Topics')
#
#
#         st.write(df_dominant_topic[:20])
#
#         st.pyplot()
#
#     if add_selectbox == 'Word Cloud and Challenges':
#         #st.write('The word cloud has allowed us to get a general idea about the challenges that are faced by the respondents. But we cannot stop here.')
#
#         with c1:
#             st.write("##")
#             st.write("##")
#             st.write("##")
#             wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=700, height=500).generate(all_text2)
#             plt.subplots(figsize = (8,8))
#             plt.tight_layout(pad=0)
#             plt.imshow(wordcloud)
#             plt.axis('off')
#             plt.show()
#             st.pyplot()
#
#         with c3:
#
#             challenges= np.where(chal01.str.contains('Nationality' or 'Nepotism' or "nationality") ,"Nationality",
#                    np.where(chal01.str.contains('experience') ,"Experience",
#                    np.where(chal01.str.contains('wages') ,"Wages",
#                    np.where(chal01.str.contains('low') ,"Wages",
#                    np.where(chal01.str.contains('jobs' or 'mismatch') ,"Finding Jobs",
#                    np.where(chal01.str.contains('shortage') ,"Shortage of Jobs",
#                    np.where(chal01.str.contains('Nationality' or "Racism" or "Racial") ,"Discrimination",
#                    np.where(chal01.str.contains('Nationality' or "Racism" or "Racial") ,"Discrimination",
#                    np.where(chal01.str.contains('favoritism') ,"Discrimination",
#                    np.where(chal01.str.contains('situation') ,"State of Country",
#                    np.where(chal01.str.contains('Nationality') ,"Working Hours",
#                    np.where(chal01.str.contains('female') ,"Gender",
#                    np.where(chal01.str.contains('gender') ,"Gender",
#                    np.where(chal01.str.contains('lack') ,"Discrimination",
#                    np.where(chal01.str.contains('Palestinian') ,"Nationality",
#                    np.where(chal01.str.contains('Gender') ,"Gender",
#                    np.where(chal01.str.contains('Incompatibility') ,"Education Conflict",
#                    np.where(chal01.str.contains('Lebanon') ,"State of Country", "Shortage of Jobs"))))))))))))))))))
#
#             dfchal = pd.DataFrame(challenges, columns=['Challenges'])
#             az = dfchal['Challenges'].value_counts()
#
#             xz = list(az.index)
#             yz = list(az)
#
#             dataz = [go.Bar(
#                x = xz,
#                y = yz, text = yz,  textposition='auto',
#                marker=dict(
#                #color = np.random.randn(500), #set color equal to a variable
#                    color = az.values,
#                    colorscale='Tealgrn',
#                    showscale=False
#                    ),
#                    )
#             ]
#             layoutz = go.Layout(title='Main Challenges Faced', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
#             fig = go.Figure(data=dataz, layout=layoutz)
#             fig.update_layout(
#             autosize=False,
#             width=800,
#             height=650)
#             st.plotly_chart(fig)

    # if add_selectbox == 'Topic Modelling: Most Frequent Words':
    #     st.markdown('Topic Modelling: Most Frequent Words')
    #     import pyLDAvis
    #     import pyLDAvis.gensim_models as gensimvis
    #     #pyLDAvis.enable_notebook()
    #     vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, dictionary=lda_model.id2word)
    #     vis

if pick =="Executive Summary":
    st.title('Executive Summary: Conclusion and Recommendations')
    st.markdown('All the analysis has led us to see the general perception of youth employability with direct feedback from the individuals themselves.')
    st.markdown('We saw general trends as well as achieved our objective, which was, to see an overview of what training needs are missing to schedule and assign the designated training regimes.')
    st.markdown('We also identified the biggest challenges that they encountered in order for us to acquaint and offer assistance in the areas that assistance can be provided')
    # selectlocation = st.sidebar.selectbox('Please select one option to view on input based on location', ('North', 'Mount Lebanon', 'Saida', 'Tyre', 'Beirut', 'Bekaa'))
    # selectgender = st.sidebar.selectbox('Please select one option to view on input based on gender', ('Male', 'Female', 'All'))
    chal = df['What are the main challenges you face in work/job search?']
    chal1=chal.dropna()
    chal2 = chal1.astype(str)

    def matcher(f):
        for i in chal2:
            if i.lower() in f.lower():
                return i
        else:
            return np.nan

    df['Challenges Faced'] = chal2.apply(matcher)
    dfcal = df['Challenges Faced'].dropna()
    chal01 = dfcal.astype(str)
    all_text1 = chal01.str.cat(sep = ' ')
    all_text2 = all_text1.lower()

    # in the below code if the word isnt in stop words then we want it.
    nltk.download('stopwords')
    def cleaning_stopwords(text):
        return " ".join([word for word in str(text).split() if word not in stopwords])

    dfTtext01 = chal01.apply(lambda message : cleaning_stopwords(message))
    dfTtext02= dfTtext01.str.lower()
    c1, c2, c3 = st.beta_columns((2,0.5,2))
    with c1:
        challenges= np.where(chal01.str.contains('Nationality' or 'Nepotism' or "nationality") ,"Nationality",
               np.where(chal01.str.contains('experience') ,"Experience",
               np.where(chal01.str.contains('wages') ,"Wages",
               np.where(chal01.str.contains('low') ,"Wages",
               np.where(chal01.str.contains('jobs' or 'mismatch') ,"Finding Jobs",
               np.where(chal01.str.contains('shortage') ,"Shortage of Jobs",
               np.where(chal01.str.contains('Nationality' or "Racism" or "Racial") ,"Discrimination",
               np.where(chal01.str.contains('Nationality' or "Racism" or "Racial") ,"Discrimination",
               np.where(chal01.str.contains('favoritism') ,"Discrimination",
               np.where(chal01.str.contains('situation') ,"State of Country",
               np.where(chal01.str.contains('Nationality') ,"Working Hours",
               np.where(chal01.str.contains('female') ,"Gender",
               np.where(chal01.str.contains('gender') ,"Gender",
               np.where(chal01.str.contains('lack') ,"Discrimination",
               np.where(chal01.str.contains('Palestinian') ,"Nationality",
               np.where(chal01.str.contains('Gender') ,"Gender",
               np.where(chal01.str.contains('Incompatibility') ,"Education Conflict",
               np.where(chal01.str.contains('Lebanon') ,"State of Country", "Shortage of Jobs"))))))))))))))))))

        dfchal = pd.DataFrame(challenges, columns=['Challenges'])
        az = dfchal['Challenges'].value_counts()

        xz = list(az.index)
        yz = list(az)

        dataz = [go.Bar(
           x = xz,
           y = yz, text = yz,  textposition='auto',
           marker=dict(
           #color = np.random.randn(500), #set color equal to a variable
               color = az.values,
               colorscale='Tealgrn',
               showscale=False
               ),
               )
        ]
        layoutz = go.Layout(title='Main Challenges Faced', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        fig = go.Figure(data=dataz, layout=layoutz)
        fig.update_layout(
        autosize=False,
        width=800,
        height=650)
        st.plotly_chart(fig)

    with c3:
        temp_series = dfchal.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dfchal, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Challenges Stated?')
        fig.update_layout(
            title='Percentages of Challenges Stated', title_x=0.5
        )
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        fig.update_layout(width=800, height=600)
        st.plotly_chart(fig)
    with c1:
        dfyes = df['If yes, in what field?']
        dfyess = dfyes.astype('string')
        dfye = dfyess[dfyess != "<NA"]
        #dfye
        def matcher(r):
            for i in dfye:
                if i.lower() in r.lower():
                    return i
            else:
                return np.nan

        df['Training Needs'] = dfye.apply(matcher)
        dftrains1 = df['Training Needs'].dropna()
        dfTtext = dftrains1.astype(str)
        # in the below code if the word isnt in stop words then we want it.
        def cleaning_stopwords(text):
            return " ".join([word for word in str(text).split() if word not in stopwords])

        dfTtext = dfTtext.apply(lambda message : cleaning_stopwords(message))
        dfTtext1= dfTtext.str.lower()
        temp = dfTtext1
        areas1 = np.where(temp.str.contains("social") ,"Social Skills",
                  np.where(temp.str.contains("work") ,"Social Skills",
               np.where(temp.str.contains("sociology") ,"Social Skills",
               np.where(temp.str.contains("volunteering") ,"Social Skills",
               np.where(temp.str.contains("volunteer") ,"Social Skills",
               np.where(temp.str.contains("communcation") ,"Communication",
               np.where(temp.str.contains("coding"), "Computer Skills",
               np.where(temp.str.contains('computer'), "Computer Skills",
               np.where(temp.str.contains('digital'), "Computer Skills",
               np.where(temp.str.contains('technological'), "Computer Skills",
               np.where(temp.str.contains('technology'), "Computer Skills",
               np.where(temp.str.contains('electronics'), "Computer Skills",
               np.where(temp.str.contains('programming'), "Computer Skills",
               np.where(temp.str.contains("business"), "Business and Leadership Skills",
               np.where(temp.str.contains('leadership'), "Business and Leadership Skills",
               np.where(temp.str.contains('accounting'), "Business and Leadership Skills",
               np.where(temp.str.contains("management"), "Business and Leadership Skills",
               np.where(temp.str.contains("editing"), "Photography and Design",
               np.where(temp.str.contains("art"), "Art",
               np.where(temp.str.contains('photography'), "Photography and Design",
               np.where(temp.str.contains('design'), "Photography and Design",
               np.where(temp.str.contains("life"), "Self Development Skills",
               np.where(temp.str.contains("self"), "Self Development Skills",
               np.where(temp.str.contains('free'), "Self Development Skills",
               np.where(temp.str.contains("photo"), "Photography and Design",
               np.where(temp.str.contains('nalist'), "Photography and Design",
               np.where(temp.str.contains('drawing'), "Photography and Design",
               np.where(temp.str.contains("education"), "Teaching Skills",
               np.where(temp.str.contains('teacher'), "Teaching Skills",
               np.where(temp.str.contains("teach"), "Teaching Skills",
               np.where(temp.str.contains("tutor"), "Teaching Skills",
               np.where(temp.str.contains("medical"), "Medical Skills",
               np.where(temp.str.contains('clinic'), "Medical Skills",
               np.where(temp.str.contains('nurs'), "Medical Skills",
               np.where(temp.str.contains('dental'), "Medical Skills",
               np.where(temp.str.contains("language"), "Language Skills",
               np.where(temp.str.contains('english'), "Language Skills",
               np.where(temp.str.contains('building'), "Engineering ",
                np.where(temp.str.contains('construction'), "Engineering",
                np.where(temp.str.contains('engineering'), "Engineering","Life Skills"))))))))))))))))))))))))))))))))))))))))

        dftr = pd.DataFrame(areas1, columns=['Needs'])
        az = dftr['Needs'].value_counts()

        xz = list(az.index)
        yz = list(az)

        dataz = [go.Bar(
           x = xz,
           y = yz, text = yz,  textposition='auto',
           marker=dict(
           #color = np.random.randn(500), #set color equal to a variable
               color = az.values,
               colorscale='Tealgrn',
               showscale=False
               ),
               )
        ]
        layoutz = go.Layout(title='Training Needed In', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        fig = go.Figure(data=dataz, layout=layoutz)
        fig.update_layout(
        autosize=False,
        width=800,
        height=650)
        st.plotly_chart(fig)
    with c3:
        st.write('##')
        st.write('')
        temp_series = dftr.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dftr, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Training Needs')
        fig.update_layout(
            title='Percentages of Training Needs Stated', title_x=0.5
        )
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        fig.update_layout(width=800, height=600)
        st.plotly_chart(fig)

    with c1:
        dfrej1 = temp = df['In case of yes, please specify the cause']
        dfrej2 = dfrej1.dropna()

        dfrejs = dfrej2.astype(str)

        def matcher(x):
            for i in dfrejs:
                if i.lower() in x.lower():
                    return i
            else:
                return np.nan

        df['Reasons For Giving Up Opportunities'] = dfrejs.apply(matcher)

        dfreason = df['Reasons For Giving Up Opportunities']
        dfreasonn = dfreason.dropna()

        dfreason1 = np.where(dfreasonn.str.contains("wage"), "Salary",
        np.where(dfreasonn.str.contains("Salary"), "Salary",
        np.where(dfreasonn.str.contains("time"), "Time Inadequate and Conflicting",
        np.where(dfreasonn.str.contains("suitable"), "Not In Field",
        np.where(dfreasonn.str.contains("field"), "Not In Field",
        np.where(dfreasonn.str.contains("hours"), "Working Hours",
        np.where(dfreasonn.str.contains("Nationality"), "Nationality",
        np.where(dfreasonn.str.contains("Family"), "Personal Reasons","Other"))))))))

        dfreason2 = pd.DataFrame(dfreason1, columns = ['Reason for Giving Up Job Opportunity'])
        a1 = dfreason2['Reason for Giving Up Job Opportunity'].value_counts()

        x1 = list(a1.index)
        y1 = list(a1)

        data1 = [go.Bar(
           x = x1,
           y = y1, text = y1,  textposition='auto',
           marker=dict(
           #color = np.random.randn(500), #set color equal to a variable
               color = a1.values,
               colorscale='Tealgrn',
               showscale=False
               ),
               )
        ]
        layout = go.Layout(title='Reasons for Rejection', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        fig = go.Figure(data=data1, layout=layout)
        fig.update_layout(
        autosize=False,
        width=750,
        height=650)
        st.plotly_chart(fig)

    with c3:
        st.write('##')
        st.write('')
        temp_series = dfreason2.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dfreason2, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Reasons for Rejection')
        fig.update_layout(
            title='Percentages of Rejection Reasons Stated', title_x=0.5
        )
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        fig.update_layout(width=800, height=600)
        st.plotly_chart(fig)

    with c1:
        dfY = df['In case of employment, please mention the job title.']
        dfY1 = dfY[dfY.notnull()]
        dfY2 = dfY1[dfY1 != "Central Ruby"]
        dfY3 = dfY2[dfY2 != "Cbr"]
        job = dfY3

        def matcher(x):
            for i in job:
                if i.lower() in x.lower():
                    return i
            else:
                return np.nan

        df['JobTitle'] = job.apply(matcher)
        df['JobTitle'].value_counts()
        jobno = df['JobTitle'].dropna()
        jobno1 = jobno.copy()
        jobno1 = np.where(jobno.str.contains("Volunteer"), "Volunteer",
        np.where(jobno.str.contains("Tutor"), "Teacher",
        np.where(jobno.str.contains("Teaching"), "Teacher",
        np.where(jobno.str.contains("Teacher"), "Teacher",
        np.where(jobno.str.contains("teacher"), "Teacher",
        np.where(jobno.str.contains("Secretary"), "Secretary",
        np.where(jobno.str.contains("Accounting"), "Accountant",
        np.where(jobno.str.contains("Cashier"), "Accountant",
        np.where(jobno.str.contains("employee"), "General Employee",
        np.where(jobno.str.contains("worker"), "General Employee",
        np.where(jobno.str.contains("Waiter"), "Waiter",
        np.where(jobno.str.contains("Cashier"), "Accountant",
        np.where(jobno.str.contains("Women"), "Cosmetics Specialist",
        np.where(jobno.str.contains("rights"), "Social Worker",
        np.where(jobno.str.contains("Accountant"), "Accountant",
        np.where(jobno.str.contains("Journalist"), "Journalist",
        np.where(jobno.str.contains("Photograph"), "Photographer",
        np.where(jobno.str.contains("Photography"), "Photographer",
        np.where(jobno.str.contains("Wedding"), "Wedding Planner",
        np.where(jobno.str.contains("Painter"), "Painter",
        np.where(jobno.str.contains("Social"), "Social Worker",
        np.where(jobno.str.contains("Anera"), "Social Worker",
        np.where(jobno.str.contains("Sterilization"), "Clinic Assistant",
        np.where(jobno.str.contains("Dental"), "Clinic Assistant", "Sales Assistant"))))))))))))))))))))))))


        jobdf = pd.DataFrame(jobno1, columns = ['Job Title'])
        a1 = jobdf['Job Title'].value_counts()
        x1 = list(a1.index)
        y1 = list(a1)

        data1 = [go.Bar(
           x = x1,
           y = y1, text = y1,  textposition='auto',
           marker=dict(
           #color = np.random.randn(500), #set color equal to a variable
               color = a1.values,
               colorscale='Tealgrn',
               showscale=False
               ),
               )
        ]
        layout = go.Layout(title='Job Titles', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')
        fig = go.Figure(data=data1, layout=layout)
        fig.update_layout(
        autosize=False,
        width=750,
        height=650)
        st.plotly_chart(fig)

    with c3:
        st.write('##')
        st.write('')
        temp_series = jobdf.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(jobdf, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Job Titles Mentioned')
        fig.update_layout(
            title='Percentages of Job Titles Stated', title_x=0.5
        )
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        fig.update_layout(width=800, height=600)
        st.plotly_chart(fig)

    with c1:
        dfO = df['In case of job search, methods used in search']
        countO= dfO.value_counts()
        trace = go.Bar(
            y=countO.index, text = countO.values,  textposition='auto',
            x=countO.values,
            marker=dict(
            #color = np.random.randn(500), #set color equal to a variable
                color = countO.values,
                colorscale='Tealgrn',
                showscale=False
                ), orientation = 'h')

        layout = go.Layout(title='Job Search Methods Adopted', title_x=0.5, plot_bgcolor='rgba(0,0,0,0)')#, width=700, height=600)
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        fig.update_layout(
        autosize=False,
        width=750,
        height=500)
        st.plotly_chart(fig)

    with c3:
        st.write('##')
        st.write('')
        temp_series = dfO.value_counts()
        labels = (np.array(temp_series.index))
        sizes = (np.array((temp_series / temp_series.sum())*100))
        fig = px.pie(dfO, names=labels, values=sizes, color_discrete_sequence=px.colors.sequential.Tealgrn, hole=0.5, title='Job Search Methods Mentioned')
        fig.update_layout(
            title='Percentages of Job Search Methods Stated', title_x=0.5
        )
        fig.update_traces(
        texttemplate="%{percent:.1%f}")
        fig.update_layout(width=800, height=600)
        st.plotly_chart(fig)
    st.write('For final words, this analysis depicts what is a small representation of what could be a more elaborate and inclusive coverage however given the scope of the project and the objectives on hand, it bodes extremely well and answers the main questions we wished to answer.')
