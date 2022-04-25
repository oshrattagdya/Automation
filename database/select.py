from DataBase import DB

class Select(DB) :
    co = DB().connect("select * from film")
    print(co)

    co2 = DB().connect("select * from actor")
    print(co2)

    co3 = DB().connect("select count(*) from actor")
    print(co3)

    co4 = DB().connect("select count(*) from film")
    print(co4)