## import modules here 
import pandas as pd
import numpy as np
from itertools import product
from lab02 import helper


################### Question 1 ###################

def buc_rec_optimized(df):  # do not change the heading of the function
    if df.shape[0] == 1:
        # single tuple implementation
        row = df.loc[0].values.tolist()
        tup = row[:-1]
        df_bro = []

        for x in list(product([False, True], repeat=len(tup))):
            temp = []

            for i in range(len(x)):
                if not x[i]:
                    temp += [tup[i]]
                else:
                    temp += ['ALL']

            temp += [row[-1]]
            df_bro += [temp]

        return pd.DataFrame(df_bro, columns=df.columns.values.tolist())

    # multiple tuples implementation
    df_bro = pd.DataFrame(columns=df.columns.values.tolist())
    buc_rec_optimized_(df, [], df_bro)

    return df_bro


def buc_rec_optimized_(df, row, df_bro):
    # Note that input is a DataFrame
    dims = df.shape[1]

    if dims == 1:
        # only the measure dim
        input_sum = sum(helper.project_data(df, 0))
        row += [input_sum]

        df_bro.loc[len(df_bro)] = row
    else:
        # the general case
        dim0_vals = set(helper.project_data(df, 0).values)
        temp = [r for r in row]

        for dim0_v in dim0_vals:
            sub_data = helper.slice_data_dim0(df, dim0_v)
            row = [t for t in temp] + [dim0_v]

            buc_rec_optimized_(sub_data, row, df_bro)

        ## for R_{ALL}
        sub_data = helper.remove_first_dim(df)
        row = [t for t in temp] + ['ALL']

        buc_rec_optimized_(sub_data, row, df_bro)


if __name__ == '__main__':
    print(buc_rec_optimized(pd.read_csv('./asset/a_.txt', sep=' ')))
