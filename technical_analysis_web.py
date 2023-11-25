from ctypes.wintypes import SIZE
import streamlit as stl
import technical_analysis_library as tal

start_date, end_date = None, None 
symbols = []
# session_state: dictionary object stores key-value pair  
chart_data = None 
def get_start_date() -> str: 
    start_date = stl.session_state['start_date']
    return start_date
    
def get_end_date() -> str : 
    end_date = stl.session_state['end_date']
    return end_date
    
def get_symbols() -> list: 
    symbols = stl.session_state['symbols'].split(" ")
    return symbols

def generate_static_linear_chart() :
    state_date = get_start_date()
    end_date = get_end_date() 
    symbols = get_symbols() 
    print(f"{start_date} {end_date} {symbols}")
    figure = tal.generate_simple_linear_chart(start_date,end_date,symbols)
    stl.pyplot(figure)

def generate_interactive_linear_chart() : 
    pass

stl.title("Technical Analysis")
stl.subheader("The web application is a prototype of Algorithm Trading WS")
stl.write("Created by Benjamin Chang")

stl.checkbox("Are you eligible for using this app? ")
stl.checkbox("Are you living in North America? ")

row_input1 = stl.columns((1))
with row_input1[0] : 
    stl.text_input(placeholder="Enter a list of tickers...", 
               label="Enter Tickers/Symbols",
               on_change=get_symbols,
               key='symbols')

row_input2 = stl.columns((2,1,2,1))
with row_input2[0] : 
    stl.text_input(placeholder="Enter start date...",
                   label="Start Date",
                   on_change=get_start_date, 
                   key='start_date')
    
    with row_input2[2]:
        stl.text_input(placeholder="Enter end date...", 
                       label="End Date",
                       on_change=get_end_date,
                       key='end_date')

row_input3 = stl.columns((1,1))
with row_input3[0] :
    stl.write("<b>Applicable Technical Analysis</b>")

row_input4 = stl.columns((1,1,1,1))
with row_input4[0] : 
    stl.button("Simple Linear",
               on_click=generate_static_linear_chart,
               key="simple_linear")

    with row_input4[1] : 
        stl.button("Interactive Linear",
                    on_click=generate_interactive_linear_chart,
                    key="interactive_linear")

row_input5 = stl.columns((1))
with row_input4[0] : 
    stl.area_chart()


        