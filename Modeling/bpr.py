import scipy.sparse as sp
import pandas as pd
import implicit.cpu.evaluation as eval
import implicit
import numpy as np
df = pd.read_csv("orders.inter",sep="\t")
# print(df)
df["score"] = 1
#sample random suubset of users ffor eval
users = df["user_id:token"].unique()
np.random.shuffle(users)
train_users = users[:int(len(users)*0.9)]
test_users = users[int(len(users)*0.9):]

df.sort_values(by="last_time_ordered:float",inplace=True)

train_df = df[df["user_id:token"].isin(train_users)]
test_df = df[df["user_id:token"].isin(test_users)]

test_df_x = test_df.groupby("user_id:token").apply(lambda x: x.head(int(x.shape[0]*0.9))-1).reset_index(drop=True)
test_df_y = test_df.groupby("user_id:token").apply(lambda x: x.tail(int(x.shape[0]*0.1))+1).reset_index(drop=True)
print(test_df_x.columns)
n_items = df['product_id:token'].max()+1
sparse_train = sp.csr_matrix((train_df['score'], (train_df['user_id:token'], train_df['product_id:token'])),
                       shape=(train_df['user_id:token'].max()+1, n_items ),dtype=float)
sparse_test_x = sp.csr_matrix((test_df_x['score'], (test_df_x['user_id:token'], test_df_x['product_id:token'])),
                       shape=(test_df_x['user_id:token'].max()+1, n_items ),dtype=float)
sparse_test_y = sp.csr_matrix((test_df_y['score'], (test_df_y['user_id:token'], test_df_y['product_id:token'])),
                       shape=(test_df_y['user_id:token'].max()+1, n_items ),dtype=float)

good_rows = sparse_test_x.getnnz(1)>0
sparse_test_x = sparse_test_x[good_rows,:]
sparse_test_y = sparse_test_y[good_rows,:]
# train = sparse[:(sparse.shape[0]*9)//10]

model = implicit.bpr.BayesianPersonalizedRanking(factors=128, iterations=200)
model.fit(sparse_train)

k = 20
ndcg = eval.ndcg_at_k(model,sparse_test_x,sparse_test_y,K=k)
print("ndcg@{}:{}".format(k,ndcg))
