""" CSC108 Assignment 3: Club Recommendations - Starter code."""
from typing import List, Tuple, Dict, TextIO


# Sample Data (Used by Doctring examples)

P2F = {'Jesse Katsopolis': ['Danny R Tanner', 'Joey Gladstone',
                            'Rebecca Donaldson-Katsopolis'],
       'Rebecca Donaldson-Katsopolis': ['Kimmy Gibbler'],
       'Stephanie J Tanner': ['Michelle Tanner', 'Kimmy Gibbler'],
       'Danny R Tanner': ['Jesse Katsopolis', 'DJ Tanner-Fuller',
                          'Joey Gladstone']}

P2F2 = {'Jennifer Vo': ['Danny R Vo', 'Joey Yorkdale',
                        'Sophia Huang'],
        'Sophia Huang': ['Kimmy Possible']}

P2C = {'Michelle Tanner': ['Comet Club'],
       'Danny R Tanner': ['Parent Council'],
       'Kimmy Gibbler': ['Rock N Rollers', 'Smash Club'],
       'Jesse Katsopolis': ['Parent Council', 'Rock N Rollers'],
       'Joey Gladstone': ['Comics R Us', 'Parent Council']}

P2C2 = {'Jennifer Vo': ['Comet Club', 'BJJ'],
        'Sophia Huang': ['Parent Council', 'BJJ'],
        'Merve Younessi': ['Rock N Rollers', 'BJJ', 'Parent Council']}

# Helper functions 

def update_dict(key: str, value: str,
                key_to_values: Dict[str, List[str]]) -> None:
    """Update key_to_values with key/value. If key is in key_to_values,
    and value is not already in the list associated with key,
    append value to the list. Otherwise, add the pair key/[value] to
    key_to_values.

    >>> d = {'1': ['a', 'b']}
    >>> update_dict('2', 'c', d)
    >>> d == {'1': ['a', 'b'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    >>> update_dict('1', 'c', d)
    >>> d == {'1': ['a', 'b', 'c'], '2': ['c']}
    True
    """

    if key not in key_to_values:
        key_to_values[key] = []
        
    if value not in key_to_values[key]:
        key_to_values[key].append(value)
        
def track_mutual_clubs(person_to_clubs: Dict[str, List[str]], 
                       person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that in which members have mutual clubs with person,
    excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> track_mutual_clubs(P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    >>> track_mutual_clubs(P2C, 'Michelle Tanner')
    []
    """    
    clubs_to_person = invert_and_sort(person_to_clubs)
    people_list = []
    club_list = []
    unique_list = []
    
    if person not in person_to_clubs:
        return []
    for club in person_to_clubs[person]:
        if club in clubs_to_person:
            people_list.extend(clubs_to_person[club])
    for member in people_list:
        if member not in unique_list:
            unique_list.append(member)
    for member in unique_list:
        for club in person_to_clubs[member]:
            if club not in person_to_clubs[person]: 
                club_list.append(club)
                club_list.sort()
    return club_list      

def sort_tuples(list: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """Return a list in which clubs are ordered by highest to lowest score from 
    an original list of clubs and corresponding scores. Clubs with the same 
    score are ordered alphabetically. 
    
    >>> sort_tuples([('a', 1),('b', 4), ('c',1)])
    [('b', 4), ('a', 1), ('c', 1)]
    >>> sort_tuples([('d', 10), ('a', 1), ('f', 12)])
    [('f', 12), ('d', 10), ('a', 1)]
    """
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    
    for i in list:
        list_1.append(i[0])
        list_1.sort()       
    for i in list_1:
        for j in list:
            if j[0] == i:
                list_2.append(j)   
    for i in list:
        list_3.append(i[1])
        list_3.sort(reverse=True)
    for i in list_3:
        for j in list_2:
            if j[1] == i:
                if j not in list_4:
                    list_4.append(j)
    return list_4 

# Required functions

def load_profiles(profiles_file: TextIO) -> Tuple[Dict[str, List[str]],
                                                  Dict[str, List[str]]]:
    """Return a two-item tuple containing a "person to friends" dictionary
    and a "person_to_clubs" dictionary with the data from profiles_file.

    NOTE: Functions (including helper functions) that have a parameter of type
          TextIO do not need docstring examples.
    """

    line = profiles_file.readline()
    person_to_friends = {}
    person_to_clubs = {}

    while line != '':
        list_of_friends = []
        list_of_clubs = []        
        person_name = line.strip()
        while line != '\n' and line != '':
            if line.strip() != person_name:
                if ',' in line:
                    list_of_friends.append(' '.join((line.strip()).split(', ')\
                    [::-1])) 
                else:
                    list_of_clubs.append(str(line.strip()))
            line = profiles_file.readline()
        line = profiles_file.readline()
        if len(list_of_friends) != 0:
            person_to_friends[' '.join(person_name.split(', ')[::-1])] =\
            list_of_friends            
            list_of_friends.sort()
        if len(list_of_clubs) != 0:
            person_to_clubs[' '.join(person_name.split(', ')[::-1])] = \
            list_of_clubs 
            list_of_clubs.sort()
    line = profiles_file.readline()
    return person_to_friends, person_to_clubs  

def get_average_club_count(person_to_clubs: Dict[str, List[str]]) -> float:
    """Return the average number of clubs that a person in person_to_clubs
    belongs to.

    >>> get_average_club_count(P2C)
    1.6
    >>> get_average_club_count(P2C2)
    2.3333333333333335
    """
    sum_clubs = 0
    for person in person_to_clubs:
        sum_clubs = sum_clubs + len(person_to_clubs[person])
        average_clubs = sum_clubs / len(person_to_clubs)
    if person_to_clubs == {}:
        average_clubs = float(0) 
    return average_clubs
     
def get_last_to_first(
        person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first name(s)" dictionary with the people from the
    "person to friends" dictionary person_to_friends.

    >>> get_last_to_first(P2F) == {
    ...    'Katsopolis': ['Jesse'],
    ...    'Tanner': ['Danny R', 'Michelle', 'Stephanie J'],
    ...    'Gladstone': ['Joey'],
    ...    'Donaldson-Katsopolis': ['Rebecca'],
    ...    'Gibbler': ['Kimmy'],
    ...    'Tanner-Fuller': ['DJ']}
    True
    >>> get_last_to_first(P2F2) == {
    ...    'Vo': ['Danny R', 'Jennifer'],
    ...    'Yorkdale': ['Joey'],
    ...    'Huang': ['Sophia'],
    ...    'Possible': ['Kimmy']}
    True
    """
    dict_lastname = {}
    list_friends = []
    for key in person_to_friends:
        for value in person_to_friends[key]:
            list_friends.append(value)
            list_friends.append(str(key))
    for name in list_friends:
        first_name = name.rsplit(' ', 1)[0]
        last_name = name.rsplit(' ')[-1]
        update_dict(last_name, first_name, dict_lastname)
        dict_lastname[last_name].sort()
    return dict_lastname

def invert_and_sort(key_to_value: Dict[object, object]) -> Dict[object, list]:
    """Return key_to_value inverted so that each key is a value (for
    non-list values) or an item from an iterable value, and each value
    is a list of the corresponding keys from key_to_value.  The value
    lists in the returned dict are sorted.

    >>> invert_and_sort(P2C) == {
    ...  'Comet Club': ['Michelle Tanner'],
    ...  'Parent Council': ['Danny R Tanner', 'Jesse Katsopolis',
    ...                     'Joey Gladstone'],
    ...  'Rock N Rollers': ['Jesse Katsopolis', 'Kimmy Gibbler'],
    ...  'Comics R Us': ['Joey Gladstone'],
    ...  'Smash Club': ['Kimmy Gibbler']}
    True
    >>> invert_and_sort(P2F) == {
    ...  'Danny R Tanner': ['Jesse Katsopolis'],
    ...  'Joey Gladstone': ['Danny R Tanner', 'Jesse Katsopolis'],
    ...  'Rebecca Donaldson-Katsopolis': ['Jesse Katsopolis'],
    ...  'Kimmy Gibbler': ['Rebecca Donaldson-Katsopolis', 'Stephanie J Tanner'\
    ],
    ...  'Michelle Tanner': ['Stephanie J Tanner'],
    ...  'Jesse Katsopolis': ['Danny R Tanner'],
    ...  'DJ Tanner-Fuller': ['Danny R Tanner']}
    True
    """
    inverted_dict = {}
    for key in key_to_value: 
        for value in key_to_value[key]:
            update_dict(value, key, inverted_dict)
            inverted_dict[value].sort()
    return inverted_dict
    
def get_clubs_of_friends(person_to_friends: Dict[str, List[str]],
                         person_to_clubs: Dict[str, List[str]],
                         person: str) -> List[str]:
    """Return a list, sorted in alphabetical order, of the clubs in
    person_to_clubs that person's friends from person_to_friends
    belong to, excluding the clubs that person belongs to.  Each club
    appears in the returned list once per each of the person's friends
    who belong to it.

    >>> get_clubs_of_friends(P2F, P2C, 'Danny R Tanner')
    ['Comics R Us', 'Rock N Rollers']
    >>> get_clubs_of_friends(P2F, P2C, 'Michelle Tanner')
    []
    """
    list_clubs = []
    if person not in person_to_friends:
        return []
    for key in person_to_clubs:
        if key in person_to_friends[person]:
            for club in person_to_clubs[key]:
                if person not in person_to_clubs:
                    list_clubs.append(club)
                    list_clubs.sort()
                if person in person_to_clubs and club not in person_to_clubs\
                [person]:
                    list_clubs.append(club)
                    list_clubs.sort()                    
    return list_clubs
        
def recommend_clubs(
        person_to_friends: Dict[str, List[str]],
        person_to_clubs: Dict[str, List[str]],
        person: str,) -> List[Tuple[str, int]]:
    """Return a list of club recommendations for person based on the
    "person to friends" dictionary person_to_friends and the "person
    to clubs" dictionary person_to_clubs using the specified
    recommendation system.

    >>> recommend_clubs(P2F, P2C, 'Stephanie J Tanner')
    [('Comet Club', 1), ('Rock N Rollers', 1), ('Smash Club', 1)]
    >>> recommend_clubs(P2F, P2C, 'Kimmy Gibbler')
    [('Parent Council', 1)]
    """
    list_mutual_friends = get_clubs_of_friends(person_to_friends, \
    person_to_clubs, person)
    list_mutual_clubs = track_mutual_clubs(person_to_clubs, person)
    list_recommended = []
    list_recommended_scores = []
    
    list_recommended.extend(list_mutual_friends)
    list_recommended.extend(list_mutual_clubs)
    for club in list_recommended:
        list_recommended_scores.append(list_recommended.count(club))
    zipped = zip(list_recommended, list_recommended_scores)
    set_zipped = list(set(list(zipped)))
    order_set_zipped = sort_tuples(set_zipped)
    return order_set_zipped    


if __name__ == '__main__':   
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.
    
    #import doctest
    #doctest.testmod()     