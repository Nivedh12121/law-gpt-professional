#!/usr/bin/env python3
"""
LAW-GPT - Comprehensive Legal Assistant
Recreating the beautiful dark interface from law-gpt-comprehensive-fixed.html
"""

import streamlit as st
import json
import time
from datetime import datetime
import sys
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

# Configure page
st.set_page_config(
    page_title="LAW-GPT - Comprehensive Legal Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Recreating the exact dark theme from your HTML
st.markdown("""
<style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: #0a0a0a !important;
        color: #e5e5e5 !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    .stToolbar {display: none;}
    
    /* Welcome Screen Styles */
    .welcome-screen {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 40px;
        background: linear-gradient(135deg, #1e1e1e, #2a2a2a);
        margin: -1rem;
    }
    
    .welcome-card {
        max-width: 600px;
        padding: 60px 40px;
        background: rgba(40, 40, 40, 0.8);
        border-radius: 20px;
        border: 1px solid rgba(80, 80, 80, 0.5);
        text-align: center;
    }
    
    .logo {
        font-size: 4rem;
        margin-bottom: 15px;
    }
    
    .title {
        font-size: 2.8rem;
        font-weight: 600;
        margin-bottom: 15px;
        color: #f5f5f5;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: #a0a0a0;
        margin-bottom: 35px;
        line-height: 1.4;
    }
    
    /* Chat Interface Styles */
    .chat-header {
        padding: 25px;
        text-align: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        background: rgba(20, 20, 20, 0.8);
        border-radius: 15px;
    }
    
    .chat-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 8px;
        color: #f5f5f5;
    }
    
    .chat-subtitle {
        color: #cccccc;
        font-size: 1rem;
    }
    
    /* Message Styles */
    .user-message {
        background: rgba(40, 40, 40, 0.8);
        border: 1px solid rgba(80, 80, 80, 0.5);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        margin-left: auto;
        max-width: 95%;
        text-align: right;
        color: #e5e5e5;
    }
    
    .assistant-message {
        background: rgba(30, 30, 30, 0.8);
        border: 1px solid rgba(60, 60, 60, 0.5);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        margin-right: auto;
        max-width: 95%;
        color: #e5e5e5;
    }
    
    .system-message {
        background: rgba(25, 25, 25, 0.8);
        border: 1px solid rgba(50, 50, 50, 0.5);
        border-radius: 15px;
        padding: 20px;
        margin: 15px auto;
        max-width: 70%;
        text-align: center;
        color: #e5e5e5;
    }
    
    /* Legal Response Styling */
    .legal-highlight {
        background: rgba(255, 193, 7, 0.2);
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 15px 0;
        border-radius: 8px;
    }
    
    .legal-warning {
        background: rgba(220, 53, 69, 0.2);
        border-left: 4px solid #dc3545;
        padding: 15px;
        margin: 15px 0;
        border-radius: 8px;
    }
    
    .legal-section {
        background: rgba(34, 197, 94, 0.2);
        border-left: 4px solid #22c55e;
        padding: 15px;
        margin: 15px 0;
        border-radius: 8px;
    }
    
    /* Input Styling */
    .stTextArea textarea {
        background: rgba(30, 30, 30, 0.8) !important;
        border: 1px solid rgba(60, 60, 60, 0.5) !important;
        border-radius: 15px !important;
        color: #e5e5e5 !important;
        font-size: 16px !important;
        padding: 18px 20px !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stTextArea textarea::placeholder {
        color: rgba(160, 160, 160, 0.8) !important;
    }
    
    /* Button Styling */
    .stButton button {
        background: rgba(80, 80, 80, 0.8) !important;
        border: 1px solid rgba(100, 100, 100, 0.5) !important;
        border-radius: 15px !important;
        color: #e5e5e5 !important;
        font-weight: 600 !important;
        padding: 18px 25px !important;
        transition: all 0.3s ease !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stButton button:hover {
        background: rgba(100, 100, 100, 0.8) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Start Button Special Styling */
    .start-button button {
        background: rgba(255, 255, 255, 0.9) !important;
        color: #1a1a1a !important;
        border-radius: 25px !important;
        padding: 16px 40px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    
    .start-button button:hover {
        background: rgba(255, 255, 255, 1) !important;
        transform: translateY(-2px) !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .welcome-card { padding: 40px 20px; }
        .title { font-size: 2.5rem; }
        .user-message, .assistant-message { max-width: 95%; }
    }
</style>
""", unsafe_allow_html=True)

class LAWGPTApp:
    """LAW-GPT Application with your beautiful dark interface"""
    
    def __init__(self):
        self.law_gpt_system = None
        self.initialize_system()
        self.initialize_session_state()
    
    def initialize_session_state(self):
        """Initialize session state"""
        if 'started' not in st.session_state:
            st.session_state.started = False
        if 'messages' not in st.session_state:
            st.session_state.messages = []
    
    def initialize_system(self):
        """Initialize the LAW-GPT system"""
        try:
            from high_accuracy_law_gpt import HighAccuracyLawGPT
            
            if 'law_gpt_system' not in st.session_state:
                with st.spinner("🚀 Loading LAW-GPT System..."):
                    st.session_state.law_gpt_system = HighAccuracyLawGPT()
            
            self.law_gpt_system = st.session_state.law_gpt_system
            
        except Exception as e:
            st.error(f"❌ System initialization error: {e}")
            self.law_gpt_system = None
    
    def render_welcome_screen(self):
        """Render welcome screen exactly like your HTML"""
        st.markdown("""
        <div class="welcome-screen">
            <div class="welcome-card">
                <div class="logo">⚖️</div>
                <h1 class="title">LAW-GPT</h1>
                <p class="subtitle">
                    Welcome to Powerful LAW-GPT
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Center the start button with special styling
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.markdown('<div class="start-button">', unsafe_allow_html=True)
            if st.button("🚀 Start", key="start_button", use_container_width=True):
                st.session_state.started = True
                st.session_state.messages.append({
                    "role": "system",
                    "content": "Welcome to LAW-GPT Professional! I'm your AI legal assistant. Ask me about any legal matter and I'll provide detailed guidance.",
                    "timestamp": datetime.now().strftime("%H:%M")
                })
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    
    def render_chat_interface(self):
        """Render chat interface exactly like your HTML"""
        # Chat Header
        st.markdown("""
        <div class="chat-header">
            <h2 class="chat-title">⚖️ LAW-GPT Professional</h2>
            <p class="chat-subtitle">AI-Powered Legal Assistant • Always Available</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Chat Messages
        self.render_messages()
        
        # Input Area
        self.render_input_area()
    
    def render_messages(self):
        """Render chat messages with your styling"""
        for message in st.session_state.messages:
            if message["role"] == "system":
                st.markdown(f"""
                <div class="system-message">
                    <strong>{message["content"]}</strong><br>
                    <small style="color: rgba(255, 255, 255, 0.6); margin-top: 8px;">{message["timestamp"]}</small>
                </div>
                """, unsafe_allow_html=True)
            
            elif message["role"] == "user":
                st.markdown(f"""
                <div class="user-message">
                    {message["content"]}
                    <div style="font-size: 0.8rem; color: rgba(255, 255, 255, 0.6); margin-top: 8px;">{message["timestamp"]}</div>
                </div>
                """, unsafe_allow_html=True)
            
            elif message["role"] == "assistant":
                # Format legal response with proper styling
                formatted_content = self.format_legal_response(message["content"])
                st.markdown(f"""
                <div class="assistant-message">
                    {formatted_content}
                    <div style="font-size: 0.8rem; color: rgba(255, 255, 255, 0.6); margin-top: 8px;">{message["timestamp"]}</div>
                </div>
                """, unsafe_allow_html=True)
    
    def format_legal_response(self, content):
        """Format legal response with proper highlighting"""
        # Add legal section highlighting for important sections
        if "Section" in content and ("IPC" in content or "CrPC" in content):
            content = content.replace("Section", '<span style="color: #22c55e; font-weight: 600;">Section</span>')
        
        # Add warning highlighting for disclaimers
        if "Disclaimer" in content or "Warning" in content:
            content = f'<div class="legal-warning">{content}</div>'
        
        # Add highlight for important legal terms
        legal_terms = ["punishment", "imprisonment", "fine", "court", "lawyer", "legal", "Article", "Constitution"]
        for term in legal_terms:
            if term in content:
                content = content.replace(term, f'<strong style="color: #ffc107;">{term}</strong>')
        
        return content
    
    def render_input_area(self):
        """Render input area"""
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Input form
        with st.form(key="message_form", clear_on_submit=True):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                user_input = st.text_area(
                    "",
                    placeholder="Describe your legal question or situation...",
                    height=80,
                    key="message_input"
                )
            
            with col2:
                st.markdown("<br>", unsafe_allow_html=True)
                send_button = st.form_submit_button("Send", use_container_width=True)
            
            if send_button and user_input.strip():
                self.process_message(user_input.strip())
    
    def process_message(self, user_input):
        """Process user message"""
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
        # Generate AI response
        if self.law_gpt_system:
            try:
                with st.spinner("🔍 Analyzing your legal query..."):
                    result = self.law_gpt_system.answer_legal_query(user_input)
                    response = result['response']
                
                # Add assistant message
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "timestamp": datetime.now().strftime("%H:%M")
                })
                
            except Exception as e:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": f"I apologize, but I encountered an error processing your query: {str(e)}. Please try again or rephrase your question.",
                    "timestamp": datetime.now().strftime("%H:%M")
                })
        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": "I'm sorry, but the legal AI system is currently unavailable. Please try again later.",
                "timestamp": datetime.now().strftime("%H:%M")
            })
        
        st.rerun()
    
    def run(self):
        """Run the application"""
        if not st.session_state.started:
            self.render_welcome_screen()
        else:
            self.render_chat_interface()

def main():
    """Main function"""
    app = LAWGPTApp()
    app.run()

if __name__ == "__main__":
    main()
