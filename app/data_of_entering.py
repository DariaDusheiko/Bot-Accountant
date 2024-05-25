import pandas as pd

class Data_enter:
    def __init__(self):
        super(Data_enter, self).__init__()

        try:
            df = pd.read_csv('app/csvy/akks.csv')

        except Exception as err:
            self.server()


    def server(self):
        df = pd.DataFrame(columns=["login", "password", "res", "goal"], )
        df.to_csv('app/csvy/akks.csv', index=False)


    def done_registration(self, login_acc, password_acc):
        df = pd.read_csv('app/csvy/akks.csv')

        df_1 = pd.DataFrame(data=[[login_acc, password_acc, 0, 0]],
                            columns=["login", "password", "res", "goal"])

        df = pd.concat([df, df_1], ignore_index=True)
        df.to_csv('app/csvy/akks.csv', index=False)


    def enter_acc(self, login_acc, password_acc):
        df = pd.read_csv('app/csvy/akks.csv')

        search_log = df[df["login"] == login_acc]
        try:
            inde = search_log.index[0]
            password_list = df.loc[inde, 'password']

            if password_acc != password_list:
                return {"error": "Invalid login data", "inde": ""}
            return {"error": "", "inde": str(inde)}

        except Exception as err:
            return {"error": "Invalid login data", "inde": ""}


    # def change_data(self, inde, what_change, for_change, flag=0):
    #     df = pd.read_csv('app/csvy/akks.csv')
    #     if flag == 11:
    #         df.at[inde, what_change] += for_change
    #     elif:
    #         df.at[inde, "goal"] = for_change
    #         df.at[inde, what_change] = 0
    #     df.to_csv('app/csvy/akks.csv', index=False)

    def del_akk(self, inde):
        df = pd.read_csv('app/csvy/akks.csv')
        df = df.drop(index=inde)
        df.to_csv('app/csvy/akks.csv', index=False)


# if __name__ == "__main__":
#     window = Data_enter()