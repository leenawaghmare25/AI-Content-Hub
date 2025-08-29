AI Content Hub
An intuitive and simple AI-powered web application designed to help content creators, marketers, and students overcome writer's block and enhance their writing productivity. This platform provides a suite of tools that leverage modern AI models to generate, summarize, and rephrase text with ease.

Features:
1. This project showcases a range of core and advanced features built into a single, cohesive application.

2. Content Writer: Generates original content from scratch based on a user's prompt. Users can specify topics and keywords to guide the AI's output.

3. Idea Generator: Brainstorms creative and relevant ideas for a given topic, helping users overcome writer's block.

4. Text Summarizer: Condenses long articles or documents into a concise, easy-to-read summary with the main key points.

5. Text Rewriter: Paraphrases and rephrases a block of text to improve clarity, originality, and tone.

6. Tone & Style Adjustment: An advanced feature that allows users to select a specific tone (e.g., professional, casual, academic) for the generated content, demonstrating a deeper level of AI integration.

7. Multi-Language Support: The platform can handle content generation in multiple languages, making it a versatile tool for a global audience.

Tech Stack: 
1. Frontend:

React.js: The core JavaScript library for building the user interface.

Tailwind CSS: A utility-first CSS framework for a clean and responsive design.

Axios: A promise-based HTTP client for seamless communication with the backend API.

2. Backend:

Python: The programming language used to build the server-side logic.

Flask: A lightweight and flexible web framework for creating the REST API.

Hugging Face transformers: The primary library for integrating and utilizing powerful pre-trained AI models.

3. Deployment:

Netlify: For hosting the static React frontend.

Render: For deploying the Flask backend API.

4. Installation and Usage
To run the project locally, follow these steps.

(i)Clone the repository:

git clone [https://github.com/leenawaghmare25/AI-Content-Hub.git](https://github.com/leenawaghmare25/AI-Content-Hub.git)
cd AI-Content-Hub

(ii) Backend Setup:

# Navigate to the backend directory
cd backend

# Create and activate a Python virtual environment
python -m venv venv
# On Windows: venv\Scripts\activate
# On macOS/Linux: source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run the Flask backend
flask run

(iii)Frontend Setup:

# Open a new terminal and navigate to the frontend directory
cd frontend

# Install npm packages
npm install

# Start the React development server
npm start

The application will be accessible at 

License
This project is licensed under the MIT License.

Acknowledgments
A special thank you to my sister for the inspiring project idea.

The Hugging Face community for their incredible work and open-source models.
