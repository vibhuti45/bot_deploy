export PATH="/opt/homebrew/opt/python@3.10/libexec/bin:$PATH"
export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"
export SSL_CERT_FILE=$(python3 -c "import certifi; print(certifi.where())")
