from DataCollection.AddVotesInPrevElections.AddVoted import AddVoted

__author__ = 'lizzybradley'

av = AddVoted('../Data/2_pages_created.csv')
av.add_voted()
av.print_newData()