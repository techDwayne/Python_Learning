import pandas as pd
import numpy as np
dates = pd.date_range('20220701', periods=8)
print(dates)
df=pd.DataFrame(np.random.randn(8,4),index=dates,columns=list('ABCD'))
print(df)
df2=pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20220701"),
        "C": pd.Series(1,index=list(range(4)),dtype="float32"),
        "D": np.array([3]*4,dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
print(df.head())
print(df.tail())

