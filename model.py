import web

render = web.template.render('templates/')

class Increment:

    def __init__(self):
        self.file_increment = './counter.txt'

    def count_users(self):
        f = open(self.file_increment, 'r')
        users = f.read()
        f.close()
        if users == "":
            users = 0
        return int(users)

    def increment_users(self):
        try:
            users = self.count_users()
        except IOError:
            open(self.file_increment, 'w').close() # touch
            users = self.count_users()

        users += 1
        susers = str(users)

        try:
            f = open(self.file_increment, 'w')
        except IOError as (errno, strerror):
            print "I/O error({0}): {1}".format(errno, strerror)
            return False
        f.write(susers)
        f.close()
        return users

