mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"21f1004586@student.onlinedegree.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=true\n\
port = 8501\n\
" > ~/.streamlit/config.toml
