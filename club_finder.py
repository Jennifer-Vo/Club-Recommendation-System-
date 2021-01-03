""" CSC108 Assignment 3: Club Recommendations - Main Program code """
from typing import Dict, List
from club_functions import load_profiles, recommend_clubs


def print_recommendations(recommended_clubs: List[str], person: str) -> None:
    """Print the recommendations in recommended_clubs or a message
    indicating that there are no recommendations.

    """

    if recommended_clubs == None:
        print('\nrecommend_clubs returned None. Implement recommend_clubs before using the recommendation system')

    elif recommended_clubs != []:
        print('\nRecommendations for {}:'.format(person))
        for name in recommended_clubs:
            print(name)
    else:
        print('\nThere are no recommendations for {}.'.format(person))


def interactive_session(person_to_friends: Dict[str, List[str]],
                        person_to_clubs: Dict[str, List[str]],
                        people: List[str]) -> None:
    """Continuously prompt the user for a person's name and respond by
    printing club recommendations for that person.
    """
    print('List of people in network:')
    i = 0
    for p in people:
        print(i,p)
        i += 1
    person = input('Please enter a person or their # (or press return to exit): ')
    while person != '':
        if person.isdigit():
            person = int(person)
            if 0 <= person < len(people):
                person = people[person]
        potential = recommend_clubs(person_to_friends,
                                person_to_clubs, person)
        print_recommendations(potential, person)
        person = input('\nPlease enter a person or their # (or press return to exit): ')
    print('Thank you for using the recommendation system!')


if __name__ == '__main__':

    print("Welcome to the Recommendation System!\n")
    print("There are two social networks:")
    print("A  P2F and PNC from the starter code")
    print("B  data read from profiles.txt\n")
    which = input("Which social network do you want to use (A or B)? ")
    if 'a' in which.lower():
        print("Using P2F and P2C from starter code")
        from club_functions import P2F, P2C
    else:
        print("Using profiles loaded from profiles.txt")
        profiles_file = open('profiles.txt')
        P2F, P2C = load_profiles(profiles_file)
        profiles_file.close()

    people = []
    for key in P2F:
        if key not in people:
            people.append(key)
        for friend in P2F[key]:
            if friend not in people:
                people.append(friend)
    for key in P2C:
        if key not in people:
            people.append(key)
    people.sort()

    interactive_session(P2F, P2C, people)
