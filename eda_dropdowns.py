df_options = [
    {'label':'transfers', 'value': "transfers"},
    {'label':'market values', 'value': "markval"}
]

numerical_options = [
    {'label':'fee','value':'fee'},
    {'label':'mv', 'value':'mv'},
    {'label':'age', 'value':'age'},
    ]

categorical_options = [
    {'label':'position','value':'main_field_position'},
    {'label':'continent', 'value':'continent'},
    {'label':'year', 'value':'year'},
    {'label':'type', 'value':'type'},
]

mv_numeric_options = [    
    {'label':'cum_mv','value':'cum_mv'},
    {'label':'mv','value':'mv'},
    {'label':'last_year_mv', 'value':'last_year_mv'},
    {'label':'age', 'value':'age'},
]

mv_categoric_options = [
    {'label':'year','value':'year'},
    {'label':'position','value':'main_field_position'},
    {'label':'continent','value':'continent'},
    {'label':'league_class','value':'league_class'}
]


transfers_hover_data = ['name','age','nationality','from','to','mv','fee']
markval_hover_data = ['name','age','nationality','club','league','cum_mv',]