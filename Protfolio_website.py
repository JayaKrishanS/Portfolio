import streamlit as st
import pybase64

st.set_page_config(page_title="Jk Portfolio", page_icon="page_icon.png",layout="wide", initial_sidebar_state="expanded")

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return pybase64.b64encode(data).decode()
img = get_img_as_base64("Background.jpeg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2= st.columns((3,1))

with col1:
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10,tab11 = st.tabs(["Home","---","About me","---","Education","---","Projets","---","Skills","---","Contact"])

with tab1:
    st.markdown("<h1 style='color: red;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: red;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: red;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: red;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: white;'>JAYA KRISHNA S</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: blue;'>   Data Science Aspirant    </h3>", unsafe_allow_html=True)

with tab3:
    st.write("")
    st.write()
    st.markdown("Hello, I'm Jaya Krishna S, a passionate Data Science enthusiast with a background in Bioinformatics. ""I completed my Masters in Bioinformatics and have since embarked on a journey into the captivating world of Data Science.")
    st.markdown("Over the past six months, I'm upskilling my knowledge and applying Data Science techniques to real-world challenges. "
             "This immersive experience has allowed me to develop a strong foundation in data visualization and machine learning. "
             "I have successfully completed several projects that demonstrate my skills in these areas, which you can explore in the Projects section of this website.")
    st.markdown("As a Data Scientist, I am adept at extracting insights from complex datasets, creating meaningful visualizations, and building predictive models. I possess a solid understanding of statistical analysis and have hands-on experience with popular tools and libraries such as Python, Pandas, scikit-learn, and data visualization libraries like Matplotlib and Plotly.")
    st.markdown("I am now actively seeking a Data Scientist role where I can leverage my interdisciplinary background, passion for data-driven decision-making, and problem-solving abilities. I am eager to collaborate with teams in tackling challenging projects and making a positive impact through data.")
    st.markdown("Thank you for visiting my portfolio website, and I look forward to connecting with you!")

with tab5:
    col5,col6 =st.columns((1,7))
    with col5:
        st.write("")
        st.image("IITM_logo.png")
        st.write("---")
        st.image("BDU_logo.png")
        st.write("---")
        st.image("BVN_logo.jpg")
    with col6:
        st.write("")
        st.markdown("<h5 style='color: orange;'> Indian Institute of Technology, Madras </h5>", unsafe_allow_html=True)
        st.markdown("IIT-M Certified Advanced Programmer with Data Science Mastery Program <br> Feb 2023 - July 2023",unsafe_allow_html=True)
        st.markdown("Currently pursuing the course from IIT-M Digital Skills Academy")
        st.write("")
        st.write("")
        st.markdown("<h5 style='color: orange;'> Bharathidasan University, Tiruchirappalli. </h5>", unsafe_allow_html=True)
        st.markdown("Master of Science in Bioinformatics <br> 2017 - 2022",unsafe_allow_html=True)
        st.markdown("CGPA : 8.06")
        st.write("")
        st.write("")
        st.markdown("<h5 style='color: orange;'> BVN matriculation higher secondary school, Pollachi </h5>", unsafe_allow_html=True)
        st.markdown("HSC <br> 2015 -2017", unsafe_allow_html=True)
        st.markdown("Percentage : 81% ")

with tab7:
        #Heading
        st.markdown("<h4 style='color: #ECE7E7;'> <u>Data Science projects: </u></h4>", unsafe_allow_html=True)

        #project-1
        st.markdown("<h5 style='color: orange;'>Predicting Breast Cancer in Patients using Optimized Support Vector Classifier </h5>", unsafe_allow_html=True)    
        st.markdown("In this project, a dataset comprising approximately 569 instances was utilized. The project workflow involved several key steps to develop an accurate machine learning model."
                    "Firstly, the dataset was loaded and subjected to an exploratory data analysis (EDA) process. Following the EDA, a feature engineering process was conducted, which involved transforming and manipulating the dataset."
                    "To construct a machine learning model, an ensemble technique was employed, which consisted of building five different models: SVM classifier, logistic regression, random forest classifier, decision tree classifier, and GradientBoosting classifier. Each model brought unique strengths to the prediction task."
                    "However, the primary focus of the project was to optimize the performance of the SVM classifier through hyperparameter tuning. To achieve this, the dataset underwent feature scaling, a technique that normalizes the range of features. Subsequently, the SVM model was fine-tuned using grid search cross-validation (CV) to determine the optimal combination of hyperparameters."
                    "Upon obtaining the best hyperparameters, a new SVM classifier was trained and evaluated. The outcome of this tuning process yielded an impressive accuracy of 98%, showcasing a significant improvement compared to the initial accuracy of 94% obtained before hyperparameter tuning.")
        github_url_1 = "https://github.com/JayaKrishanS/Predicting-Breast-Cancer-in-Patients-using-Optimized-Support-Vector-Classifier.git"
        st.markdown(f'<a href="{github_url_1}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)
        st.markdown("---")

        #Project-2
        st.markdown("<h5 style='color: orange;'>Heart Disease Prediction using a Machine Learning Model and Streamlit Application. </h5>", unsafe_allow_html=True)
        st.markdown("In this project, a Streamlit application was developed to predict heart disease using a logistic regression machine learning model. The application serves as a user-friendly interface that allows individuals to input relevant health parameters and obtain a prediction regarding the likelihood of having heart disease. The logistic regression model, a widely used classification algorithm,  was trained on a dataset containing ")
        st.markdown("")
        st.markdown("various features related to cardiovascular health. These features include factors such as age, blood pressure, cholesterol levels, and other relevant indicators. By analyzing these input variables, the logistic regression model calculates the probability of an individual having heart disease."
                    "Overall, this Streamlit application offers a user-friendly interface for predicting heart disease using a logistic regression model, enabling individuals to make informed decisions about their well-being based on their personal health parameters.")
        github_url_2 = "https://github.com/JayaKrishanS/Heart-Disease-Prediction-using-a-Machine-Learning-Model-and-Streamlit-Application..git"
        st.markdown(f'<a href="{github_url_2}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)
        linkedin_url_2 = "https://www.linkedin.com/posts/jaya-krishna-s-aab674196_datascience-machinelearning-dataanalysis-activity-7071124124831531010-TfHx?utm_source=share&utm_medium=member_desktop"
        st.markdown(f'<a href="{linkedin_url_2}" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>', unsafe_allow_html=True)
        st.markdown("---")

        #Project-3
        st.markdown("<h5 style='color: orange;'>Spam Mail Prediction using a Machine Learning Model </h5>", unsafe_allow_html=True)
        st.markdown("This is a Spam or Ham Mail Classifier, an Streamlit application designed to predict whether an email is spam ham using a Machine Learning model. It has become crucial to filter out unwanted spam messages to ensure an efficient and secure email experience. This application aims for classifying emails, saving time and reducing the risk of falling victim to phishing or other malicious activities."
                    "The objective of this project is to offer users a practical tool for identifying potential spam emails, helping them efficiently manage their email communications and reduce the risk of falling victim to malicious or unwanted content.")
        github_url_3 = "https://github.com/JayaKrishanS/Spam-Mail-Prediction-using-a-Machine-Learning-Model.git"
        st.markdown(f'<a href="{github_url_3}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)
        linkedin_url_2 = "https://www.linkedin.com/posts/jaya-krishna-s-aab674196_datascience-machinelearning-dataanalysis-activity-7075836642510454784-ErA5?utm_source=share&utm_medium=member_desktop"
        st.markdown(f'<a href="{linkedin_url_2}" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>', unsafe_allow_html=True)
        st.markdown("---")

        #Capstone
        st.markdown("<h4 style='color: #ECE7E7;'> <u>Capstone projects: </u></h4>", unsafe_allow_html=True)
        st.markdown("<h5 style='color: orange;'>Pulse Data Visualization and Exploration: A User-Friendly Tool Using Streamlit and Plotly </h5>", unsafe_allow_html=True)
        st.markdown("This project about building a visualization dashboard that displays information and insights from the Phonepe pulse Github repository in an interactive and visually appealing manner. The dashboard will have options for users to select different facts and figures to display. The data will be stored in a SQL database for efficient retrieval and the dashboard will be dynamically updated to reflect the latest data. Overall, the result of this project will be a comprehensive and user-friendly solution for extracting, transforming, and visualizing data from the Phonepe pulse Github repository.")
        github_url_4 = "https://github.com/JayaKrishanS/Phonepe-Pulse-Data-Visualization-and-Exploration-A-User-Friendly-Tool-Using-Streamlit-and-Plotly.git"
        st.markdown(f'<a href="{github_url_4}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)
        st.markdown("---")

        st.markdown("<h5 style='color: orange;'>BizCardX-Extracting-Business-Card-Data-with-OCR </h5>", unsafe_allow_html=True)
        st.markdown("In the project, a Streamlit application was developed to extract and store business card data using Optical Character Recognition (OCR) technology. The application allows users to upload an image of a business card, which is then processed using the easyOCR library to convert the text on the card into a digital format. "
                    "Once the text is extracted, the information is stored in an SQL database, enabling easy access and management of the business card data. Users can retrieve the stored data and, if necessary, make modifications or updates to ensure accuracy and completeness."
                    " The primary objective of this project is to provide a convenient solution for capturing and organizing business card information, thereby preventing the loss or misplacement of valuable contacts.")
        github_url_5 = "https://github.com/JayaKrishanS/BizCardX-Extracting-Business-Card-Data-with-OCR.git"
        st.markdown(f'<a href="{github_url_5}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)
        st.markdown("---")

with tab9:
    col3,col4 = st.columns((3,1))
    def skills():
        st.write("")
        st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">', unsafe_allow_html=True)

        st.markdown('<i class="fab fa-python"></i> Python', unsafe_allow_html=True)
        st.progress(87)
              
        st.markdown('<i class="fab fa-python"></i> Pandas, Numpy', unsafe_allow_html=True)
        st.progress(83)
        
        st.markdown('<i class="fas fa-chart-bar"></i> Matplotlib, Seaborn and Plotly', unsafe_allow_html=True)
        st.progress(80)
        
        st.markdown('<i class="fas fa-database"></i> SQL', unsafe_allow_html=True)
        st.progress(84)
        
        st.markdown('<i class="fas fa-database"></i> MongoDB', unsafe_allow_html=True)
        st.progress(75)
        
        st.markdown('<i class="fas fa-robot"></i> Machine Learning: scikit-learn', unsafe_allow_html=True)
        st.progress(83)

        st.markdown('<i class="fas fa-globe"></i> Web Application: Streamlit', unsafe_allow_html=True)
        st.progress(84)
        
    with col3:
        skills()

with tab11:
    st.write("")
    st.write("")
    st.markdown('<i class="fas fa-address-book" style="font-size: 20px;"></i>  Contact me with :', unsafe_allow_html=True)
    st.write("")

    gmail_url = "mailto:jkbioinfo99@gmail.com"
    st.markdown(f'<a href="{gmail_url}" target="_blank"><i class="far fa-envelope"></i> jkbioinfo99@gmail.com</a>', unsafe_allow_html=True)

    github_url = "https://github.com/JayaKrishanS"
    st.markdown(f'<a href="{github_url}" target="_blank"><i class="fab fa-github"></i>  GitHub</a>', unsafe_allow_html=True)

    linkedin_url = "https://www.linkedin.com/in/jaya-krishna-s-aab674196/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>', unsafe_allow_html=True)

