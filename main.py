#! usr/bin/env python3

try:
    import pyfiglet
    import urllib.request
    #from tabulate import tabulate
    from modules.user_loc import *
    from modules.color_codes import *
except Exception as error:
    #print(error.__class__.__name__+":"+error.message)
    print(error)

class Main:
    global cmd
    global main_banner
    global map_func
    global user_data
    global connection

    def main():
        #create a banner

        #find my details
        #print( user_data() if connection() else "no internet!" ) #simplyfy this code
        #user_data()
        #main_banner()

        user_inp = str(input("Enter your choice:-\t"))
        if user_inp != "0":
            while True:
                user_inp = str(input("Enter your choice:-\t"))
                if user_inp == "0":
                    break
        

    """def main_banner():
        ascii_banner = pyfiglet.figlet_format("IP TRACER")
        print(BRIGHT_CYAN+ascii_banner+BRIGHT_GREEN+"by Ravindu Priyankara\n"+BRIGHT_WHITE)

        table = [['Number', 'Details'], [1,"Command Line application"], [2,"Web Application"],[3,"Graphical user interface"]]
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))"""

    def user_data():
        user_detail = get_location()

        list = ["ip","city","region","postal","timezone","organization","location"]

        for x in range(len(list)):
            print(f"{BRIGHT_YELLOW} your {list[x]} is: {BRIGHT_MAGENTA}{user_detail[list[x]]}\n")

        #get a latitude and longitude

        #loc_split = user_detail["location"]
        #latitude,longitude = loc_split.split(",")

    
    def cmd():
        pass

    def connection(host='http://google.com'):
        try:
            urllib.request.urlopen(host)
            return True
        except:
            return False
    
if __name__ == '__main__':
    mainClass = Main
    mainClass.main()