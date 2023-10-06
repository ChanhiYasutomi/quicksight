cnt_cumsum
count(cumsum)

shift_cumsum
lag(
     count(cumsum),
     [{cnt_cumsum} DESC],
     1,
     [product]
)

shift_cumsum
lag(
     count(cumsum),
     [{cnt_cumsum} DESC],
     1
)

repeat_rate
{cnt_cumsum} / {shift_cumsum}

num_contract
sum(ifelse({contract_flag} = 1, 1, 0))

num_churn
sum(ifelse({contract_flag} = 0, 1, 0))

cumsum_contract
runningSum
(
  sum(ifelse({contract_flag} = 1, 1, 0)),
  [truncDate("MM",{date}) ASC]
)

cumsum_churn
runningSum
(
  sum(ifelse({contract_flag} = 0, 1, 0)),
  [truncDate("MM",{date}) ASC]
)

num_stay
{cumsum_contract} - {cumsum_churn}

flag_0_repurchase_1
sum(ifelse({flag} = 0 and {repurchase} = 1, 1, 0))

flag_repurchase_1
sum(ifelse({flag} = 1 and {repurchase} = 1, 1, 0))

flag_0
sum(ifelse({flag} = 0, 1, 0))

flag_0_rep_rate
(sum(ifelse({flag} = 0 and {repurchase} = 1, 1, 0))) / (sum(ifelse({flag} = 0, 1, 0)))

flag_1
sum(ifelse({flag} = 1, 1, 0))

flag_1_rep_rate
(sum(ifelse({flag} = 1 and {repurchase} = 1, 1, 0))) / (sum(ifelse({flag} = 1, 1, 0)))
