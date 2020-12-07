from app import db, MaternityLeave #importing class from app.py
from maternity_leave import mat_leave #import scraping script from the maternity_leave.py file


mat_url = "https://worldpopulationreview.com/country-rankings/maternity-leave-by-country"
#passing the url link to the scraping script --> to be saved in a table
mat_table = mat_leave(mat_url)

# rows = { 
#     "row1": "row1_val",
#     "row2": "row2_val",
# } 

# this `main` function should run your scraping when 
# this script is ran.
def main():
    db.drop_all()  #makes sure there are no tables and the database is empty
    db.create_all() #creates the columns defined inside the Class
    for i in mat_table:  #loops through the scraping results
        new_row = MaternityLeave(country=i[0], weeks_paid=i[1], payment_rate=i[2], population_2020=i[3]) #defining each column using undexing from the list results
        print(new_row)
        db.session.add(new_row)  #adds each row to the database
        db.session.commit()

if __name__ == '__main__':
    main()