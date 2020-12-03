from app import db, MaternityLeave
from maternity_leave import mat_leave


mat_url = "https://worldpopulationreview.com/country-rankings/maternity-leave-by-country"
# set up your scraping below

mat_table = mat_leave(mat_url)

# rows = { 
#     "row1": "row1_val",
#     "row2": "row2_val",
# } 

# this `main` function should run your scraping when 
# this script is ran.
def main():
    db.drop_all()
    db.create_all()
    for country in mat_table:
        new_row = MaternityLeave(country=country[0], weeks_paid=country[1], payment_rate=country[2], population_2020=country[3])
        print(new_row)
        db.session.add(new_row)
        db.session.commit()

if __name__ == '__main__':
    main()