# Author :: Yiǧit Akoymak Date :: 19.05.2023
# Basic social media program
import time


class SocialNetworkGraph:
    def __init__(self, file_name):
        self.file_name = file_name
        self.social_NW = {}
        self.pretty_display = ""

    def load_file(self):
        """Converts the social_NW file to a dictionary where first value is the key and the rest is value"""
        with open(f'{self.file_name}', 'r') as sn_network_file:
            while line := sn_network_file.readline().rstrip():
                head, *tail = line.split()
                self.social_NW[head] = tail

    def add_user(self, nw_user):
        """Adds the user to Social_NW keys"""
        self.social_NW[nw_user] = ""

    def remove_user(self, rm_user):
        """Removes the user from social_NW keys and values"""
        del self.social_NW[rm_user]
        for usr, friends in self.social_NW.items():
            if rm_user in friends:
                self.social_NW[usr].remove(rm_user)

    def display_network(self, network) -> str:
        """A formatted string representation of the social_NW"""
        for keys, values in network.items():
            self.pretty_display += f"{keys}  --> {', '.join(values)} \n"
        return self.pretty_display

    def make_friend(self, frnd1, frnd2):
        """Make two users friends in the database if they are already in the database"""
        if (frnd2 and frnd1) in self.social_NW.keys():
            self.social_NW[frnd1] = [frnd2]
            self.social_NW[frnd2] = [frnd1]
            return f"{frnd1} and {frnd2} are now friends"
        return f"{frnd2} or/and {frnd1} are not part of the database"


class SocialNetwork(SocialNetworkGraph):
    def __init__(self, file_name):
        super().__init__(file_name)

    def total_friends(self, t_friends) -> int:
        """Returns the total amount of friends for a single user"""
        return len(self.social_NW[t_friends])

    def lonely_users(self) -> str:
        """Returns users with no friend at all"""
        lonely_list = [usr for usr in self.social_NW.keys() if len(self.social_NW[usr]) < 1]
        return f" {' '.join(lonely_list)} have/has no friend(s)"

    def less_friend(self) -> str:
        """Returns users with friends fewer friends
        stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary"""
        min_val = min(filter(lambda m_val: m_val != 0, map(len, self.social_NW.values())))
        less_f = [item for item in self.social_NW if len(self.social_NW[item]) == min_val]
        return f"{','.join(less_f)} have/has {min_val} friend(s)"

    def show_relations(self, member_id) -> str:
        """Displays the relationship in a Social network"""
        relation_nw, appr = {}, 0
        for key, values in self.social_NW.items():
            modified_values = []
            for val in values:
                if val == member_id:
                    appr += 1
                    modified_values.append(val)
            relation_nw[key] = modified_values
        return f"User {member_id} has/have {appr} appearance(s) in our database\n{self.display_network(relation_nw)}"

    def recommend_friend(self, reco_friend):
        x = []
        for friend in self.social_NW[reco_friend]:
            y = set(self.social_NW[reco_friend]).difference(set(self.social_NW[friend]))
            if "".join(y) not in self.social_NW[reco_friend]:
                x.append(y)
        print(x)


class MainProgram(SocialNetwork, SocialNetworkGraph):
    def __init__(self, file_name, user_option):
        super().__init__(file_name)
        self.user_option = user_option
        self.admin_name = None

    @staticmethod
    def intro():
        """A text based command line interface"""
        return str(f"{'_' * 10}SocialMediaManager{'_' * 10}\n"
                   f"| 0: exit from the program           |\n"
                   f"| 1: Load another the database       |\n"
                   f"| 2: Add user to the database        |\n"
                   f"| 3: Remove user from the database   |\n"
                   f"| 4: Show the user with no friends   |\n"
                   f"| 5: Show total friends of the user  |\n"
                   f"| 6: Display the database            |\n"
                   f"| 7: show users with less friends    |\n"
                   f"| 8: Relation diagram in database    |\n"
                   f"| 9: Recommend friend for the user   |\n"
                   f"| 10: Make users friend              |\n"
                   f"{'_' * 38}")


if __name__ == '__main__':
    main = MainProgram(None, None)
    main.admin_name = input("please enter the admin name > ")
    main.file_name = input("please enter the file name > ")
    main.load_file()
    while main.user_option != "0":
        try:
            print(main.intro())
            main.user_option = input(f'{main.admin_name}@{main.file_name}$ ')
            match main.user_option:
                case "1":
                    db_file = input("please enter the database file > ")
                    main = MainProgram(db_file, None)
                    main.load_file()
                case "2":
                    add = input("please enter the user you want to add >")
                    main.add_user(add)
                    print(f"the user {add} has been added to the system")
                case "3":
                    rmv = input("please enter the user you want to remove >")
                    main.remove_user(rmv)
                    print(f'the user {rmv} has been removed')
                case "4":
                    print(main.lonely_users())
                case "5":
                    tfrnd = input("please enter the user name to see all friends >")
                    print(f'{tfrnd} has/have {main.total_friends(tfrnd)} friends')
                case "6":
                    print(main.display_network(main.social_NW))
                case "7":
                    print(main.less_friend())
                case "8":
                    rel = input("please enter the user name to see the relationship in the system >")
                    print(main.show_relations(rel))
                case "9":
                    r_friend = input("please enter the name of the user to recommend friend > ")
                    main.recommend_friend(r_friend)
                case "10":
                    usr1 = input("please enter the first user name  > ")
                    usr2 = input("please enter the second user name > ")
                    print(main.make_friend(usr1, usr2))
            time.sleep(2)
        except (KeyError, FileNotFoundError) as errors:
            print("""ERROR! Possible couses \n
            1 - We try to access a key that does not exist in the dictionary.
            2 - We try to open a file that does not exist. 
                """)
            time.sleep(2)
