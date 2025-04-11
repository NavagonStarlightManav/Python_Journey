import pandas as pd

dataset = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_set=dataset[dataset['Primary Fur Color']=='Gray']
red_set=dataset[dataset['Primary Fur Color']=='Red']
black_set=dataset[dataset['Primary Fur Color']=='Black']

grey=len(grey_set)
red=len(red_set)
black=len(black_set)



color_set = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey, red, black]
}

color_set=pd.DataFrame(color_set)
color_set.to_csv('color_set.csv')