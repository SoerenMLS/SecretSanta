from flask_table import Table, Col


class SantaTable(Table):
    html_attrs = {'id': 'santaTable'}
    santa = Col('Santa')
    description = Col('Description')


class SantaItem(object):
    def __init__(self, santa='santa', description='description'):
        self.santa = santa
        self.description = description


santa_items = [SantaItem('santa1', 'owner'),
               SantaItem('santa2', 'participant'),
               SantaItem('santa3', 'participant')]

table = SantaTable(santa_items)
