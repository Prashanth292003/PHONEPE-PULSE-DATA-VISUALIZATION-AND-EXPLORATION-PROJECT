import mysql.connector
import streamlit as st
import pandas as pd
from PIL import Image
# st.set_page_config(layout= "wide")
st.set_page_config(page_title="Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

logo_path = r"C:\Users\Senthil\Downloads\phonepeimage.png"
image = Image.open(logo_path)
st.image(image, width=300)

video_path = "C:/Users/Senthil/Downloads/phonepead.mp4"
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.5rem;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)
tab1, tab2, tab3, tab4 = st.tabs(["***HOME***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "***EXPLORE DATA***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "***DATA VISULAIZATION***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", '***REPORTS***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'])

with tab1:
  st.title("PHONEPE DATA VISUALIZATION AND EXPLORATION")
with tab1:
  col1,col2= st.columns(2)
  with col2:
    st.video(video_path)
  with col1:
      st.header("About PhonePe")
      st.write("PhonePe, established in 2015, has swiftly emerged as a game-changer in India's digital financial realm. Operating on the Unified Payments Interface (UPI), it offers a diverse suite of services encompassing peer-to-peer transfers, bill payments, and seamless online shopping experiences. Its intuitive interface, fortified by stringent security measures, has catapulted PhonePe into the forefront of the country's digital payments landscape, catering to millions seeking a convenient and secure platform. Beyond transactions, PhonePe's commitment to inclusivity is evident through innovative solutions like PhonePe for Business, empowering merchants with digital payment acceptance. Under Flipkart's umbrella since 2016, PhonePe has evolved into a multifaceted financial services platform, extending its offerings to include investments, insurance, and travel bookings, marking its transition from a mere payment facilitator to a comprehensive financial ecosystem. Continuously evolving and embracing innovation, PhonePe's pivotal role in reshaping India's digital economy, fostering financial inclusion, and propelling the nation towards a cashless future remains undeniably significant.")
      st.markdown("[Download PhonePe App](https://www.phonepe.com/app-download/)")
      # st.markdown("[Project GitHub Link](https://github.com/Prashanth292003)")

with tab2:
  col1,col2= st.columns(2)
  logo_path = r"C:\Users\Senthil\Downloads\answer.png"
  image = Image.open(logo_path)
  col1.image(image, width=300)
  col2.title('EXPLORE HERE:')
  ques= col2.selectbox("Select the Question",('Select a Query','Top Brands Of Mobiles Used and transaction count','Type of transaction type, count, amount','States and Districts With Lowest Trasaction Amount',
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
with tab2:
  selected_option = col2.selectbox("Select an years", ["Select","2018", "2019","2020","2021","2022","2023"])
  selected_option1 = col2.selectbox("Select Quarter", ["Select","1", "2","3","4"])
  selected_option2 = col2.selectbox("Select States",['Select State'] + state_options)
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
with tab2 and col2:       
  if ques=="Top Brands Of Mobiles Used and transaction count":
    if st.button("Top Brands Of Mobiles Used and transaction count"):
      Ans = ques1()
      col1.write(Ans)
      col1.button("Clear")

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
  
with tab2 and col2: 
  if ques=='States and Districts With Highest Transaction Amount':
    if st.button("States and Districts With Highest Transaction Amount"):
      Finals = ques2()
      col1.write(Finals)
      col1.button("Clear")
    
    
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

with tab2 and col2:   
  if ques=='Type of transaction type, count, amount':
    if st.button("Type of transaction type , count, amount"):
      Finals = ques3()
      col1.write(Finals)
      col1.button("Clear")
    
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

with tab2 and col2:  
  if ques=='States and Districts With Lowest Trasaction Amount':
    if st.button("States and Districts With Lowest Trasaction Amount"):
      Finals = ques4()
      col1.write(Finals)
      col1.button("Clear") 
      
      
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
  
with tab2 and col2: 
  if ques=='Top 10 Districts and states With Lowest Transaction Amount':
    if st.button("Top 10 Districts and states With Lowest Transaction Amount"):
      Finals = ques5()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
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

with tab2 and col2:   
  if ques=='Top 10 Districts and states With highest Transaction Amount':
    if st.button("Top 10 Districts and states With highest Transaction Amount"):
      Finals = ques6()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
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

with tab2 and col2:    
  if ques=='Top 10 States With AppOpens':
    if st.button("Top 10 States With AppOpens"):
      Finals = ques7()
      col1.write(Finals)
      col1.button("Clear")



    
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

with tab2 and col2:    
  if ques=='Top States With AppOpens':
    if st.button("Top States With AppOpens"):
      Finals = ques8()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
    
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
  
with tab2 and col2: 
  if ques=='Top States With RegesteredUser':
    if st.button("Top States With RegesteredUser"):
      Finals = ques9()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
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

with tab2 and col2:   
  if ques=='States and Districts With Lowest Trasaction Count':
    if st.button('States and Districts With Lowest Trasaction Count'):
      Finals = ques10()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
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

with tab2 and col2:   
  if ques=='States and Districts With Highest Transaction Count':
    if st.button('States and Districts With Highest Transaction Count'):
      Finals = ques111()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
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

with tab2 and col2:    
  if ques=='Top Transaction count with States and pincodes':
    if st.button('Top Transaction count with States and pincodes'):
      Finals = ques12()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
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

with tab2 and col2:  
  if ques=='Least Transaction count with States and pincodes':
    if st.button('Least Transaction count with States and pincodes'):
      Finals = ques13()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
    
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

with tab2 and col2:  
  if ques=='Least RegisteredUser with States and pincodes':
    if st.button('Least RegisteredUser with States and pincodes'):
      Finals = ques14()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
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

with tab2 and col2:    
  if ques=='Top RegisteredUser with States and pincodes':
    if st.button('Top RegisteredUser with States and pincodes'):
      Finals = ques15()
      col1.write(Finals)
      col1.button("Clear")
      
      
      
      
      
with tab4:
  st.title("Comprehensive Report:")
  col1, col2 = st.columns(2)
  col1.header("Digital Payments in India: A US$10 Tn Opportunity!")
  col1.write("Check out the new PhonePe Pulse - BCG report on what the future holds for digital payments in India.")
  file_path = 'C:/Users/Senthil/Downloads/report.pdf'
  with open(file_path, 'rb') as file:
    file_content = file.read()
  col1.download_button('Download Report', file_content, key='file_download', file_name='report.pdf')


  logo_path = r"C:\Users\Senthil\Downloads\imp.png"
  image = Image.open(logo_path)
  # resized_image = image.resize((400, image.size[2]))
  # col2.image(resized_image)
  col2.image(image, width=650)