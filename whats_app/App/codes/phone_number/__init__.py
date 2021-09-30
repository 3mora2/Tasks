import pandas

data = pandas.read_csv('./countries.csv', sep=';', names=["code", "name", "en_name", "ar_name", "calling_code"],
                       header=None)
series = data.get("ar_name")
series.index = data.get("calling_code")
countries = series.to_dict()

# result = list(filter(lambda x: '+04002894519'.startswith('+' + str(x).replace(' ', '')), countries.keys()))
# if result:
#     really = max(result, key=lambda x: len(x))
# else:
#     really = None
# print(result, really, countries[really])
