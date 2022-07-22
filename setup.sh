mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"21f1001588@student.onlinedegree.iitm.ac.in\"n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
" > ~/.streamlit/config.toml
