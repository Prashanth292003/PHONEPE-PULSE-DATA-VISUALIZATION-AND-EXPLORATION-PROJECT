import mysql.connector
import streamlit as st
import pandas as pd
st.title('Phonepe Pulse Data Visualization and Exploration')
ques= st.selectbox("Select the Question",('Select a Query','Top Brands Of Mobiles Used and transaction count','Type of transaction type, count, amount','States and Districts With Lowest Trasaction Amount',
                                  'States and Districts With Highest Transaction Amount','Top 10 Districts and states With Lowest Transaction Amount','Top 10 Districts and states With highest Transaction Amount',
                                  'Top States With AppOpens','Top States With RegesteredUser','States and Districts With Lowest Trasaction Count',"Top 10 States With AppOpens",
                                 'States and Districts With Highest Transaction Count','Top Transaction count with States and pincodes','Least Transaction count with States and pincodes',
                                 'Top RegisteredUser with States and pincodes','Least RegisteredUser with States and pincodes'))
host = "localhost"
user = "root"
password = "PrasHantHCHinnapappal19802003"

# Connect to MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)
cursor = connection.cursor()
cursor.execute('USE phone_pe')
distinct_states_query = "SELECT DISTINCT States FROM type_of_brand"
cursor.execute(distinct_states_query)
distinct_states = cursor.fetchall()
cursor.close()
connection.close()
state_options = [state[0] for state in distinct_states]

selected_option = st.selectbox("Select an years", ["Select","2018", "2019","2020","2021","2022","2023"])
selected_option1 = st.selectbox("Select Quarter", ["Select","1", "2","3","4"])
selected_option2 = st.selectbox("Select States",['Select State'] + state_options)
Years = selected_option
Quarter = selected_option1
States = selected_option2

host = "localhost"
user = "root"
password = "PrasHantHCHinnapappal19802003"
connection = mysql.connector.connect(
           host=host,
           user=user,
           password=password
            )
cursor = connection.cursor()
cursor.execute('USE phone_pe')
def ques1():
  sql_query = """
            SELECT Transaction_type, Transaction_count
            FROM type_of_brand
            WHERE Years = %s AND Quarter = %s AND States = %s
            ORDER BY Transaction_count DESC
            LIMIT 3;
                 """
  cursor.execute(sql_query,(Years,Quarter,States))
  result = cursor.fetchall()
  Ans = pd.DataFrame(result, columns = ['Brands', 'Transaction_count'])
  cursor.close()
  connection.close()
  return Ans      
      
if ques=="Top Brands Of Mobiles Used and transaction count":
  if st.button("Top Brands Of Mobiles Used and transaction count"):
    Ans = ques1()
    st.write(Ans)
    st.button("Clear")

def ques2():
  sql_query2 = """
    SELECT States,District, Transaction_amount AS highest_transaction_amount, Transaction_count
    FROM transaction_count
    WHERE Years = %s AND Quarter = %s AND States = %s
    ORDER BY Transaction_amount DESC
    LIMIT 3;"""
  cursor.execute(sql_query2, (Years,Quarter,States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = ['States','District', 'highest_transaction_amount', 'Transaction_count'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='States and Districts With Highest Transaction Amount':
  if st.button("States and Districts With Highest Transaction Amount"):
    Finals = ques2()
    st.write(Finals)
    st.button("Clear")
    
    
def ques3():
  sql_query3 = """
   SELECT Transaction_type, Transaction_count, Transaction_amount
   FROM type_of_pay
   WHERE Years = %s AND Quarter = %s AND States = %s;"""
  cursor.execute(sql_query3, (Years,Quarter,States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = ['Transaction_type', 'Transaction_count', 'Transaction_amount'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Type of transaction type , count, amount':
  if st.button("Type of transaction type , count, amount"):
    Finals = ques3()
    st.write(Finals)
    st.button("Clear")
    
def ques4():
  sql_query4 = """
    SELECT States,District, Transaction_amount AS Lowest_transaction_amount, Transaction_count
    FROM transaction_count
    WHERE Years = %s AND Quarter = %s AND States = %s
    ORDER BY Transaction_amount ASC
    LIMIT 3;"""
  cursor.execute(sql_query4, (Years,Quarter,States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = ['States','District', 'Lowest_transaction_amount', 'Transaction_count'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='States and Districts With Lowest Trasaction Amount':
  if st.button("States and Districts With Lowest Trasaction Amount"):
    Finals = ques4()
    st.write(Finals)
    st.button("Clear") 
      
      
def ques5():
  sql_query5 = """
    SELECT States,District, Transaction_count, Transaction_amount
    FROM transaction_count
    order by Transaction_amount DESC
    LIMIT 10;"""
  cursor.execute(sql_query5)
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = ['States','District', 'Transaction_count','lowest_transaction_amount'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Top 10 Districts and states With Lowest Transaction Amount':
  if st.button("Top 10 Districts and states With Lowest Transaction Amount"):
    Finals = ques5()
    st.write(Finals)
    st.button("Clear")
    
    
    
def ques6():
  sql_query6 = """
    SELECT States,District, Transaction_count, Transaction_amount
    FROM transaction_count
    order by Transaction_amount DESC
    LIMIT 10;"""
  cursor.execute(sql_query6)
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = ['States','District', 'Transaction_count','highest_transaction_amount'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Top 10 Districts and states With highest Transaction Amount':
  if st.button("Top 10 Districts and states With highest Transaction Amount"):
    Finals = ques6()
    st.write(Finals)
    st.button("Clear")
    
    
    
def ques7():
  sql_query7 = """
   SELECT States,RegisteredUser, AppOpens
   FROM register_user
   order by AppOpens DESC
   LIMIT 10;"""
  cursor.execute(sql_query7)
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States','RegisteredUser', 'AppOpens'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Top 10 States With AppOpens':
  if st.button("Top 10 States With AppOpens"):
    Finals = ques7()
    st.write(Finals)
    st.button("Clear")



    
def ques8():
  sql_query8 = """
    SELECT  States, Districts, RegisteredUser, AppOpens
    FROM register_user
    WHERE Years = %s AND Quarter = %s AND States = %s
   order by AppOpens DESC
   LIMIT 3;"""
  cursor.execute(sql_query8,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States',  'Districts', 'RegisteredUser', 'AppOpens'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Top States With AppOpens':
  if st.button("Top States With AppOpens"):
    Finals = ques8()
    st.write(Finals)
    st.button("Clear")
    
    
    
    
def ques9():
  sql_query9 = """
    SELECT  States, Districts, RegisteredUser
    FROM register_user
    WHERE Years = %s AND Quarter = %s AND States = %s
   order by RegisteredUser DESC
   LIMIT 3;"""
  cursor.execute(sql_query9,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States',  'Districts', 'RegisteredUser'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Top States With RegesteredUser':
  if st.button("Top States With RegesteredUser"):
    Finals = ques9()
    st.write(Finals)
    st.button("Clear")
    
    
    
def ques10():
  sql_query10 = """
   SELECT  District, Transaction_amount, Transaction_count
   FROM transaction_count
   WHERE Years = %s AND Quarter = %s AND States = %s
   order by Transaction_count ASC
   LIMIT 3;"""
  cursor.execute(sql_query10,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'District', 'Transaction_amount', 'Lowest_Transaction_count'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='States and Districts With Lowest Trasaction Count':
  if st.button('States and Districts With Lowest Trasaction Count'):
    Finals = ques10()
    st.write(Finals)
    st.button("Clear")
    
    
    
def ques111():
  sql_query11 = """
   SELECT District, Transaction_amount, Transaction_count
   FROM transaction_count
   WHERE Years = %s AND Quarter = %s AND States = %s
   order by Transaction_count DESC
   LIMIT 3;"""
  cursor.execute(sql_query11,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'District', 'Transaction_amount', 'highest_Transaction_count'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='States and Districts With Highest Transaction Count':
  if st.button('States and Districts With Highest Transaction Count'):
    Finals = ques111()
    st.write(Finals)
    st.button("Clear")
    
    
    
def ques12():
  sql_query12 = """
    SELECT States, pincodes, Transaction_count
    FROM top_transaction 
    WHERE Years = %s AND Quarter = %s AND States = %s
    order by Transaction_count DESC
    LIMIT 3;"""
  cursor.execute(sql_query12,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States', 'pincodes', 'Highest_Transaction_count'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Top Transaction count with States and pincodes':
  if st.button('Top Transaction count with States and pincodes'):
    Finals = ques12()
    st.write(Finals)
    st.button("Clear")
    
    
    
def ques13():
  sql_query13 = """
    SELECT States, pincodes, Transaction_count
    FROM top_transaction 
    WHERE Years = %s AND Quarter = %s AND States = %s
    order by Transaction_count ASC
    LIMIT 3;"""
  cursor.execute(sql_query13,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States', 'pincodes', 'Lowest_Transaction_count'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Least Transaction count with States and pincodes':
  if st.button('Least Transaction count with States and pincodes'):
    Finals = ques13()
    st.write(Finals)
    st.button("Clear")
    
    
    
    
def ques14():
  sql_query14 = """
    SELECT States, pincodes, RegisteredUser
    FROM top_user 
    WHERE Years = %s AND Quarter = %s AND States = %s
    order by RegisteredUser ASC
    LIMIT 3"""
  cursor.execute(sql_query14,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States', 'pincodes', 'Lowest_RegisteredUser'])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Least RegisteredUser with States and pincodes':
  if st.button('Least RegisteredUser with States and pincodes'):
    Finals = ques14()
    st.write(Finals)
    st.button("Clear")
    
    
    
def ques15():
  sql_query15 = """
  SELECT States, pincodes, RegisteredUser
  FROM top_user 
  WHERE Years = %s AND Quarter = %s AND States = %s
  order by RegisteredUser DESC
  LIMIT 3"""
  cursor.execute(sql_query15,(Years, Quarter, States))
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States', 'pincodes', 'Highest_RegisteredUser' ])
  cursor.close()
  connection.close()
  return Final
  
if ques=='Top RegisteredUser with States and pincodes':
  if st.button('Top RegisteredUser with States and pincodes'):
    Finals = ques15()
    st.write(Finals)
    st.button("Clear")