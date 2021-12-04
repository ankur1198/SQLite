import sqlite3

# Connect to database
conn= sqlite3.connect(':memory:')
conn= sqlite3.connect('C:/sqlite/db/movies.db')

# Create a cursor
c = conn.cursor()

# Create a table
 c.execute("""CREATE TABLE  Movies (
         movie_name TEXT,
         actor_full_name TEXT,
         actress_full_name TEXT,
         director_full_name TEXT,
         year_of_release INTEGER
)""")
  
many_movies= [('The Conjuring: The Devil Made Me Do It','Patrick Wilson','Vera Farmiga','Michael Chaves', '2021'),
              ('Tanhaji','Ajay DEvgan','Kajol','Om Raut','2020'),
              ('Sholay','Amjad Khan','Hema Malini','Ramesh Sippy','1975'),
              ('Interstellar ','Matthew McConaughey','Jessica Chastain','Christopher Nolan','2014'),
              ('Inception','Leonardo DiCaprio','Marion Cotillard','Christopher Nolan','2010'),
              ('Joker','Joaquin Phoenix','Zazie Beetz','Todd Phillips','2019'),
              ('Jai Bhim','Suriya','Lijo Mol Jose','T.J. Gnanavel','2021'),
]

# Insert Data into Movies Table
c.executemany("INSERT INTO Movies VALUES (?,?,?,?,?)", many_movies)

# Quering all values from table Movies
c.execute("SELECT * FROM Movies")
print(c.fetchall())
print('-------------------------------------------------------------------------------------------------------------')

# Quering Actor name to getting movie name
c.execute("SELECT actor_full_name,movie_name FROM Movies WHERE actor_full_name= 'Leonardo DiCaprio'")
print(c.fetchall())

print('Program executed successfully...........')



conn.commit()
conn.close()
