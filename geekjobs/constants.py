from collections import OrderedDict

# bundeslander = {'DE': 'Germany', 'BW': 'Baden-Wuerttemberg', 'BY': 'Bayern', 'BE': 'Berlin', 'BB': 'Brandenburg',
#                'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern', 'NI': 'Niedersachsen',
#                'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz', 'SL': 'Saarland', 'SN': 'Sachsen',
#                'ST': 'Sachen-Anhalt', 'SH': 'Schleswig-Holstein', 'TH': 'Thuringia'}

bundeslander = OrderedDict(
        [('DE', 'Germany'), ('REMOTE', 'Remote'), ('BW', 'Baden-Württemberg'), ('BY', 'Bayern'), ('BE', 'Berlin'),
         ('BB', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hessen'), ('MV', 'Mecklenburg-Vorpommern'),
         ('NI', 'Niedersachsen'), ('NW', 'Nordrhein-Westfalen'), ('RP', 'Rheinland-Pfalz'), ('SL', 'Saarland'),
         ('SN', 'Sachsen'), ('ST', 'Sachen-Anhalt'), ('SH', 'Schleswig-Holstein'), ('TH', 'Thüringen')])

bundeslander2 = {'DE': 'Germany', 'REMOTE': 'Remote', 'BW': 'Baden-Wuerttemberg', 'BY': 'Bayern', 'BE': 'Berlin',
                 'BB': 'Brandenburg', 'HB': 'Bremen', 'HH': 'Hamburg', 'HE': 'Hessen', 'MV': 'Mecklenburg-Vorpommern',
                 'NI': 'Niedersachsen', 'NW': 'Nordrhein-Westfalen', 'RP': 'Rheinland-Pfalz', 'SL': 'Saarland',
                 'SN': 'Sachsen', 'ST': 'Sachen-Anhalt', 'SH': 'Schleswig-Holstein', 'TH': 'Thuringia'}

DE_STATE_CHOICES = (('Germany', 'Germany'), ('BW', 'Baden-Württemberg'), ('BY', 'Bayern'), ('BE', 'Berlin'),
                    ('BB', 'Brandenburg'), ('HB', 'Bremen'), ('HH', 'Hamburg'), ('HE', 'Hessen'),
                    ('MV', 'Mecklenburg-Vorpommern'), ('NI', 'Niedersachsen'), ('NW', 'Nordrhein-Westfalen'),
                    ('RP', 'Rheinland-Pfalz'), ('SL', 'Saarland'), ('SN', 'Sachsen'), ('ST', 'Sachen-Anhalt'),
                    ('SH', 'Schleswig-Holstein'), ('TH', 'Thüringen'))