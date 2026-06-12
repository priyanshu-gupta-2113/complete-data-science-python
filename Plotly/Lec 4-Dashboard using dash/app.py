import pandas as pd
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
import dash
import numpy as npl
import dash.dependencies 
from dash.dependencies import Input,Output
# External CSS stylesheet (Bootstrap is css framework)
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]


patients=pd.read_csv('/Users/priyanshugupta/Desktop/plotly/corona/IndividualDetails.csv')
total=patients.shape[0] ## total entries 
active=patients[patients['current_status']=='Hospitalized'].shape[0]
recovered=patients[patients['current_status']=='Recovered'].shape[0]
deaths=patients[patients['current_status']=='Deceased'].shape[0]
pbar=patients['detected_state'].value_counts().reset_index()

options=[
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
]
## write the pandas code above the app

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)
## app.layout = html.Div([],className='container') ## You have created a div jiske andar you will create more divs

'''
app.Layout=html.Div([
html.Div([],className='row'),
html.Div([],className='row'),
html.Div([],className='row')
],className='container)
'''

'''
app.Layout=html.Div([
html.Div([
html.Div([],className='col-md-12')
],className='row'),
],className='container)
'''


'''
app.Layout=html.Div([
html.Div([
html.Div([
html.Div([],className='card')
],className='col-md-12')
],className='row'),
],className='container)
'''

'''
app.Layout=html.Div([
html.Div([
html.Div([
html.Div([
html.Div([enter text here using html.H3/H4/H5...],className='card-body')
],className='card')
],className='col-md-12')
],className='row'),
],className='container)
'''

app.layout=html.Div([            ## this html is for container. 
html.H1("Corona Virus Pandemic",style={'color':'#fff','text-align':'center'}), 
html.Div([ ## this html is for row
    html.Div([ ## this html is for col-md-3
        html.Div([    ## this html is for card
            html.Div([ ## this html is for card body
                html.H3("Total cases",className='text-light'),
                html.H4(total,className='text-light') ## you can use style={color:'red hex number'} instead of className
            ],className='card-body')
        ],className='card bg-danger ') ## to change the background to red use 'card bg-danger' bg means background and danger indicates red  ## if not red then simply write 'card'
    ],className='col-md-3'),
    html.Div([        
        html.Div([    
            html.Div([ 
                html.H3("Active cases",className='text-light'),
                html.H4(active,className='text-light') 
            ],className='card-body')
        ],className='card bg-info ') 
        ],className='col-md-3'),
    html.Div([html.Div([    
            html.Div([ 
                html.H3("Recover cases",className='text-light'),
                html.H4(recovered,className='text-light') 
            ],className='card-body')
        ],className='card bg-warning ')
          ],className='col-md-3'),
    html.Div([html.Div([    
            html.Div([ 
                html.H3("Deaths",className='text-light'),
                html.H4(deaths,className='text-light') 
            ],className='card-body')
        ],className='card bg-success ')
          ],className='col-md-3')
],className='row'),
html.Div([ 
    html.Div([],className='col-md-6'), 
    html.Div([],className='col-md-6')
],className='row'),
html.Div([
        html.Div([
            html.Div([
                html.Div([ ## in this div we need to add two things 1st is Dropdown (choose one option from list of options) and second is Bargraph
                    dcc.Dropdown(id='picker',options=options,value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
],className='row')
],className='container')



@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):
    if type=='All':
        pbar=patients['detected_state'].value_counts().reset_index()
    
    else:
        npat=patients[patients['current_status']==type]
        pbar=npat['detected_state'].value_counts().reset_index()
    
    return {'data':[go.Bar(x=pbar['detected_state'],y=pbar['count'])],
               'layout':go.Layout(title='State Total Count')}

if __name__ == "__main__":
    app.run(debug=True, port=8050)

## it is very hard to use css so therefore we use bootstrap instead of css
## to add graphs we use dcc
## to add para or heading we use html 

