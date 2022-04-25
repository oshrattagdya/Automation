from DataBase import DB


class Update(DB):
    x = DB().connect(" update actor set first_name = 'avi' where last_name =")

