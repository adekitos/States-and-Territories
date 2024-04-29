#add required assignment header comment lines here

    
#Global Constants
# Indentation constant of two spaces
indent1 = ' '*2

#1D Lists ------------------------------------------------------------------------------------------------------------------
STATE_CODES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA',
               'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
               'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

TERRITORY_CODES = ['AS', 'GU', 'MP', 'PR', 'VI']


STATE_INCOMES = [56929, 81133, 70821, 50784, 81575, 84954, 80958, 68687, 59734, 61497,
                  82199, 76918, 79253, 70190, 72429, 75979, 55629, 57206, 71139, 97332,
                  86566, 64488, 80441, 46637, 63594, 64999, 78109, 64340, 88841, 88559,
                  53463, 72920, 62891, 68882, 62689, 60096, 81855, 72627, 74982, 62542,
                  73893, 62166, 67404, 87649, 76079, 80268, 87648, 46836, 69943, 71052]
    
#2D LISTs ------------------------------------------------------------------------------------------------------------------
STATES = [  ['AL' , 'Alabama' , 'Montgomery' , 'Yellowhammer' , 'Camellia' , 22 , '12/14/1819' , 5024279],
            ['AK' , 'Alaska' , 'Juneau' , 'Willow Ptarmigan' , 'Forget-me-not' , 49 , '01/03/1959' , 733391],
            ['AZ' , 'Arizona' , 'Phoenix' , 'Cactus Wren' , 'Saguaro Cactus Blossom' , 48 , '02/14/1912' , 7151502],
            ['AR' , 'Arkansas' , 'Little Rock' , 'Mockingbird' , 'Apple Blossom' , 25 , '06/15/1836' , 3011524],
            ['CA' , 'California' , 'Sacramento' , 'California Valley Quail' , 'Golden Poppy' , 31 , '09/09/1850' , 39538223],
            ['CO' , 'Colorado' , 'Denver' , 'Lark Bunting' , 'Columbine' , 38 , '08/01/1876' , 5773714],
            ['CT' , 'Connecticut' , 'Hartford' , 'American Robin' , 'Mountain Laurel' , 5 , '01/09/1788' , 3605944],
            ['DE' , 'Delaware' , 'Dover' , 'Blue Hen Chicken' , 'Peach Blossom' , 1 , '12/07/1787' , 989948],
            ['FL' , 'Florida' , 'Tallahassee' , 'Mockingbird' , 'Orange Blossom' , 27 , '03/03/1845' , 21538187],
            ['GA' , 'Georgia' , 'Atlanta' , 'Brown Thrasher' , 'Cherokee Rose' , 4 , '01/02/1788' , 10711908],
            ['HI' , 'Hawaii' , 'Honolulu' , 'Nene (Hawaiian Goose)' , 'Hibiscus' , 50 , '08/21/1959' , 1455271],
            ['ID' , 'Idaho' , 'Boise' , 'Mountain Bluebird' , 'Syringa' , 43 , '07/03/1890' , 1839106],
            ['IL' , 'Illinois' , 'Springfield' , 'Cardinal' , 'Native violet' , 21 , '12/03/1818' , 12812508],
            ['IN' , 'Indiana' , 'Indianapolis' , 'Cardinal' , 'Peony' , 19 , '12/11/1816' , 6785528],
            ['IA' , 'Iowa' , 'Des Moines' , 'Eastern Goldfinch' , 'Wild Rose' , 29 , '12/28/1846' , 3190369],
            ['KS' , 'Kansas' , 'Topeka' , 'Western Meadowlark' , 'Native Sunflower' , 34 , '01/29/1861' , 2937880],
            ['KY' , 'Kentucky' , 'Frankfort' , 'Kentucky Cardinal' , 'Goldenrod' , 15 , '06/01/1792' , 4505836],
            ['LA' , 'Louisiana' , 'Baton Rouge' , 'Pelican' , 'Magnolia' , 18 , '04/30/1812' , 4657757],
            ['ME' , 'Maine' , 'Augusta' , 'Chickadee' , 'White Pine Cone and Tassel' , 23 , '03/15/1820' , 1362359],
            ['MD' , 'Maryland' , 'Annapolis' , 'Baltimore Oriole' , 'Black-Eyed Susan' , 7 , '04/28/1788' , 6177224],
            ['MA' , 'Massachusetts' , 'Boston' , 'Chickadee' , 'Mayflower' , 6 , '02/06/1788' , 7029917],
            ['MI' , 'Michigan' , 'Lansing' , 'Robin' , 'Apple Blossom' , 26 , '01/26/1837' , 10077331],
            ['MN' , 'Minnesota' , 'St. Paul' , 'Common Loon' , 'Pink and White Ladys Slipper' , 32 , '05/11/1858' , 5706494],
            ['MS' , 'Mississippi' , 'Jackson' , 'Mockingbird' , 'Magnolia' , 20 , '12/10/1817' , 2961279],
            ['MO' , 'Missouri' , 'Jefferson City' , 'Bluebird' , 'Hawthorn' , 24 , '08/10/1821' , 6154913],
            ['MT' , 'Montana' , 'Helena' , 'Western Meadowlark' , 'Bitterroot' , 41 , '11/08/1889' , 1084225],
            ['NE' , 'Nebraska' , 'Lincoln' , 'Western Meadowlark' , 'Goldenrod' , 37 , '03/01/1867' , 1961504],
            ['NV' , 'Nevada' , 'Carson City' , 'Mountain Bluebird' , 'Sagebrush' , 36 , '10/31/1864' , 3104614],
            ['NH' , 'New Hampshire' , 'Concord' , 'Purple Finch' , 'Purple Lilac' , 9 , '06/21/1788' , 1377529],
            ['NJ' , 'New Jersey' , 'Trenton' , 'Eastern Goldfinch' , 'Purple Violet' , 3 , '12/18/1787' , 9288994],
            ['NM' , 'New Mexico' , 'Santa Fe' , 'Roadrunner' , 'Yucca Flower' , 47 , '01/06/1912' , 2117522],
            ['NY' , 'New York' , 'Albany' , 'Bluebird' , 'Rose' , 11 , '07/26/1788' , 20201249],
            ['NC' , 'North Carolina' , 'Raleigh' , 'Cardinal' , 'Dogwood' , 12 , '11/21/1789' , 10439388],
            ['ND' , 'North Dakota' , 'Bismarck' , 'Western Meadowlark' , 'Wild Prairie Rose' , 39 , '11/02/1889' , 779094],
            ['OH' , 'Ohio' , 'Columbus' , 'Cardinal' , 'Scarlet Carnation' , 17 , '03/01/1803' , 11799448],
            ['OK' , 'Oklahoma' , 'Oklahoma City' , 'Scissor-Tailed Flycatcher' , 'Mistletoe' , 46 , '11/16/1907' , 3959353],
            ['OR' , 'Oregon' , 'Salem' , 'Western Meadowlark' , 'Oregon Grape' , 33 , '02/14/1859' , 4237256],
            ['PA' , 'Pennsylvania' , 'Harrisburg' , 'Ruffed Grouse' , 'Mountain Laurel' , 2 , '12/12/1787' , 13002700],
            ['RI' , 'Rhode Island' , 'Providence' , 'Rhode Island Red' , 'Violet' , 13 , '05/29/1790' , 1097379],
            ['SC' , 'South Carolina' , 'Columbia' , 'Carolina Wren' , 'Yellow Jessamine' , 8 , '05/23/1788' , 5118425],
            ['SD' , 'South Dakota' , 'Pierre' , 'Ring-Necked Pheasant' , 'American Pasqueflower' , 40 , '11/02/1889' , 886667],
            ['TN' , 'Tennessee' , 'Nashville' , 'Mockingbird' , 'Iris' , 16 , '06/01/1796' , 6910840],
            ['TX' , 'Texas' , 'Austin' , 'Mockingbird' , 'Bluebonnet' , 28 , '12/29/1845' , 29145505],
            ['UT' , 'Utah' , 'Salt Lake City' , 'California Gull' , 'Sego Lily' , 45 , '01/04/1896' , 3271616],
            ['VT' , 'Vermont' , 'Montpelier' , 'Hermit Thrush' , 'Red Clover' , 14 , '03/04/1791' , 643077],
            ['VA' , 'Virginia' , 'Richmond' , 'Cardinal' , 'Dogwood' , 10 , '06/25/1788' , 8631393],
            ['WA' , 'Washington' , 'Olympia' , 'Willow Goldfinch' , 'Western Rhododendron' , 42 , '11/11/1889' , 7705281],
            ['WV' , 'West Virginia' , 'Charleston' , 'Cardinal' , 'Big Rhododendron' , 35 , '06/20/1863' , 1793716],
            ['WI' , 'Wisconsin' , 'Madison' , 'Robin' , 'Wood Violet' , 30 , '05/29/1848' , 5893718],
            ['WY' , 'Wyoming' , 'Cheyenne' , 'Meadowlark' , 'Indian Paintbrush' , 44 , '07/10/1890' , 576851]]


TERRITORIES = [ ['AS' , 'American Samoa' , 'Pago Pago' , '1900' , 49710],
                ['GU' , 'Guam' , 'Hagåtña' , '1899' , 153836],
                ['MP' , 'Northern Mariana Islands' , 'Saipan' , '1986' , 47329],
                ['PR' , 'Puerto Rico' , 'San Juan' , '1899' , 3285874],
                ['VI' , 'U.S. Virgin Islands' , 'Charlotte Amalie' , '1917' , 87146]]


#MAIN ------------------------------------------------------------------------------------------------------------------
def main():
    header()

# validating inputs
    y = 'false'
    while y == 'false':
        menu_option = input('  Enter a selection: ')
        if menu_option == '1':
            #menu_option = int(menu_option)
            view_all_states(STATES)
            #y = 'true'
        elif menu_option == '2':
            #menu_option = int(menu_option)
            view_all_territories(TERRITORIES)
            #y = 'true'
        elif menu_option == '3':
            #menu_option = int(menu_option)
            view_one_state(STATE_INCOMES, STATES)
            #y = 'true'
        elif menu_option == '4':
            #menu_option = int(menu_option)
            view_state_stats_facts(STATES)
            #y = 'true' 
        elif menu_option.upper() == 'X':
            exit() 
            y = 'true'
        else:
            print(indent1,'invalid input, Please try again')
        
   



#FUNCTIONS -------------------------------------------------------------------------------------------------------------
# Function that prints the header
def header():
    print('*'*70)
    print(f'{"U.S. States & Territories":^70}')
    print('*'*70)
    
    print()
    print(indent1,'Menu Options')
    print('-'*25)
    print(indent1,'1: View all states')
    print(indent1,'2: View all territories')
    print(indent1,'3: View one state')
    print(indent1,'4: View state stats & facts')
    print(indent1,'5: Press to exit', '\n')
    

# Function to view all states     
def view_all_states(STATES):
    print('='*27)
    print(' List of States')
    print('='*27)
    
    print(f'{"St Code":7s} {"State Name":^19s} {"Capital":^25s} {"Bird":^25s} {"Flower":^35s} {"Join Order":^10s} {"Join Date":^10s} {"Population":>10s}')
    print(f'{"-"*7} {"-"*19} {"-"*25} {"-"*25} {"-"*35} {"-"*10} {"-"*10} {"-"*10}')
    for row in range(len(STATES)):
        state_code = STATES[row][0]
        state_name = STATES[row][1]
        capital = STATES[row][2]
        bird = STATES[row][3]
        flower = STATES[row][4]
        join_order = STATES[row][5]
        join_date = STATES[row][6]
        population = STATES[row][7]
        
        print(f'{state_code:7s} {state_name:19s} {capital:25s} {bird:25s} {flower:35s} {join_order:^10} {join_date:10s} {population:10,}')
    
    print()
    input('Press enter to continue...')

# Function to view the territories
def view_all_territories(TERRITORIES):
    print('='*27)
    print(' List of Territories')
    print('='*27)
    
    print(f'{"Code":4s} {"Territory Name":25s} {"Capital":16s} {"Year":4s} {"Population":9s}')
    print(f'{"-"*4} {"-"*25} {"-"*16} {"-"*4} {"-"*9}')
    for row in range(len(TERRITORIES)):
        terr_code = TERRITORIES[row][0]
        territory_name = TERRITORIES[row][1]
        capital = TERRITORIES[row][2]
        year_acquired = TERRITORIES[row][3]
        population = TERRITORIES[row][4]
        print(f'{terr_code:^4s} {territory_name:25s} {capital:16s} {year_acquired:^4} {population:9,}')
    
    print()
    input('Press enter to continue...')

# Function to view a state
def view_one_state(STATE_INCOMES, STATES):
    search_value = input('  Enter State Code:      ')
    print()
    print('='*25)
    print(' State Details')
    print('='*25,'\n')
    
    print(' ','-'*32)
    #search_value = input('  State:      ')
    for i in range(0, len(STATES)):
        if STATES[i][0] == search_value:
            state_code = STATES[i][0]
            state_name = STATES[i][1]
            capital = STATES[i][2]
            bird = STATES[i][3]
            flower = STATES[i][4]
            join_order = STATES[i][5]
            join_date = STATES[i][6]
            population = STATES[i][7]
            avg_income = STATE_INCOMES[i]
            
            print(f' {" State:":13}    {state_code} - {state_name}')
            print(f' {" Capital:":13}    {capital}')
            print(f' {" Bird:":13}    {bird}')
            print(f' {" Flower:":13}    {flower}')
            print(f' {" Join Order:":13}    {join_order}')
            print(f' {" Join Date:":13}    {join_date}')
            print(f' {" Population:":13}    {population:,}')
            print(f' {" Avg Income:":13}    ${avg_income:,}')
        
    print(' ','-'*32,'\n')
    
    input('Press enter to continue...')

# Function to view state stats & facts
def view_state_stats_facts(STATES):
    print('='*27)
    print(' All States - Stats & Facts')
    print('='*27)
    
    print(' ','-'*32)
    total = 0
    min = 10**1000
    max = 0
    count = 0
    join_order_lowest = STATES[0][5]
    join_order_highest = 0
    for i in range(len(STATES)):
        total += STATES[i][7]
        if STATES[i][7] < min:
            min = STATES[i][7]
            
            
        if STATES[i][7] > max:
            max = STATES[i][7]
            
            
        if STATES[i][3] == 'Mockingbird':
            count +=1
            
        if STATES[i][5] < join_order_lowest:
            join_order_lowest = STATES[i][5]
            index1 = i
            
        if STATES[i][5] > join_order_highest:
            join_order_highest = STATES[i][5]
            index2 = i
    average = total//len(STATES)    
    print('  Population Stats:')
    print(f'{"     Total:":16s}       {total:,}')
    print(f'{"     Avg/State:":16s}       {average:,}')
    print(f'{"     Min:":16s}       {min:,}')
    print(f'{"     Max:":16s}       {max:,}')
    
    print(' ','-'*32)
    print('  Mockingbird States: ', count)
    print(' ','-'*32)
    
    print('  Join Order: ')
    print(f'{"     First:"}            {STATES[index1][1]}-{STATES[index1][6]}')
    print(f'{"     Last:"}             {STATES[index2][1]}-{STATES[index2][6]}')
    
    print()
    input('Press enter to continue...')
    

def exit():
    print(indent1,">> Exiting...")
    SystemExit


main()