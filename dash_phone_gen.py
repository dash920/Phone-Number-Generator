import sys
import random
import os
import time
us_states_area_codes = {
    "Alabama": ['205', '251', '256', '334', '938'],
    "Alaska": ['907'],
    "Arizona": ['480', '520', '602', '623', '928'],
    "Arkansas": ['479', '501', '870'],
    "California": ['209', '213', '310', '415', '510', '818', '925', '619', '323', '714', '805', '831', '949', '562', '408', '916', '747', '669', '628', '442', '760'],
    "Colorado": ['303', '719', '720', '970'],
    "Connecticut": ['203', '475', '860', '959'],
    "Delaware": ['302'],
    "Florida": ['239', '305', '321', '352', '386', '407', '561', '727', '754', '772', '786', '813', '850', '863', '904', '941', '954'],
    "Georgia": ['229', '404', '470', '478', '678', '706', '762', '770', '912'],
    "Hawaii": ['808'],
    "Idaho": ['208', '986'],
    "Illinois": ['217', '224', '309', '312', '331', '618', '630', '708', '773', '779', '815', '847', '872'],
    "Indiana": ['219', '260', '317', '463', '574', '765', '812', '930'],
    "Iowa": ['319', '515', '563', '641', '712'],
    "Kansas": ['316', '620', '785', '913'],
    "Kentucky": ['270', '364', '502', '606', '859'],
    "Louisiana": ['225', '318', '337', '504', '985'],
    "Maine": ['207'],
    "Maryland": ['240', '301', '410', '443', '667'],
    "Massachusetts": ['339', '351', '413', '508', '617', '774', '781', '857', '978'],
    "Michigan": ['231', '248', '269', '313', '517', '586', '616', '734', '810', '906', '947', '989'],
    "Minnesota": ['218', '320', '507', '612', '651', '763', '952'],
    "Mississippi": ['228', '601', '662', '769'],
    "Missouri": ['314', '417', '573', '636', '660', '816'],
    "Montana": ['406'],
    "Nebraska": ['308', '402', '531'],
    "Nevada": ['702', '725', '775'],
    "New Hampshire": ['603'],
    "New Jersey": ['201', '551', '609', '732', '848', '856', '862', '908', '973'],
    "New Mexico": ['505', '575'],
    "New York": ['212', '315', '332', '347', '516', '518', '585', '607', '631', '646', '716', '718', '845', '914', '917', '929', '934'],
    "North Carolina": ['252', '336', '704', '743', '828', '910', '980', '984'],
    "North Dakota": ['701'],
    "Ohio": ['216', '220', '234', '330', '419', '440', '513', '567', '614', '740', '937'],
    "Oklahoma": ['405', '539', '580', '918'],
    "Oregon": ['458', '503', '541', '971'],
    "Pennsylvania": ['215', '267', '272', '412', '484', '570', '610', '717', '724', '814', '878'],
    "Rhode Island": ['401'],
    "South Carolina": ['803', '843', '854', '864'],
    "South Dakota": ['605'],
    "Tennessee": ['423', '615', '629', '731', '865', '901', '931'],
    "Texas": ['210', '214', '254', '281', '325', '346', '409', '430', '432', '469', '512', '682', '713', '737', '806', '817', '830', '832', '903', '915', '936', '940', '956', '972', '979'],
    "Utah": ['385', '435', '801'],
    "Vermont": ['802'],
    "Virginia": ['276', '434', '540', '571', '703', '757', '804'],
    "Washington": ['206', '253', '360', '425', '509', '564'],
    "West Virginia": ['304', '681'],
    "Wisconsin": ['262', '414', '534', '608', '715', '920'],
    "Wyoming": ['307']
}
canada_provinces_area_codes = {
    "Alberta": ['403', '587', '780', '825', '368'],
    "British Columbia": ['236', '250', '604', '672', '778'],
    "Manitoba": ['204', '431', '584'],
    "New Brunswick": ['506'],
    "Newfoundland and Labrador": ['709'],
    "Nova Scotia and PEI": ['902', '782'],
    "Ontario": ['226', '249', '289', '343', '365', '416', '437', '519', '548', '613', '647', '705', '807', '905'],
    "Quebec": ['367', '418', '438', '450', '514', '579', '581', '819', '873'],
    "Saskatchewan": ['306', '639', '474'],
    "Northwest Territories, Yukon, Nunavut": ['867']
}
def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
def generate_aus_numbers(num_count):
    """Generate Australian phone numbers."""
    country_code = '+61'
    with open('AUSphone.txt', 'a') as file:
        for _ in range(num_count):
            while True: 
                number = country_code + '4' + ''.join(random.choice('0123456789') for _ in range(8))
                file.write(number + '\n')
                print(f"Generated Australian phone number: {number}")
                break
def generate_usa_numbers(states, num_count):
    """Generate USA phone numbers for selected states."""
    country_code = '+1'
    selected_area_codes = [code for state in states for code in us_states_area_codes[state]]
    
    with open('USAphone.txt', 'a') as file:
        for _ in range(num_count):
            area_code = random.choice(selected_area_codes)
            number = country_code + area_code + ''.join(random.choice('0123456789') for _ in range(7))
            file.write(number + '\n')
            print(f"Generated USA phone number: {number}")
def generate_canada_numbers(provinces, num_count):
    country_code = '+1'
    selected_area_codes = [code for province in provinces for code in canada_provinces_area_codes[province]]
    with open('CANADAphone.txt', 'a') as file:
        for _ in range(num_count):
            area_code = random.choice(selected_area_codes)
            number = country_code + area_code + ''.join(random.choice('0123456789') for _ in range(7))
            file.write(number + '\n')
            print(f"Generated Canadian phone number: {number}")
def display_states():
    """Display available states for selection."""
    print("Select a state by its number:")
    for i, state in enumerate(us_states_area_codes.keys(), 1):
        print(f"{i}. {state}")
def display_provinces():
    print("Select a Canadian province/territory by its number:")
    for i, province in enumerate(canada_provinces_area_codes.keys(), 1):
        print(f"{i}. {province}")

def get_selection(options_dict):
    while True:
        try:
            selection = input("Enter the numbers (comma-separated) or a single number: ")
            indices = [int(x.strip()) - 1 for x in selection.split(',')]
            options = list(options_dict.keys())
            selected = [options[i] for i in indices if 0 <= i < len(options)]
            if not selected:
                raise ValueError("Invalid selection.")
            return selected
        except ValueError:
            print("Invalid input. Please try again.")
def get_user_choice():
    while True:
        print('\nPlease Select from the list ♥:\n')
        print('1 - Phone Generator Australia')
        print('2 - Phone Generator USA')
        print('3 - Phone Generator Canada')
        print('0 - Quit the Program')
        user_choice = input('Your Choice : ')
        if user_choice in ['0', '1', '2', '3']:
            return user_choice
        else:
            print("Invalid choice, please select a valid option.")
def main():
    print('dash-phone generator')
    print('discord:dash01632')
    time.sleep(2)
    clear()

    user_choice = get_user_choice()

    if user_choice == '1':
        try:
            num_count = int(input("How many Australian phone numbers to generate? "))
            generate_aus_numbers(num_count)
        except ValueError:
            print("Please enter a valid number.")
    elif user_choice == '2':
        display_states()
        selected_states = get_selection(us_states_area_codes)
        try:
            num_count = int(input("How many USA phone numbers to generate? "))
            generate_usa_numbers(selected_states, num_count)
        except ValueError:
            print("Please enter a valid number.")
    elif user_choice == '3':
        display_provinces()
        selected_provinces = get_selection(canada_provinces_area_codes)
        try:
            num_count = int(input("How many Canadian phone numbers to generate? "))
            generate_canada_numbers(selected_provinces, num_count)
        except ValueError:
            print("Please enter a valid number.")
    elif user_choice == '0':
        print('CLOSING BYEEEEEEEEEEEEE')
        quit()
if __name__ == "__main__":
    main()
