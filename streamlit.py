import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.gragh_objects as go
from PIL import Image
# import altair 
import plotly.express as px
# import streamlit_lottie
# st.set_page_config(layout= "wide")
st.set_page_config(page_title="Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

logo_path = r"C:\Users\Senthil\Desktop\DS\Projects I & V\phonepeimage.png"
image = Image.open(logo_path)
st.image(image, width=300)
st.title("PHONEPE DATA VISUALIZATION AND EXPLORATION")

video_path = "C:/Users/Senthil\Desktop/DS/Projects I & V/phonepead.mp4"
css = '''
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.5rem;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)
path3 = r"C:\Users\Senthil\Desktop\DS\Projects I & V\la.png"
image2 = Image.open(path3)
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["***HOME***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "***EXPLORE DATA-CHARTS***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", "***GEO VISULAIZATION***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","***SUNBURST VISULAIZATION***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;",'***REPORTS***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;','***ABOUT US***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;',"***CONTACT US***&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"])

with tab1:
  col1,col2= st.columns(2)
  with col2:
    st.video(video_path)
  with col1:
      st.image(image2, width = 50)
      st.write("PhonePe, established in 2015, has swiftly emerged as a game-changer in India's digital financial realm. Operating on the Unified Payments Interface (UPI), it offers a diverse suite of services encompassing peer-to-peer transfers, bill payments, and seamless online shopping experiences. Its intuitive interface, fortified by stringent security measures, has catapulted PhonePe into the forefront of the country's digital payments landscape, catering to millions seeking a convenient and secure platform. Beyond transactions, PhonePe's commitment to inclusivity is evident through innovative solutions like PhonePe for Business, empowering merchants with digital payment acceptance. Under Flipkart's umbrella since 2016, PhonePe has evolved into a multifaceted financial services platform, extending its offerings to include investments, insurance, and travel bookings, marking its transition from a mere payment facilitator to a comprehensive financial ecosystem. Continuously evolving and embracing innovation, PhonePe's pivotal role in reshaping India's digital economy, fostering financial inclusion, and propelling the nation towards a cashless future remains undeniably significant.")
      st.markdown("[Download PhonePe App](https://www.phonepe.com/app-download/)")
      # st.markdown("[Project GitHub Link](https://github.com/Prashanth292003)")

with tab2:
  col1,col2= st.columns(2)
  logo_path = r"C:\Users\Senthil\Desktop\DS\Projects I & V\answer.png"
  image = Image.open(logo_path)
  col1.image(image, width=300)
  col2.title('EXPLORE HERE')
  ques= col2.selectbox("Select the Question",('Select a Query','Top Brands Of Mobiles Used and transaction count','Type of transaction type, count, amount','States and Districts With Lowest Trasaction Amount',
                                  'States and Districts With Highest Transaction Amount','*Top 10 Districts and states With Lowest Transaction Amount','*Top 10 Districts and states With highest Transaction Amount',
                                  'Top States With AppOpens','Top States With RegesteredUser','States and Districts With Lowest Trasaction Count',"*Top 10 States With AppOpens",
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
            SELECT DISTINCT Transaction_type, Transaction_count
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.bar(Ans,x = 'Brands', y = 'Transaction_count')
      col1.plotly_chart(fig)
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.line(Finals, y= 'highest_transaction_amount', x = 'District' )
      col1.plotly_chart(fig)
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.scatter(Finals, y= 'Transaction_count', x = 'Transaction_type')
      col1.plotly_chart(fig)
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig, ax = plt.subplots()
      ax.bar(Finals['District'], Finals['Lowest_transaction_amount'], color = "purple", hatch = "x")
      ax.set_xlabel('District')
      ax.set_ylabel('Lowest Transaction Amount')
      ax.legend(["Lowest_transaction_amount"])
      col1.pyplot(fig)
      col1.button("Clear") 
       
      
def ques5():
  sql_query5 = """
    SELECT States,District,Years,Quarter, Transaction_count, Transaction_amount
    FROM transaction_count
    order by Transaction_amount ASC
    LIMIT 10;"""
  cursor.execute(sql_query5)
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = ['States','District','Years', 'Quarter','Transaction_count','lowest_transaction_amount'])
  Final['Years'] = Final['Years'].astype(str)
  cursor.close()
  connection.close()
  return Final
  
with tab2 and col2: 
  if ques=='*Top 10 Districts and states With Lowest Transaction Amount':
    if st.button("*Top 10 Districts and states With Lowest Transaction Amount"):
      Finals = ques5()
      col1.write(Finals)
      col1.button("Clear")
      
    
    
    
def ques6():
  sql_query6 = """
    SELECT States,District,Years,Quarter, Transaction_count, Transaction_amount
    FROM transaction_count
    order by Transaction_amount DESC
    LIMIT 10;"""
  cursor.execute(sql_query6)
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = ['States','District','Years','Quarter', 'Transaction_count','highest_transaction_amount'])
  Final['Years'] = Final['Years'].astype(str)
  cursor.close()
  connection.close()
  return Final

with tab2 and col2:   
  if ques=='*Top 10 Districts and states With highest Transaction Amount':
    if st.button("*Top 10 Districts and states With highest Transaction Amount"):
      Finals = ques6()
      col1.write(Finals)
      col1.button("Clear")
    
    
    
def ques7():
  sql_query7 = """
   SELECT States,Years,Quarter,RegisteredUser, AppOpens
   FROM register_user
   order by AppOpens DESC
   LIMIT 10;"""
  cursor.execute(sql_query7)
  results = cursor.fetchall()
  Final = pd.DataFrame(results,columns = [ 'States','Years','Quarter','RegisteredUser', 'AppOpens'])
  Final['Years'] = Final['Years'].astype(str)
  cursor.close()
  connection.close()
  return Final

with tab2 and col2:    
  if ques=='*Top 10 States With AppOpens':
    if st.button("*Top 10 States With AppOpens"):
      Finals = ques7()
      col1.write(Finals)
      col1.button("Clear")



    
def ques8():
  sql_query8 = """
    SELECT  States, Districts, RegisteredUser, AppOpens
    FROM register_user
    WHERE Years = %s AND Quarter = %s AND States = %s
   order by AppOpens DESC,
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.box(Finals['Districts'], Finals['AppOpens'])
      col1.plotly_chart(fig)
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.pie(Finals, names='Districts', values='RegisteredUser')
      col1.plotly_chart(fig)
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig, ax = plt.subplots()
      ax.plot(Finals['District'], Finals['Lowest_Transaction_count'])
      ax.legend(["Lowest_Transaction_count"])
      ax.set_xlabel("District")
      ax.set_ylabel("Lowest_Transaction_count")
      col1.pyplot(fig)
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
  Final = pd.DataFrame(results,columns = [ 'District', 'Transaction_amount', 'Highest_Transaction_count'])
  cursor.close()
  connection.close()
  return Final

with tab2 and col2:   
  if ques=='States and Districts With Highest Transaction Count':
    if st.button('States and Districts With Highest Transaction Count'):
      Finals = ques111()
      col1.write(Finals)
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.pie(Finals, values = 'Highest_Transaction_count', names = 'District')
      col1.plotly_chart(fig)
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      col1.area_chart(Finals, x = 'pincodes',  y = 'Highest_Transaction_count')
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      col1.scatter_chart(Finals, y = 'Lowest_Transaction_count',x= 'pincodes')
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.box( Finals['pincodes'], Finals['Lowest_RegisteredUser'])
      fig.update_layout(title_text='Box Plot')
      col1.plotly_chart(fig)
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
      col1.markdown("""""""        """"""""")
      col1.markdown("""""""        """"""""")
      fig = px.pie(Finals, values = 'Highest_RegisteredUser', names = 'pincodes')
      col1.plotly_chart(fig)
      col1.button("Clear")
      
      
      
      
      
with tab5:
  st.title("Comprehensive Report:")
  col1, col2 = st.columns(2)
  col1.header("Digital Payments in India: A US$10 Tn Opportunity!")
  col1.write("Check out the new PhonePe Pulse - BCG report on what the future holds for digital payments in India.")
  file_path = 'C:/Users/Senthil/Desktop/DS/Projects I & V/report.pdf'
  with open(file_path, 'rb') as file:
    file_content = file.read()
  col1.download_button('Download Report', file_content, key='file_download', file_name='report.pdf')


  logo_path = r"C:\Users\Senthil\Desktop\DS\Projects I & V\imp.png"
  image = Image.open(logo_path)
  # resized_image = image.resize((400, image.size[2]))
  # col2.image(resized_image)
  col2.image(image, width=650)
  

with tab6:
  st.subheader("INDIA'S BEST TRANSACTION APP")
  st.subheader("PhonePe is an Indian digital payments and financial technology company")
  st.subheader("To offer every Indian equal opportunity to accelerate their progress by unlocking the flow of money and access to services")
  col1, col2 = st.columns(2)
  path = "C:/Users/Senthil/Desktop/DS/Projects I & V/PhonePe_Pulse.jpg"
  image = Image.open(path)
  col1.image(image,width=400)
  col2.write("PhonePe, a leading digital payments platform in India, offers a comprehensive range of services, including secure UPI-based money transfers, mobile recharges, bill payments, and online shopping. With a user-friendly interface, the app also provides features like in-app services for food ordering and travel bookings, cashback rewards, and gold purchases. Targeting both consumers and businesses, PhonePe ensures secure transactions, integrates banking services, and introduces innovative offerings such as insurance products. Continuously evolving, PhonePe remains a versatile and trusted platform, playing a pivotal role in the digital payment landscape in India.")
  col2.write("PhonePe's future plans may encompass ongoing innovation, service diversification, and user experience enhancements. This could involve integrating new technologies, forging strategic partnerships, and adapting to changing market needs. To stay informed about PhonePe's latest developments and future strategies, it's advisable to refer to official announcements, press releases, and updates from the company through its website or reliable news sources.")
  A,B,C = st.columns(3)
  B.title("Our Founders")
  col1, col2, col3 = st.columns(3)
  col1.subheader("Sameer Nigam")
  col1.write("Sameer Nigam founded PhonePe in 2015 and serves as its Chief Executive Officer. Before PhonePe, he served as the SVP Engineering and VP Marketing at Flipkart. His Flipkart journey started in 2011 when the company acquired his earlier startup - Mime360, a digital media distribution platform. Sameer has also served as the Director of Product Management at Shopzilla Inc, where he built the company's proprietary shopping search engine. In 2009, he won the coveted Wharton Venture Award, bestowed by the prestigious Wharton Business School. He holds an MBA from the Wharton Business School (University of Pennsylvania), USA, and a Master’s degree in Computer Science from the University of Arizona, Tucson-USA.")
  col2.subheader("Rahul Chari")
  col2.write("Rahul Chari is the Chief Technology officer at PhonePe. He comes with two decades of experience spanning embedded systems, enterprise software development, e-commerce platforms and apps. Prior to PhonePe he was working as the VP Engineering at Flipkart and was responsible for building the best-in-class supply chain system for e-commerce. He joined Flipkart in 2011 through the acquisition of Mallers Inc where he served as the Chief Technology Officer and built Mime360, their flagship product. Prior to Mallers, Rahul was with the Data Center Business Unit at Cisco Systems where he was part of the team that developed the market changing MDS 9000 family of SAN switches. He is named on multiple storage virtualization related patents. Rahul holds a Masters degree in Computer Science from Purdue University, USA and a Bachelor's degree in Computer Engineering from Bombay (Mumbai) University, India (Gold Medalist).")
  col3.subheader("Burzin Engineer")
  col3.write("Burzin is the Chief Reliability Officer at PhonePe. He has more than 25 years of experience in the dot-com space. During his stint at PhonePe, he has built web scale infrastructure and led multiple engineering projects including running and building PhonePe's web serving layer, cloud systems, network, storage and CDN. He’s passionate about building software at scale. Previously, he helped build Mime360, the flagship product at Mallers Inc. He set up their web services, Internal-IT, Application Engineering, Storage Networks and Configuration Services. While at Mallers Inc, he helped redesign the company’s infrastructure for unprecedented growth (100% year over). He holds a Master of Science in Computer Science from the University of Southern California.")



with tab7:
  col1, col2 = st.columns(2)
  path = "C:/Users/Senthil/Desktop/DS/Projects I & V/video1.mp4"
  col2.video(path)
  col1.subheader("Customer Support")
  col1.write("To get instant help, tap  on your PhonePe app home screen & select the relevant topic.")
  col1.write("OR tap below.")
  col1.markdown("[GET HELP ---->](https://support.phonepe.com/)")
  col1.markdown("""      """)
  col1.write("To reach us by phone, tap below")
  col1.write('080-68727374 / 022-68727374')
  
  
  
  
  
  
with tab3:
  st.subheader("EXPLORE HERE")
  A = st.selectbox("select", ['Select',"Aggregated","Map"])
  Y = st.selectbox("Select",["Select","Transaction", "User"])



latitude_longitude_data = {
    'Latitude': [
        15.9129, 28.2180, 26.2006, 25.0961, 21.2787,
        15.2993, 22.2587, 29.0588, 32.2396, 23.6102,
        15.3173, 10.8505, 22.9734, 19.7515, 24.6637,
        25.4670, 23.1645, 26.1584, 20.9517, 31.1471,
        30.9000, 27.0238, 27.5330, 11.1271, 18.1124,
        23.9408, 26.8467, 28.6304, 25.000, 58.0000, 85.0000, 98.000, 98.7000, 58.0000, 87.0000, 96.0000
    ],
    'Longitude': [
        79.7400, 94.7278, 92.9376, 85.3131, 81.8661,
        74.1240, 71.1924, 76.0856, 77.8375, 85.2799,
        75.7131, 76.2711, 78.6569, 75.7139, 93.9063,
        91.3662, 92.9376, 94.5624, 85.0985, 76.1937,
        75.5000, 74.2179, 88.6065, 78.6569, 79.0193,
        91.9882, 80.9462, 77.1025, 87.000, 85.000, 85.0000, 98.000, 98.7000, 58.000, 87.0000, 96.0000
    ]
}

df_lat_lon = pd.DataFrame(latitude_longitude_data)

states = [
    "Andaman & Nicobar Islands",
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chandigarh",
    "Chhattisgarh",
    "Dadra & Nagar Haveli & Daman & Diu",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu & Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Ladakh",
    "Lakshadweep",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Puducherry",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
data = pd.DataFrame(states, columns=['states'])
# result_df = pd.concat([data, df_lat_lon], axis=1)


def geo1():
  sql_query2 = """
    SELECT  Transaction_count
    FROM type_of_pay
    WHERE Years = %s AND Quarter = %s  AND Transaction_type = %s
    ORDER BY States ASC"""
  cursor.execute(sql_query2,(B, C, D))
  results = cursor.fetchall()
  df1 = pd.DataFrame(results, columns = [ 'Transaction_count'])
  df4 = pd.concat([df_lat_lon,data ,df1], axis=1)
  return df4



with tab3:
  def geoo(Q):
    fig = px.choropleth(
      Q,
      geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
      featureidkey='properties.ST_NM',
      locations='states',
      color='Transaction_count',
      color_continuous_scale='Reds',
      title=D
)
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
  



with tab3:
  if A is 'Aggregated' and Y is 'Transaction':
    D = st.selectbox("select Transaction_type", ['Select',"Recharge & bill payments","Peer-to-peer payments","Merchant payments",'Financial Services',"Others"])
    if D!='Select':
        B = st.selectbox("select Year", ['Select',"2018","2019","2020",'2021','2022','2023'])
        Years = B
        if B!='Select':
            C = st.selectbox("select Quarter", ['Select',"1","2","3",'4'])
            if C!='Select':
              S = geo1()
              if S is not None:
                geoo(S)
                
  
  
  
  
def geo2():
  sql_query2 = """
    SELECT Transaction_count
    FROM type_of_brand
    WHERE Years = %s AND Quarter = %s  AND Transaction_type = %s
    ORDER BY States ASC"""
  cursor.execute(sql_query2,(B, C, D))
  results = cursor.fetchall()
  df1 = pd.DataFrame(results, columns = ['Transaction_count'])
  df4 = pd.concat([df_lat_lon,data ,df1], axis=1)
  return df4
with tab3:
  def geoo1(Q):
    fig = px.choropleth(
      Q,
      geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
      featureidkey='properties.ST_NM',
      locations='states',
      color='Transaction_count',
      color_continuous_scale='Reds',
      title=D
)
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
    return 'success'


with tab3:
  if A == 'Aggregated' and Y == 'User':
    D = st.selectbox("select Brand_Type", ['Select','Xiaomi' ,'Samsung', 'Vivo' ,'Oppo' ,'OnePlus', 'Realme', 'Apple' ,'Motorola', 'Lenovo' ,'Huawei', 'Others' ,'Tecno' ,'Gionee' ,'Infinix' ,'Asus' ,'Micromax' ,'HMD' ,'Global', 'Lava' ,'COOLPAD', 'Lyf'])              
    if D!='Select':
        B = st.selectbox("select Year", ['Select',"2018","2019","2020",'2021','2022','2023'])
        Years = B
        if B!='Select':
            C = st.selectbox("select Quarter", ['Select',"1","2","3",'4'])
            if C!='Select':
              S = geo2()
              if S is not None:
                geoo1(S)
                
                
                            
                

def geo3():
  sql_query2 = """
    SELECT SUM(Transaction_count), SUM(Transaction_amount)
    FROM transaction_count
    WHERE Years = %s AND Quarter = %s
    GROUP BY States
    ORDER BY States ASC"""
  cursor.execute(sql_query2,(B, C))
  results = cursor.fetchall()
  df1 = pd.DataFrame(results, columns = ['Transaction_count',"Transaction_amount"])
  df4 = pd.concat([df_lat_lon,data ,df1], axis=1)
  return df4


with tab3:
  def geoo3(Q):
    fig = px.choropleth(
      Q,
      geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
      featureidkey='properties.ST_NM',
      locations='states',
      color='Transaction_count',
      hover_data=['Transaction_count', 'Transaction_amount'],
      color_continuous_scale='Reds',
    
)
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
    return 'success'


with tab3:
  if A == 'Map' and Y == 'Transaction':
    if Y:
        B = st.selectbox("select Year", ['Select',"2018","2019","2020",'2021','2022','2023'])
        Years = B
        if B!='Select':
            C = st.selectbox("select Quarter", ['Select',"1","2","3",'4'])
            if C!='Select':
              S = geo3()
              if S is not None:
                geoo3(S)     
                
                
                
def geo4():
  sql_query2 = """
    SELECT SUM(RegisteredUser),  SUM(AppOpens)
    FROM register_user
    WHERE Years = %s AND Quarter = %s
    GROUP BY States
    ORDER BY States ASC"""
  cursor.execute(sql_query2,(B, C))
  results = cursor.fetchall()
  df1 = pd.DataFrame(results, columns = ['RegisteredUser',"AppOpens"])
  df4 = pd.concat([df_lat_lon,data ,df1], axis=1)
  return df4              
with tab3:               
  def geoo4(Q):
    fig = px.choropleth(
      Q,
      geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
      featureidkey='properties.ST_NM',
      locations='states',
    # color='AppOpens',
      hover_data=['RegisteredUser',"AppOpens"],
    # color_continuous_scale='Reds',
    
)
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
    return 'success'

with tab3:
  def geoo5(Q):
    fig = px.choropleth(
      Q,
      geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
      featureidkey='properties.ST_NM',
      locations='states',
      color='AppOpens',
      animation_frame='RegisteredUser',  
)
    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig)
    return 'success'


with tab3:
  if A == 'Map' and Y == 'User':
    if Y:
        B = st.selectbox("select Year", ['Select',"2018","2019","2020",'2021','2022','2023'])
        Years = B
        if B!='Select':
            C = st.selectbox("select Quarter", ['Select',"1","2","3",'4'])
            if C!='Select':
              S = geo4()
              if S is not None:
                geoo4(S)
                geoo5(S)





query1 = """select distinct(States) from type_of_pay"""
cursor.execute(query1)
P = cursor.fetchall()
V = pd.DataFrame(P, columns =["States"])


def sun1(Q,W,E):
    query = """SELECT Transaction_type, Transaction_count, Transaction_amount FROM type_of_pay
               WHERE States = %s AND Years = %s AND Quarter = %s"""
    cursor.execute(query, (Q, W, E))
    F = cursor.fetchall()
    Z = pd.DataFrame(F, columns=['Transaction type', 'Transaction count', 'Transaction amount'])
    # with st.spinner("Please Wait..."):
    fig = px.sunburst(Z, path=['Transaction type', 'Transaction count', 'Transaction amount'], hover_data={'Transaction count': True, 'Transaction amount': True} )
    fig.update_layout(width = 800,height = 700)
    fi = px.bar(Z, x ='Transaction type' , y = 'Transaction count')
    return fig, fi
  
def sun2(Q,W,E):
    query = """SELECT Transaction_type, Transaction_count FROM type_of_brand
               WHERE States = %s AND Years = %s AND Quarter = %s"""
    cursor.execute(query, (Q, W, E))
    F = cursor.fetchall()
    Z = pd.DataFrame(F, columns=['Transaction type', 'Transaction count'])
    fig = px.sunburst(Z, path=['Transaction type', 'Transaction count'], hover_data={'Transaction count': True, 'Transaction type': True} )
    fig.update_layout(width = 800,height = 700)
    fi = px.bar(Z, x ='Transaction type' , y = 'Transaction count')
    return fig, fi
  
with tab4:
    st.subheader("EXPLORE HERE")
    M = st.selectbox("Select",['Select',"Aggregated","Map",'Top'])

with tab4:
  if M!='Select'and M=='Aggregated':
    l = st.selectbox("Select",['Select','Type of Payment', 'Type of Brands'])
    if l!='Select' and l=='Type of Brands':
      Q = st.selectbox("Select",['Select States']+list(V['States']))
      W = st.selectbox("Select", ["Select Year", "2018", '2019', '2020', '2021', '2022', '2023'])
      E = st.selectbox("Select Quarter", ['Select Quarter','1', '2', '3', '4'])
      if E!='Select Quarter' and Q!='Select States' and W!='Select Year':
        B,U = sun2(Q, W, E)
        st.plotly_chart(B)
        st.plotly_chart(U)
        
        
    if l!='Select' and l=='Type of Payment': 
      Q = st.selectbox("Select",['Select States']+list(V['States']))
      W = st.selectbox("Select", ["Select Year", "2018", '2019', '2020', '2021', '2022', '2023'])
      E = st.selectbox("Select Quarter", ['Select Quarter','1', '2', '3', '4'])
      if E!='Select Quarter' and Q!='Select States' and W!='Select Year':
          B,K = sun1(Q, W, E)
          st.plotly_chart(B)
          st.plotly_chart(K)
          




def sun3(Q,W,E):
    query = """select District,Transaction_count ,Transaction_amount from transaction_count
         where States = %s and  Years = %s and Quarter = %s"""
    cursor.execute(query, (Q, W, E))
    F = cursor.fetchall()
    Z = pd.DataFrame(F, columns=['District', 'Transaction count','Transaction_amount'])
    fig = px.sunburst(Z, path=['District', 'Transaction count','Transaction_amount'], hover_data={'District': True, 'Transaction count': True,'Transaction_amount':True} )
    fig.update_layout(width = 800,height = 700)
    fi = px.bar(Z, x = 'District', y = 'Transaction_amount')
    return fig, fi




def sun4(Q,W,E):
    query = """select Districts, RegisteredUser, AppOpens from register_user
     where States = %s and  Years = %s and Quarter = %s"""
    cursor.execute(query, (Q, W, E))
    F = cursor.fetchall()
    Z = pd.DataFrame(F, columns=['District', 'RegisteredUser','AppOpens'])
    fig = px.sunburst(Z, path=['District', 'RegisteredUser','AppOpens'], hover_data={'District': True, 'RegisteredUser': True,'AppOpens':True} )
    fig.update_layout(width = 800,height = 700)
    fi = px.bar(Z, x ='District' , y = 'RegisteredUser')
    return fig, fi


with tab4:
  if M=='Map':
    k = st.selectbox("Select",["Select","Total Transaction Count, Amount by Districts","Total Register User, AppOpens by Districts"])
    if k!='Select' and k=="Total Transaction Count, Amount by Districts":
      Q = st.selectbox("Select",['Select States']+list(V['States']))
      W = st.selectbox("Select", ["Select Year", "2018", '2019', '2020', '2021', '2022', '2023'])
      E = st.selectbox("Select Quarter", ['Select Quarter','1', '2', '3', '4'])
      if E!='Select Quarter' and Q!='Select States' and W!='Select Year':
        B,T = sun3(Q, W, E)
        st.plotly_chart(B)
        st.plotly_chart(T)
        
  
    if k!='Select' and k=="Total Register User, AppOpens by Districts":
        Q = st.selectbox("Select",['Select States']+list(V['States']))
        W = st.selectbox("Select", ["Select Year", "2018", '2019', '2020', '2021', '2022', '2023'])
        E = st.selectbox("Select Quarter", ['Select Quarter','1', '2', '3', '4'])
        if E!='Select Quarter' and Q!='Select States' and W!='Select Year':
          B, H = sun4(Q, W, E)
          st.plotly_chart(B) 
          st.plotly_chart(H)
               
                
                
                
                
def sun5(Q,W,E):
    query = """select RegisteredUser,Pincodes from top_user
where States = %s and  Years = %s and Quarter = %s"""
    cursor.execute(query, (Q, W, E))
    F = cursor.fetchall()
    Z = pd.DataFrame(F, columns=[ 'RegisteredUser','Pincodes'])
    fig = px.sunburst(Z, path=[ 'Pincodes','RegisteredUser'], hover_data={ 'RegisteredUser': True,'Pincodes':True} )
    fig.update_layout(width = 800,height = 700)
    return fig                
                
                
                
                
def sun6(Q,W,E):
    query = """select transaction_count,Transaction_amount,pincodes from top_transaction
where States = %s and  Years = %s and Quarter = %s"""
    cursor.execute(query, (Q, W, E))
    F = cursor.fetchall()
    Z = pd.DataFrame(F, columns=[ 'Transaction_count','pincodes','Transaction_amount'])
    fig = px.sunburst(Z, path=[ 'pincodes','Transaction_count','Transaction_amount'], hover_data={ 'Transaction_amount': True,'pincodes':True,"Transaction_count":True} )
    fig.update_layout(width = 800,height = 700)
    return fig
                
                

with tab4:
  if M=='Top':
    k = st.selectbox("Select",["Select","Total Transaction Count, Amount by Pincodes","Total Register User by Pincodes"])
    if k!='Select' and k=="Total Register User by Pincodes":
      Q = st.selectbox("Select",['Select States']+list(V['States']))
      W = st.selectbox("Select", ["Select Year", "2018", '2019', '2020', '2021', '2022', '2023'])
      E = st.selectbox("Select Quarter", ['Select Quarter','1', '2', '3', '4'])
      if E!='Select Quarter' and Q!='Select States' and W!='Select Year':
        B = sun5(Q, W, E)
        st.plotly_chart(B)
  
    if k!='Select' and k=="Total Transaction Count, Amount by Pincodes":
        Q = st.selectbox("Select",['Select States']+list(V['States']))
        W = st.selectbox("Select", ["Select Year", "2018", '2019', '2020', '2021', '2022', '2023'])
        E = st.selectbox("Select Quarter", ['Select Quarter','1', '2', '3', '4'])
        if E!='Select Quarter' and Q!='Select States' and W!='Select Year':
          B = sun6(Q, W, E)
          st.plotly_chart(B)             
                
                
            
            
            
            
            

    
  
  


