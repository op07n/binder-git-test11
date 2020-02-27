from subprocess import Popen
import os

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    os.chdir('tech-news-cluster/tech_news_cluster')
    Popen(["streamlit", "run", "streamlit_app.py", "--browser.serverAddress=0.0.0.0", "--browser.gatherUsageStats=False", "--server.enableCORS=False"])
