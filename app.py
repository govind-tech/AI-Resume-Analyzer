import streamlit as st 
import re 

def contains_skills(text,skill):
    pattern =r"\b" + re.escape(skill.lower()) +r"\b"
    return re.search(pattern, text.lower()) is not None

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("AI Resume Analyzer & Job Matcher")

st.write(
    "Analyze Your Resume and Compare Your Skills "
    " With a Job Description."
)

name = st.text_input("Enter your name:")

resume = st.file_uploader(
    "Upload Your Resume(PDF)",
    type="pdf"
)

job_description = st.text_area(
    "Paste the Job description Here",
    height=200
)

if st.button("Analyzer Resume"):
    if not name:
        st.warning("Please Enter Your Name.")
        
    elif resume is None:
        st.warning("Please Upload Your Resume.")
        
    elif not job_description.strip():
        st.warning("Please Enter a Job Description.")
        
    else:
        st.success("All inputs received Successfully.")
        
        import pymupdf 
        
        document = pymupdf.open(stream=resume.getvalue(), filetype="pdf")
        
        resume_text = ""
        
        for page in document:
            resume_text += page.get_text()
            
        document.close()
        
        if resume_text.strip():
            st.subheader("Extracted Resume Text")
            st.text_area(
                "Resume content",
                resume_text,
                height = 300
            )
            
            skill_list = [
                "Python",
                "Java",
                "C++",
                "SQL",
                "HTML",
                "CSS",
                "JavaScript",
                "Django",
                "Flask",
                "FastAPI",
                "Machine Learning",
                "Deep Learning",
                "TensorFlow",
                "PyTorch",
                "OpenCV",
                "Git",
                "GitHub",
                "Data Structure",
                "Algorithms",
                "React",
                "Node.js",
                "MongoDB",
                "PostgreSQL",
                "Data Analysis",
                "NumPy",
                "Pandas",
                "Scikit-learn",
                "Statistics",
                "Natural Language Processing",
                "Computer Vision",
                "REST API",
                "Git",
                "Linux",
                "AWS",
                "Docker",
                "System Design",
                "OOPs"

            ]
            
            resume_lower = resume_text.lower()
            
            found_skills = []
            
            for skill in skill_list:
                if contains_skills(resume_text, skill):
                    found_skills.append(skill)
                    
            
            st.subheader("Skills Found in Your Resume")
            
            if found_skills:
                st.write(found_skills)
                
            else:
                st.warning("No Skills Found in Resume.")
                
            
            job_lower = job_description.lower()
            
            required_skills = []
            
            for skill in skill_list:
                if contains_skills(job_description, skill):
                    required_skills.append(skill)
                    
            matching_skills = []
            
            for skill in required_skills:
                if skill in found_skills:
                    matching_skills.append(skill)
                    
            missing_skills = []
            
            for skill in required_skills:
                if skill not in found_skills:
                    missing_skills.append(skill)
                    
            if required_skills:
                match_percentage = (
                    len(matching_skills) / len(required_skills)
                )*100
                
            else: 
                match_percentage = 0
                
            
            st.subheader("Job Match Report")
            
            col1,col2 = st.columns(2)
            
            with col1 :
                st.metric(
                    "Skill Match",
                    f"{match_percentage:.1f}%"
                )
                
            with col2:
                st.metric(
                    "Required Skills",
                    len(required_skills)
                )
                
                
            st.progress(match_percentage/100)
            
            if not required_skills:
                st.info("Enter a Job description containing support technical skills.")
                
            elif match_percentage >=80:
                st.success("Strong skill overlap with this job description.")
                
            elif match_percentage >=50:
                st.info("Moderate skill overlap. Review the required and missing skills.")
                
            else:
                st.warning("Low skill overlap. Review the required and missing skills.")
            
            st.subheader("✅ Matching Skill")
            
            if matching_skills:
                for skill in matching_skills:
                    st.write(f"✓ {skill}")
                    
            else:
                st.info("No Matching Skill Found.")
                    
            st.subheader("📌 Missing Skills")
                
            if missing_skills:
                for skill in missing_skills:
                    st.write(f"• {skill}")
                        
            else:
                st.success("No missing skills detected!")
                
            st.subheader("💡 Recommendation")
            
            if missing_skills:
                st.write(
                    "Consider learning or practicing these skills "
                    "to better align your resume with the job description:"
                )
                
                for skill in missing_skills:
                    st.write(f"- Study and Practice {skill}.")
            else:
                st.success(
                    "Your Resume includes all the skills detected "
                    "in this job description!"
                )        
            
            st.subheader("Download Your Report")
            
            report = f"""
            AI RESUME ANALYZER & JOB MATCHER
            ================================
            
            Condidate: {name}
            
            Resume-to-Job Skill Match:{match_percentage:.1f}%
            
            Required Skills:
            {",".join(required_skills) if required_skills else "None Detected"}
            
            Matching Skills:
            {",".join(matching_skills) if matching_skills else "None"}
            
            Missing Skills:
            {",".join(missing_skills) if missing_skills else "None"}
            
            Recommendations:
            {",".join("Practice "+ skill for skill in missing_skills) if missing_skills else "No Missing Skills Detected."}
            
            """
            
            st.download_button(
                label ="Download Match Report",
                data = report,
                file_name = "resume_match_report.txt",
                mime ="text/plain"
            )
            
            
        else :
            st.error(
                "No readable text was found in this PDF. "
                "Please upload a text-based PDF resume."
                
            )
            
            st.info(
                "Tip : Open Your PDF and Try selecting and copying "
                "some Text. If you cannot select text, the PDF may  "
                "Require OCR."
            )