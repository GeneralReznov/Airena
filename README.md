  # 🚀 Alrena
 
 Alrena is an AI-powered platform that provides entertainment and educational experiences through various interactive features.
 
 ---
 
 ## 📌 Problem Statement
 
 **Problem Statement 1 – Weave AI Magic with GROQ**
 
 ---
 
 ## 🎯 Objective
 
 Our project solves the challenge of creating an interactive, AI-powered multimedia platform that combines conversational AI, personalized quizzes, and engaging gaming experiences.
 It serves learners, gamers, and content creators seeking immersive, intelligent tools for education and entertainment. 

 A real-world use case for this project is providing an interactive, AI-powered multimedia platform that enables users to engage in natural conversations, generate personalized quizzes, and participate in AI-enhanced gaming—all within one application.
 By integrating multimodal AI for text, speech, image, and audio processing, the app delivers a more immersive and adaptive user experience, similar to how leading media and entertainment platforms personalize content and interactions.
 
 ---
 
 ## 🧠 Team & Approach
 
 ### Team Name:  
 `Code Glitchers`
 
 ### Team Members:  
 - Mokshit Kaushik (Team Leader)  
 - Kanishka Sharma 
 - Sumukhi Tripathi
 - Parth Sharma
 
 ### Approach:  
 - We chose this problem to explore the potential of advanced multimodal AI to create an interactive platform combining text, speech, image, and audio processing.
 - Focused on solving real-world needs in education, gaming, and content creation by providing personalized, real-time AI experiences.
 - Utilized Groq’s high-performance AI and agentic tooling for fast, accurate, and context-aware personalized answers.
 - Integrated sponsor technologies like Fluvio for dynamic quiz generation and game state tracking, and ScreenPipe for secure screen recording.
 
 ### Key Challenges:
 - Integrating multiple AI services (Groq, Fluvio, ScreenPipe) smoothly for a seamless user experience across chat, quizzes, and gaming.
 - Modularizing AI workflows during brainstorming, enabling flexible and scalable integration of different AI components.
 - Ensuring data privacy and security, leading to local recording to protect user content.
 - Managing real-time performance for interactive features, balancing speed and accuracy in speech, text, and game state processing.
  
 ---
 
 ## 🛠️ Tech Stack
 
 ### Core Technologies Used:
- Flask: Web framework
- SQLAlchemy: Database ORM
- Groq API: AI chat functionality
- Fluvio: Quiz question generation and Game tracking
- Screenpipe: Local Screen recording.
- Flask-Mail: Email services
- HTML/CSS/JavaScript: Frontend development
- Hosting: Render
 
 ### Sponsor Technologies Used :
 - ✅ **Groq:** Used Groq’s ultra-fast AI inference capabilities to power all conversational, multimodal, and agentic features in the app. Groq’s LPU-based architecture enabled real-time chat, text-to-speech, speech-to-text, and image/audio processing with ultra-low latency, ensuring seamless user experiences.    
 - ✅ **Fluvio:** Integrated Fluvio for real-time data handling, specifically to generate quizzes on the fly based on user-selected genres and to track game state (such as health and score) during AI-powered gaming sessions.  
 - ✅ **Screenpipe:** Used Screenpipe to implement secure, efficient screen-based analytics and workflows. This included recording gameplay sessions locally, enabling users to download and share their experiences without compromising privacy.  
 ---
 
 ## ✨ Key Features
 
  The most important features of our project:
 
 - ✅ AI Chat: Chat with our advanced AI assistant powered by Groq  
 - ✅ Educational Quizzes: Test your knowledge with AI-generated quizzes
 - ✅ AI Games: Play games enhanced with artificial intelligence  
 - ✅ Screen Recording: Record and share your gameplay experiences
 
![WhatsApp Image 2025-04-20 at 4 45 18 PM](https://github.com/user-attachments/assets/aa7c64f2-c056-4d86-ad96-79c3cf522420)
![WhatsApp Image 2025-04-20 at 4 47 12 PM](https://github.com/user-attachments/assets/be9cb0da-34aa-4fbb-bfd3-2797146ff5c9)
![WhatsApp Image 2025-04-20 at 4 43 30 PM](https://github.com/user-attachments/assets/4c19bc89-7c7e-4cb2-bf80-6a2a15ae20ae)
 
 ---
 
 ## 📽️ Demo & Deliverables
 
 - **Demo Video Link:** https://youtu.be/4pO9QZn0090
 - **Pitch Deck / PPT Link:** https://drive.google.com/file/d/1boWBhlWa2cmIY2c1ndHBV50-wIKRa0bS/view?usp=sharing
 - **App Link:** https://airenaisthebest.onrender.com/
 
 ---
 
 ## ✅ Tasks & Bonus Checklist
 
 - ✅ **All members of the team completed the mandatory task - Followed at least 2 of our social channels and filled the form** (Details in Participant Manual)  
 - ✅ **All members of the team completed Bonus Task 1 - Sharing of Badges and filled the form (2 points)**  (Details in Participant Manual)
 - ✅ **All members of the team completed Bonus Task 2 - Signing up for Sprint.dev and filled the form (3 points)**  (Details in Participant Manual)
 
 
 ---
 
 ## 🧪 How to Run the Project
 
 ### Requirements:
 - Python, Docker(Rust Compiler instead will work too).
 - API Keys (Groq)
 - .env file setup ()
 
 ### Local Setup:
 1. Clone the repository:
```bash
git clone https://github.com/GeneralReznov/Alrena.git
cd Airena
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with the following variables:
```
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
GROQ_API_KEY=your_groq_api_key
```

5. Initialize the database:
```bash
python reset_db.py
```

6. Run the application:
```bash
python main.py
```
 
 ## 🧬 Future Scope
 
 Extensions and Follow-up Features:
 
 - 📈 Incorporate additional AI services (e.g., sentiment analysis, emotion detection) to enrich user interactions. 
 - 🛡️ Implement end-to-end encryption for all user data and media recordings.  
 - 🌐 Implement accessibility features such as screen readers, subtitles, and voice commands for users with disabilities.
 - 🎮 Expand gaming features by introducing new Multiplayer game powered by AI and adaptive difficulty(Tekken Type). 
 
 ---
 
 ## 📎 Resources / Credits
 
 - Groq API: Utilized for conversational AI, text-to-speech, speech-to-text, and multimodal (text, image, audio) processing.Uses combination of LLaMA 3.7 and LLaMA 4 models for conversation and image processing,DeepSeek 2.3 model for agentic tool usage and Whisper V3 for advanced speech-to-text and audio processing.
 - Fluvio Generator: Used to dynamically generate quizzes based on user-selected genres.
 - ScreenPipe: Integrated for secure, local screen recording and sharing features.     
 
 ---
 
 ## Acknowledgement
 - Special thanks to Groq, Fluvio, and ScreenPipe for their sponsorship, APIs, and support in enabling advanced multimodal features.
 - Gratitude to the NameSpace community and documentation teams especially Hackhazards community for providing guidance and resources that accelerated project delivery.
 
 ## 🏁 Final Words
 
 - This hackathon journey was an incredible experience filled with both challenges and exciting breakthroughs. 
 - Integrating multiple cutting-edge AI technologies like Groq, Fluvio, and Screenpipe pushed us to think creatively about seamless interoperability and real-time performance.
 - We learned a lot about managing complex multimodal data flows and balancing innovation with user privacy and security.
 - Some of the most fun moments came from seeing the AI-powered space shooter game come alive and watching the quiz generator adapt dynamically to user choices.
 
 ---
