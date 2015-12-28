from DataCollection.AddPagesCreated.PagesCreated import PagesCreated

# reader = DataReader.DataReader()
#
# reader.read_file()
# reader.save_usernames()

# pc = PagesCreated()
# pc.append_pages_created("1_year_joined.csv", "data2.csv")

pc = PagesCreated()
pc.append_pages_created("FixDates/time_outs.csv", "fix_time_outs.csv")