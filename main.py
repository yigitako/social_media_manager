# Author :: Yiǧit Akoymak Date :: 19.05.2023
# Basic social media program
class SocialNetworkGraph:
    def __init__(self, file_name):
        self.file_name = file_name
        self.social_NW = {}
        self.pretty_display = ""
        self.admin_name = ""

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
        """a formatted string representation of the social_NW"""
        for keys, values in network.items():
            self.pretty_display += f"{keys}  --> {', '.join(values)} \n"
        return self.pretty_display


class SocialNetwork(SocialNetworkGraph):
    def __init__(self, file_name):
        super().__init__(file_name)

    def total_friends(self, t_friends) -> int:
        """Returns the total amount of friends for a single user"""
        return len(self.social_NW[t_friends])

    def lonely_users(self) -> list:
        """Returns users with no friend at all"""
        return [usr for usr in self.social_NW.keys() if len(self.social_NW[usr]) < 1]

    def less_friend(self) -> str:
        """Returns users with friends fewer friends
        stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary"""
        min_val = min(filter(lambda m_val: m_val != 0, map(len, self.social_NW.values())))
        less_f = [item for item in self.social_NW if len(self.social_NW[item]) == min_val]
        return less_f, min_val

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

    def recommend_friend(self):
        pass


class MainProgram(SocialNetworkGraph):
    def main(self):
        self.admin_name = input("Please enter the admin name to proceed.")
        """User interactions | python 3.10 needed for this program to run"""
        print(f"{'_' * 10}SocialMediaManager{'_' * 10}\n"
              f"| 1: Load the database               |\n"
              f"| 2: Add user to the database        |\n"
              f"| 3: Remove user from the database   |\n"
              f"| 4: Show the user with no friends   |\n"
              f"| 5: Show total friends of the user  |\n"
              f"| 6: Display the database            |\n"
              f"| 7: show users with less friends    |\n"
              f"| 8: Relation diagram in database    |\n"
              f"| 9: Recommend friend for the user   |\n"
              f"{'_' * 38}")
        usr_inp = input(f'{self.admin_name}@{self.file_name}$ ')
        match usr_inp:
            case "1":
                pass


if __name__ == "__main__":
    MainProgram("social_nw.txt").main()
