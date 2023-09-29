# builtin funcs https://docs.python.org/3.12/library/functions.html
# libs https://docs.python.org/3.12/library/index.html
import pandas as pd
import json
import numpy as np

# JSON.stringify([...document.querySelectorAll(".content li")].filter(n => n.querySelector(".label-error")).map(n => n.querySelector("a").text))

with open("asgen.json") as f:
    errs = json.load(f)

cols = ["rank", "name", "installs"]
df = pd.read_csv('popcon.csv', sep=r'\s+',
                 comment='#', names=cols, usecols=range(len(cols)), skipfooter=2)
df = df[df.name.isin(errs)]
df.installs /= 1000
df.installs = df.installs.map(lambda x: np.format_float_positional(
    x, precision=2, unique=False, fractional=False, trim='k'))

df.to_html("output.html", index=False,
           justify="center", border=0, col_space=0)

# print(type(df.iloc[0])) <class 'pandas.core.series.Series'>
# print(type(df)) <class 'pandas.core.series.Series'>
# print(type(df.get("name")))
