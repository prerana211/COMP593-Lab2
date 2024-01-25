def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {'full_name' : 'Prerana Mainali',
             'student_id' : 10314221,
             'pizza_toppings' :[
                 'CHESSE',
                 'GREEN PEPPER',
                 'MUSHROOM'
             ],
             'movies' : [
                 {'title' : 'Parasite',
                  'genre' : 'Thriller'},
                  {'title' : 'Train to Busan',
                   'genre' : 'Horror'}
             ]
             }
    
    # TODO: Step 3 - Add another movie to the data structure
    about_me['movies'].append({'title': 'Star Wars',
                               'genre': 'Sci-Fi'})
    

    
    add_pizza_toppings(about_me, toppings =("CHICKEN", "PANEER"))
    print_student_name_and_id(about_me)
    print_pizza_toppings(about_me)
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(movie_list)
    print()
    return
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    first_name = (full_name.split(' ')) [0]
    student_id = about_me['student_id']

    print(f"My name is {full_name}, but you can call me Miss {first_name}")
    print(f"My student id is {student_id}")
    print_student_name_and_id(about_me)
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].append(toppings)
    
    about_me['pizza_toppings'] = [tops.lower() for tops in about_me["pizza_toppings"]]
    about_me['pizza_toppings'].sort()
    

# TODO: Step 6 - Function that prints bullet list of pizza toppings
    def print_pizza_toppings(about_me):
        print("My favourite pizza toppings are:")
        for topp in about_me['pizza_toppings']:
            print(f"- {topp}")
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
        movie_genres = [movie['genre'] for movie in about_me['movies']]
        print("I like to watch", end=" ")
        for  genre in enumerate(movie_genres):
          print(f"and {genre}")
        print("movies.")
                   

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
         titles = [movie['title'].title() for movie in movie_list]
         print("Some of my favourite movies are")
         for title in enumerate(titles):
            print(f"{title}")
         return
    
if __name__ == '__main__':
    main()