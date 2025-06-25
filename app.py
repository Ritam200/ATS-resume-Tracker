# app.py

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import PyPDF2 as pdf

# Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro Function
def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

# PDF Text Extractor
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages(len(reader.pages)):
        page=reader.pages[page]
        text += str(page.extract_text())
    return text

# Streamlit UI
st.title("Smart ATS Resume Analyzer")
st.text("Improve Your Resume ATS")

jd = st.text_area("Enter the Job Description details of the role you are applying for")
uploaded_file = st.file_uploader("Upload Your Resume in PDF", type=["pdf"],help="Please Upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        resume_text = input_pdf_text(uploaded_file)

        ## prompt template       
        input_prompt = """
# Hey Act Like a skilled or very experience ATS(Application Tracking System)
# with a deep understanding of tech feild,software engineering,data science,data analyst
# and big data engineer.Your task is to evaluate the resume based on the given job description.
# You must consider the job market is very competitive and you should provide best 
# assistence for improving the resumes.Assign the percentage Matching based on JD and
# the missing keywards with high accuracy
# resume:{text}
# description:{jd}

# I want the response in one single string having the structure
# {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
#   """

        response = get_gemini_response(input_prompt)
        st.subheader("Response")
        st.write(response)
    else:
        st.error("Please upload a PDF file.")
# from dotenv import load_dotenv

# load_dotenv()## load all the environment variables
# import base64
# import streamlit as st
# import os
# import io
# from PIL import Image 
# import pdf2image
# import google.generativeai as genai
# import PyPDF2 as pdf

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# ## Gemini Pro Response
# def get_gemini_response(input):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content(input)
#     return response.text

# def input_pdf_text(uploaded_file):
#     reader=pdf.PdfReader(uploaded_file)
#     text=""
#     for page in reader(len(reader.pages)):
#         page=reader.pages[page]
#         text+=str(page.extract_text())
#         return text
#     ## prompt template
#     input_prompt="""
# Hey Act Like a skilled or very experience ATS(Application Tracking System)
# with a deep understanding of tech feild,software engineering,data science,data analyst
# and big data engineer.Your task is to evaluate the resume based on the given job description.
# You must consider the job market is very competitive and you should provide best 
# assistence for improving the resumes.Assign the percentage Matching based on JD and
# the missing keywards with high accuracy
# resume:{text}
# description:{jd}

# I want the response in one single string having the structure
# {{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
#   """
    # if uploaded_file is not None:
        ## Convert the PDF to image
    #     images=pdf2image.convert_from_bytes(uploaded_file.read())

    #     first_page=images[0]

    #     # Convert to bytes
    #     img_byte_arr = io.BytesIO()
    #     first_page.save(img_byte_arr, format='JPEG')
    #     img_byte_arr = img_byte_arr.getvalue()

    #     pdf_parts = [
    #         {
    #             "mime_type": "image/jpeg",
    #             "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
    #         }
    #     ]
    #     return pdf_parts
    # else:
    #     raise FileNotFoundError("No any files uploaded")

## Streamlit App
# st.title("Smart ATS Resume Analyzer")
# st.text("Improve Your Resume Description")
# jd=st.text_area("Enter the Job Description details of the role you are applying for: ")
# uploaded_file=st.file_uploader("Upload Your Resume in (PDF)",type="pdf",help="Please Upload the PDF")

# submit=st.button("Submit")

# if submit:
#     if uploaded_file is not none:
#         text=input_pdf_text(uploaded_file)
#       response=get_gemini_response(input_prompt)
#       st.subheader(response)

# st.set_page_config(page_title="ATS Resume/CV Analyzer")
# st.header("ATS Resume Analyzer System")
# input_text=st.text_area(" Enter the Job Description Details of the role you are applying for: ",key="input")
# uploaded_file=st.file_uploader("Upload your resume/CV in (PDF) format...",type=["pdf"])


# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")


# submit1 = st.button("Tell Me About The Resume")

# submit2 = st.button("How Can I Improve My Skills")

#submit4 = st.button("what Are The Keywords That Are Missing")

# submit3 = st.button("Percentage match")

# input_prompt1 = """
#  You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
#   Please share your professional evaluation on whether the candidate's profile aligns with the role. 
#  Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """
# # input_prompt2 = """You are an Technical Human Resource Manager with expertise in Data Science,Full Stack Web Development,Big Data Engineering,DEVOPS,Data Analyst
# # your role is to scrutinize the resume in light of the job description provided.
# # Share your insights on the candidate's suitability for the role from an HR perspective.
# # Additionally,offer advice on enhancing the candidate's skills and identify areas where 
# # """

# input_prompt3 = """
# You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role data science or Full Stack Web Development,Big Data Engineering,DEVOPS,Data Analyst and Deep ATS functionality, 
# your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
# the job description. First the output should come as percentage and then keywords missing and last final thoughts.
# """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt1,pdf_content,input_text)
#         st.subheader("The System Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")

# elif submit3:
#     if uploaded_file is not None:
#         pdf_content=input_pdf_setup(uploaded_file)
#         response=get_gemini_response(input_prompt3,pdf_content,input_text)
#         st.subheader("The System Repsonse is")
#         st.write(response)
#     else:
#         st.write("Please uplaod the resume")



    