"""
Modern Dashboard Streamlit App with Query Parameter Navigation
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="SEO & Marketing Tools",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state for authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ============================================================================
# AUTHENTICATION GATE - NOTHING RENDERS UNTIL USER IS AUTHENTICATED
# ============================================================================

def check_password():
    """Returns True if user is authenticated. Renders login page if not."""

    def password_entered():
        """Validates credentials from Streamlit secrets."""
        try:
            # Get credentials from Streamlit secrets
            correct_username = st.secrets["APP_USERNAME"]
            correct_password = st.secrets["APP_PASSWORD"]

            if (st.session_state["username"] == correct_username and
                st.session_state["password"] == correct_password):
                st.session_state.authenticated = True
                # Clear password from session state for security
                del st.session_state["password"]
                del st.session_state["username"]
            else:
                st.session_state.authenticated = False

        except KeyError:
            st.error("⚠️ Authentication credentials not configured in secrets.toml")
            st.stop()

    # If not authenticated, show ONLY the login form
    if not st.session_state.authenticated:
        # Login page CSS
        st.markdown("""
        <style>
            /* Hide Streamlit branding */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}

            /* Login page styling */
            .login-container {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                padding: 3rem;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
        </style>
        """, unsafe_allow_html=True)

        # Center the login form
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.markdown("<br><br><br>", unsafe_allow_html=True)
            st.markdown("# 🚀 SEO & Marketing Tools")
            st.markdown("### Please login to continue")
            st.markdown("<br>", unsafe_allow_html=True)

            st.text_input("Username", key="username", placeholder="Enter username")
            st.text_input("Password", type="password", key="password", placeholder="Enter password")
            st.button("Login", on_click=password_entered, type="primary", use_container_width=True)

            # Show error only after a failed login attempt
            if "authenticated" in st.session_state and not st.session_state.authenticated:
                if "username" not in st.session_state:  # Error was triggered by failed login
                    st.error("😕 Username or password incorrect")

        # STOP execution - do not render anything else
        st.stop()

    return True

# Authentication gate - stops here if not authenticated
check_password()

# ============================================================================
# AUTHENTICATED USER AREA - Only renders if authentication passes
# ============================================================================

# Custom CSS for modern card design (only loads for authenticated users)
st.markdown("""
<style>
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Dashboard container */
    .dashboard-container {
        padding: 2rem 0;
    }

    /* Style the buttons to look like cards */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
        color: white;
        height: 320px;
        width: 100%;
        text-align: left;
        font-size: 0.85rem;
        line-height: 1.4;
        white-space: pre-wrap;
    }

    .stButton > button:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        color: white;
    }

    /* First column = LinkedIn (blue) */
    div[data-testid="column"]:first-child .stButton > button {
        background: linear-gradient(135deg, #0077B5 0%, #00A0DC 100%);
    }

    div[data-testid="column"]:first-child .stButton > button:hover {
        background: linear-gradient(135deg, #0088CC 0%, #00B0EC 100%);
    }

    /* Second column = Keywords (purple) */
    div[data-testid="column"]:nth-child(2) .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    div[data-testid="column"]:nth-child(2) .stButton > button:hover {
        background: linear-gradient(135deg, #778efa 0%, #875bac 100%);
    }


    /* Header styling */
    .dashboard-header {
        text-align: center;
        margin-bottom: 3rem;
    }

    .dashboard-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .dashboard-subtitle {
        font-size: 1.3rem;
        color: #666;
        font-weight: 400;
    }

    /* Back button styling */
    .back-button {
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def render_dashboard():
    """Render the modern card-based dashboard."""

    # Header
    st.markdown("""
    <div class="dashboard-header">
        <h1 class="dashboard-title">🚀 SEO & Marketing Tools</h1>
        <p class="dashboard-subtitle">Select a tool to get started with your analysis</p>
    </div>
    """, unsafe_allow_html=True)

    # Logout button (top right)
    col1, col2, col3 = st.columns([4, 1, 1])
    with col3:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # App cards in two columns
    col1, col2 = st.columns(2, gap="large")

    with col1:
        # LinkedIn Analysis Card - the button IS the card
        linkedin_text = """📊

LinkedIn Analysis

Complete LinkedIn intelligence platform for analyzing company presence and generating content

Features:
• Scrape and analyze 50+ LinkedIn posts
• AI-powered voice & tone profiling
• Content strategy analysis
• Competitor comparison dashboard
• Generate posts in client's voice
• SEO keyword integration
• Engagement metrics tracking"""

        if st.button(linkedin_text, key="linkedin_btn", use_container_width=True):
            st.query_params["app"] = "linkedin"
            st.rerun()

    with col2:
        # Keyword Research Card - the button IS the card
        keywords_text = """🔍

Keyword Research

Advanced SEO keyword research tool with competitor analysis and trend tracking

Features:
• Search volume & CPC data
• 100+ related keyword suggestions
• Competitor URL analysis
• Opportunity scoring algorithm
• 12-month trend visualization
• Seasonality detection
• Export to CSV/JSON"""

        if st.button(keywords_text, key="keywords_btn", use_container_width=True):
            st.query_params["app"] = "keywords"
            st.rerun()

    # Footer info
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("💡 **Tip:** Each tool includes advanced features, data export, and AI-powered insights to accelerate your marketing workflows.")

def render_app(app_name):
    """Render the selected app based on query parameter."""

    # Back to dashboard button
    if st.button("← Back to Dashboard", key="back_btn", use_container_width=False):
        st.query_params.clear()
        st.rerun()

    # Logout button in sidebar
    with st.sidebar:
        st.markdown("### Navigation")
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.authenticated = False
            st.query_params.clear()
            st.rerun()

        st.divider()
        st.caption("Currently viewing:")
        if app_name == "linkedin":
            st.info("📊 LinkedIn Analysis")
        elif app_name == "keywords":
            st.info("🔍 Keyword Research")

    # Import and render the appropriate app
    if app_name == "linkedin":
        from app_linkedin import render_linkedin_app
        render_linkedin_app()

    elif app_name == "keywords":
        from app_keywords import render_keywords_app
        render_keywords_app()

    else:
        st.error(f"Unknown app: {app_name}")
        st.info("Returning to dashboard...")
        st.query_params.clear()
        st.rerun()

# Main application flow
if not check_password():
    st.stop()

# Check if an app is selected via query params
try:
    selected_app = st.query_params.get("app")
except:
    selected_app = None

if selected_app:
    # Render the selected app
    render_app(selected_app)
else:
    # Render the dashboard
    render_dashboard()
